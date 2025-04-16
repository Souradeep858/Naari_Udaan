from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
CORS(app, supports_credentials=True)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'your_secret_key_here'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Ensure uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Model for raw material listings
class RawMaterialListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to add listing
@app.route("/api/listings", methods=["POST"])
def add_listing():
    data = request.form
    image = request.files.get("image")
    filename = None

    if image and image.filename.split('.')[-1].lower() in app.config['ALLOWED_EXTENSIONS']:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    listing = RawMaterialListing(
        name=data.get("name"),
        description=data.get("description"),
        price=float(data.get("price")),
        location=data.get("location"),
        image_url=filename
    )
    db.session.add(listing)
    db.session.commit()
    return jsonify({"message": "Listing added successfully"}), 201

# Route to get listings
@app.route("/api/listings", methods=["GET"])
def get_listings():
    listings = RawMaterialListing.query.all()
    return jsonify([
        {
            "id": listing.id,
            "name": listing.name,
            "description": listing.description,
            "price": listing.price,
            "location": listing.location,
            "image_url": f"/uploads/{listing.image_url}" if listing.image_url else None,
        }
        for listing in listings
    ])

# Serve uploaded images
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return app.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route to add an item to the cart
@app.route("/api/add-to-cart", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    listing_id = data.get('listing_id')

    if not listing_id:
        return jsonify({"error": "Missing listing_id"}), 400

    listing = RawMaterialListing.query.get(listing_id)
    if not listing:
        return jsonify({"error": "Listing not found"}), 404

    if 'cart' not in session:
        session['cart'] = []

    for item in session['cart']:
        if item['id'] == listing.id:
            item['quantity'] += 1
            break
    else:
        session['cart'].append({
            'id': listing.id,
            'name': listing.name,
            'price': listing.price,
            'quantity': 1
        })

    session.modified = True
    return jsonify({"message": "Item added to cart successfully"}), 200

# Route to view the cart
@app.route("/api/cart", methods=["GET"])
def view_cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    return jsonify({"cart": cart, "total_price": total_price})

# Test session route
@app.route("/test")
def test_session():
    return jsonify({"session_cart": session.get("cart", [])})

if __name__ == "__main__":
    app.run(debug=True)
