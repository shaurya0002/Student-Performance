# 🎓 Student Performance Prediction System

## 📌 Project Overview

The Student Performance Prediction System is a Machine Learning-based web application that predicts whether a student's academic performance will be **High (H)**, **Medium (M)**, or **Low (L)** based on demographic, academic, and behavioral factors.

This project was developed as part of an **AI/ML Summer Training Capstone Project** and demonstrates the complete Machine Learning lifecycle, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment.

---

## 🚀 Live Demo

**Streamlit Application:**
https://aiml-project1.streamlit.app/

---

## 📂 Dataset

**Source:** Kaggle Student Performance Dataset

### Features Used

* Gender
* Nationality
* Place of Birth
* Educational Stage
* Grade Level
* Section
* Subject Topic
* Semester
* Parent Relation
* Raised Hands
* Visited Resources
* Announcements Viewed
* Discussion Participation
* Parent Survey Response
* Parent School Satisfaction
* Student Absence Days

### Target Variable

| Class | Meaning            |
| ----- | ------------------ |
| H     | High Performance   |
| M     | Medium Performance |
| L     | Low Performance    |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit
* Git & GitHub

---

## 🔍 Machine Learning Workflow

### 1. Data Understanding

* Dataset inspection
* Data types analysis
* Missing value checking

### 2. Exploratory Data Analysis (EDA)

* Class distribution analysis
* Gender distribution analysis
* Performance-based comparisons
* Correlation analysis

### 3. Feature Engineering

* Label Encoding
* Feature Selection
* Correlation Heatmap

### 4. Model Training

The following models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)

---

## 📊 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Random Forest       | 79.17%   |
| Decision Tree       | 75.00%   |
| Logistic Regression | 71.88%   |
| SVM                 | 63.54%   |
| KNN                 | 60.42%   |

### 🏆 Best Model

**Random Forest Classifier**

Accuracy: **79.17%**

---

## 📈 Key Insights

* Students with higher resource usage tend to perform better.
* Discussion participation positively impacts academic performance.
* Student absence days significantly affect performance.
* Parent involvement contributes to improved student outcomes.

---

## 🌐 Streamlit Application Features

* Interactive User Interface
* Real-Time Prediction
* Student Performance Classification
* Easy-to-Use Input Form
* Cloud Deployment

---

## 📁 Project Structure

```text
Student-Performance-Prediction-System/
│
├── Dataset/
│   └── student_performance.csv
│
├── Notebook/
│   └── student_performance.ipynb
│
├── Model/
│   └── student_performance_model.pkl
│
├── Streamlit_App/
│   ├── app.py
│   └── requirements.txt
│
├── Documentation/
│   ├── Project_Report.pdf
│   └── Presentation.pptx
│
└── README.md
```

## ▶️ How to Run Locally

### Clone Repository

```bash
git clone https://github.com/shaurya0002/Student-Performance
cd Student-Performance-Prediction-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run Streamlit_App/app.py
```

---

## 📸 Screenshots

Add the following screenshots:

1. Homepage
2. Input Form
3. High Performance Prediction
4. Medium Performance Prediction
5. Low Performance Prediction
6. Model Comparison Graph

---

## 🎯 Future Improvements

* Hyperparameter Optimization
* Deep Learning Models
* Student Analytics Dashboard
* Personalized Learning Recommendations
* Real-Time Academic Monitoring

---

## 👨‍💻 Author

**Shaurya Pandey**

AI/ML Summer Training Project

---

## 📜 License

This project is developed for educational and academic purposes.
