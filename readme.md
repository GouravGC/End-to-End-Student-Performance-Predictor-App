# 🎓 Student Performance Predictor - End-to-End Machine Learning Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-black)
![Deployment](https://img.shields.io/badge/Deployment-Render-green)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange)

An end-to-end Machine Learning application that predicts a student's **Mathematics Score** based on demographic, academic, and behavioral factors.

This project demonstrates the complete Machine Learning lifecycle:

**Data Collection → Data Preprocessing → Feature Engineering → Model Training → Model Evaluation → Pipeline Creation → Flask API Integration → Cloud Deployment**

---

# 🚀 Live Demo

The application is deployed on Render:

🔗 **Student Performance Predictor App:**  
https://end-to-end-student-performance-predictor-t4pc.onrender.com/

Users can enter student information and receive a real-time prediction of the expected Mathematics Score.

---

# 📌 Project Overview

Student academic performance depends on multiple factors such as:

- Parental education level
- Lunch type
- Test preparation status
- Reading performance
- Writing performance
- Demographic information

This project builds a Machine Learning regression model that learns patterns from historical student data and predicts the expected Mathematics Score.

The trained model is integrated with a Flask web application and deployed on the cloud for real-time predictions.

---

# 🎯 Problem Statement

Build a regression-based Machine Learning system capable of predicting a student's Mathematics Score using academic and demographic features.

---

# ✨ Key Features

✅ Complete end-to-end ML pipeline  
✅ Automated data preprocessing workflow  
✅ Feature engineering pipeline  
✅ Multiple regression model experimentation  
✅ Best model selection  
✅ Flask-based prediction web application  
✅ Real-time prediction interface  
✅ Cloud deployment using Render  
✅ Production-style project structure  

---

# 📊 Dataset Information

The project uses the **Student Performance Dataset** containing information about students' academic background and exam performance.

## Input Features

| Feature | Description |
|---|---|
| Gender | Student gender |
| Race/Ethnicity | Student demographic group |
| Parental Level of Education | Parent education qualification |
| Lunch | Standard or free/reduced lunch |
| Test Preparation Course | Completion status of preparation course |
| Reading Score | Reading exam score |
| Writing Score | Writing exam score |

## Target Variable

🎯 **Mathematics Score**

The model predicts the expected Mathematics Score out of 100.

---

# 🏗️ Project Architecture

```
Student Performance Predictor
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessing.pkl
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   └── pipeline/
│       └── prediction_pipeline.py
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 🔄 Machine Learning Workflow

## 1. Data Ingestion

- Load raw dataset
- Perform train-test split
- Prepare data for processing

---

## 2. Data Transformation

Data preprocessing pipeline includes:

- Missing value handling
- Categorical feature encoding
- Numerical feature scaling
- Feature transformation

Techniques used:

- SimpleImputer
- OneHotEncoder
- StandardScaler
- ColumnTransformer

---

## 3. Model Training

Multiple regression algorithms were evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

The best-performing model was selected based on evaluation metrics.

---

# 📈 Model Evaluation

The model was evaluated using:

## Mean Absolute Error (MAE)

Measures the average difference between predicted and actual scores.

## Mean Squared Error (MSE)

Measures the squared prediction error.

## Root Mean Squared Error (RMSE)

Represents prediction error in the same scale as Mathematics Score.

## R² Score

Measures how well the model explains variation in student performance.

---

# 🖥️ Flask Web Application

The Flask application provides a simple user interface.

Users provide:

- Gender
- Race/Ethnicity
- Parental Education
- Lunch Type
- Test Preparation Status
- Reading Score
- Writing Score

The application processes the input through the trained pipeline and returns the predicted Mathematics Score.

---

# 🛠️ Tech Stack

## Programming

- Python

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Web Development

- Flask
- HTML
- CSS

## Deployment

- Render

## Tools

- Git
- GitHub
- VS Code

---

# ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/student-performance-predictor.git
```

Navigate to project directory:

```bash
cd student-performance-predictor
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask application:

```bash
python app.py
```

Application will run at:

```
http://127.0.0.1:5000/
```

---

# 📸 Screenshots

Add screenshots of:

- Application homepage
- Input form
- Prediction output

Example:

```
screenshots/
│
├── home.png
└── prediction.png
```

---

# 🌐 Deployment Architecture

```
Developer
    |
    ↓
GitHub Repository
    |
    ↓
Render Cloud Platform
    |
    ↓
Flask Application
    |
    ↓
Machine Learning Pipeline
    |
    ↓
Real-Time Prediction
```

---

# 📁 Model Artifacts

Trained ML objects are stored as:

```
artifacts/

├── model.pkl
└── preprocessing.pkl
```

These artifacts are loaded by the prediction pipeline during application execution.

---

# 🔮 Future Improvements

Future enhancements:

- Improve frontend UI
- Add prediction confidence estimation
- Add model monitoring using MLflow
- Add Docker containerization
- Add CI/CD pipeline
- Add cloud-based model tracking
- Build interactive analytics dashboard

---

# 👨‍💻 Author

**Your Name**

Machine Learning Engineer | Data Science Enthusiast | AI Developer

GitHub:
https://github.com/yourusername

LinkedIn:
https://linkedin.com/in/yourprofile

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
