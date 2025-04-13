# 🌸 Naari Udaan: AI for Financial Empowerment of Rural Women

## 📌 Project Overview
**Naari Udaan** is a low-code, multilingual AI-powered web platform designed to promote financial literacy and micro-investment education among rural women in India. It combines AI chat, sentiment detection, and gamified learning modules in local languages like Hindi, Bengali, and Marathi.

---

## 🔄 Project Workflow
![Workflow Diagram](workflow.png)

### 🧠 AI-Powered Interaction Flow
1. **User Onboarding**
   - User selects preferred language and avatar.
   - Flask backend renders welcome screen with dynamic content.

2. **Mood & Sentiment Detection**
   - User types how she is feeling.
   - Mood detected using `VADER` or `TextBlob`.
   - Weather API used to change background visuals.

3. **Multilingual AI Chatbot**
   - GPT-3.5 / FLAN-T5 responds in user's chosen language.
   - Offers simple, context-aware financial guidance.

4. **Learning Modules + Gamification**
   - Users complete modules and quizzes.
   - Rewards system gives coins and badges (via decision-tree logic).

5. **Micro-Investment Strategy**
   - Logistic regression model recommends low-risk financial steps.
   - Based on quiz score + profile data (age, risk, goals).

6. **Dataset Integration**
   - 1250-entry dataset includes region, language, literacy, mobile/bank access.
   - Used for training and rule-based personalization.

---

## 💻 Tech Stack
| Area        | Tools / Frameworks                          |
|-------------|----------------------------------------------|
| Frontend    | HTML, Tailwind CSS                          |
| Backend     | Python Flask                                |
| AI/ML       | GPT-3.5 / Text t5, VADER, Decision Tree and Logistic Regression |
| Dataset     | pandas, CSV (cleaned 1250-entry dataset)     |
| APIs        | OpenAI API, WeatherAPI                      |

---

## 📊 Sample Dataset (Preview)
| User_ID | Age | Region       | Language | Bank | Mobile | Risk  | Goal               | Quiz_Score |
|---------|-----|--------------|----------|------|--------|-------|--------------------|------------|
| 001     | 28  | West Bengal  | Bengali  | Yes  | Yes    | Low   | Start Savings      | 74         |
| 002     | 34  | Maharashtra  | Marathi  | Yes  | No     | Medium| Dairy Business     | 67         |

Full dataset available in `Naari_Udaan_Complete_Clean_Dataset.csv`

---

## 📈 Project Outcomes
- Personalized learning and support for rural women
- Localized AI copilot experience
- Scalable system with NGO and SHG deployment potential
- Hackathon-ready with low-code architecture

---

## 🚀 Future Scope
- Voice-based assistant (multilingual)
- SHG & NGO-level integration
- Offline-first mobile app version
- Micro-loan & investment partner integration

---

## 🤝 Contributors
-  [Snigdha saha ] (Team leader , AI + Web)
-  [Sayantan Sahoo] (active contributor +team member in this project,(web+security handling))
-  [Soradeep Chakraborty] (active contributor +team member in this project,(web))
-  [Rup Debnath] (active contributor +team member in this project,(web))


## 📬 Contact
Have questions or want to collaborate?
Feel free to reach us at: [snigdhasaha.student@gmail.com]

---

> ✨ *Naari Udaan empowers rural women through inclusive, intelligent design.*

