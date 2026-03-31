# 🔐 Phishing Website Detection

> Integration of Feature-Based Methods and Machine Learning for Improved Protection.

## 📌 Overview

A machine learning-based phishing website detection system that classifies URLs as **phishing (-1)**, **suspicious (0)**, or **legitimate (1)** using a comprehensive set of URL-based, domain-based, and HTML/JavaScript-based features.

Built as a B.Tech final year project at **Institute of Technical Education and Research, SOA University, Bhubaneswar** (June 2024).

---

## ✨ Features

- 🔍 **Multi-Feature Detection** — Analyses URL structure, domain attributes, and HTML/JavaScript content
- 🎯 **96.7% Accuracy** — Best model (Random Forest) achieved 96.7% accuracy on test data
- 🌲 **8 ML Algorithms Compared** — Evaluated Logistic Regression, KNN, Naive Bayes, SVM, Decision Tree, and Random Forest
- 🖥️ **Web Interface** — User-friendly frontend built with HTML, CSS, and JavaScript
- ⚙️ **Flask Backend** — Lightweight Python backend for model serving and real-time prediction
- 🔒 **Real-Time Detection** — Users can paste any URL and instantly get a phishing or legitimate verdict

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask, Python |
| ML Models | Scikit-learn, XGBoost, TensorFlow |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Notebook | Jupyter Notebook |
| Version Control | Git, GitHub |
| IDE | Visual Studio Code |

---

## 🗂️ Dataset

- ~**35,000 phishing URLs** (from PhishTank, OpenPhish)
- ~**35,000 legitimate URLs** (from Alexa Top Sites)
- **~30 features** extracted per URL across 4 categories
- Final processed dataset: **11,000 entries**
- Train/Test split: **80% / 20%**

### Feature Categories

| Category | Examples |
| --- | --- |
| URL-Based | URL length, special characters, subdomains, IP in URL, @ symbol |
| Domain-Based | WHOIS info, domain age, SSL certificate, server geolocation |
| HTML/JS-Based | External links count, presence of login forms, HTML-to-text ratio |
| Abnormal-Based | Redirects, iframe usage, suspicious keywords |

---

## 🏗️ Architecture

```
User Input (URL)
      ↓
Flask Backend
      ↓
Feature Extraction (30+ features across 4 categories)
      ↓
Trained ML Model (Random Forest)
      ↓
Prediction: Legitimate ✅ | Suspicious ⚠️ | Phishing ❌
      ↓
Result displayed to User
```

---

## 📊 Model Performance Comparison

| Rank | Model | Accuracy | Precision | Recall | F1 Score |
| --- | --- | --- | --- | --- | --- |
| 🥇 1 | Random Forest | **96.70%** | 96.73% | 96.70% | 96.69% |
| 🥈 2 | Decision Tree | 96.07% | 96.08% | 96.07% | 96.06% |
| 🥉 3 | KNN (Manhattan) | 94.80% | 94.83% | 94.80% | 94.79% |
| 4 | KNN (Euclidean) | 94.35% | 94.39% | 94.35% | 94.34% |
| 5 | SVM (RBF) | 94.08% | 94.10% | 94.08% | 94.07% |
| 6 | Logistic Regression | 91.68% | 91.70% | 91.68% | 91.67% |
| 7 | SVM (Sigmoid) | 83.27% | 83.26% | 83.27% | 83.24% |
| 8 | Naive Bayes | 61.51% | 79.07% | 61.51% | 56.59% |

> ✅ **Random Forest** was selected as the final model due to its highest accuracy and best overall performance.

---

## 📈 Key Insight

Accuracy improved consistently as dataset size increased — demonstrating that a larger, more diverse dataset leads to better model generalization.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/himanshu2904hk/Phishing_Website_Detection_project.git
cd Phishing_Website_Detection_project

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

Then open `http://localhost:5000` in your browser.

### Usage

1. Go to the homepage and click **"Get Started"**
2. Paste any URL into the input field
3. Click **"Predict"**
4. The system will instantly classify the URL as phishing ❌ or legitimate ✅
   
---

## 📜 References

Key references that informed this project:
- Jain (2020) — Content-based phishing detection using TF-IDF
- Sahingoz et al. (2019) — Machine learning with NLP for phishing detection
- Wei et al. (2020) — CNN-based URL phishing detection
- Rao (2021) — Heuristics-based TWSVM approach
- Data sources: PhishTank, OpenPhish, Alexa Top Sites, UCI ML Repository

---

## 👤 Author

**Himanshu Kumar Lenka**
[LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/himanshu2904hk)
