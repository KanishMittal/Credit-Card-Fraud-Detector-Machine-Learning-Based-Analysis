# Credit Card Fraud Detector — Machine Learning Based Analysis

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## 📋 Overview

This project focuses on detecting fraudulent credit card transactions using various machine learning techniques.  
Credit card fraud detection is crucial in financial services to minimize losses and protect users. Given the highly imbalanced nature of fraud data, we apply advanced preprocessing and evaluation methods to ensure reliable model performance.

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Matplotlib & Seaborn** — Data visualization
- **Scikit-learn** — Machine learning models and evaluation
- **Imbalanced-learn** — Techniques for handling imbalanced datasets

## 📈 Machine Learning Models Applied

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- XGBoost (Extreme Gradient Boosting)

## 🔍 Dataset

We used the [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) consisting of real transactions made by European cardholders in September 2013.

- **Number of transactions:** 284,807
- **Fraudulent transactions:** 492 (≈ 0.172%)
- **Features:** 30 (anonymized using PCA techniques)

## 🧹 Data Preprocessing

- **Scaling**: StandardScaler to normalize feature values.
- **Handling Imbalance**: SMOTE (Synthetic Minority Over-sampling Technique).
- **Train-Test Split**: Dividing the dataset into 80% training and 20% testing.
- **Feature Selection**: Experimenting with feature importance for better performance.

## 🧠 Workflow

1. Data Loading and Exploration
2. Data Cleaning and Preprocessing
3. Handling Class Imbalance
4. Model Training and Evaluation
5. Model Comparison based on Precision, Recall, F1-Score, and ROC-AUC Score
6. Final Model Selection

## 📊 Evaluation Metrics

- **Accuracy**
- **Precision**
- **Recall (Sensitivity)**
- **F1-Score**
- **ROC-AUC Score**
- **Confusion Matrix**

Due to the imbalanced dataset, **Precision**, **Recall**, and **ROC-AUC** were given higher priority over simple accuracy.

## 📌 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/KanishMittal/Credit-Card-Fraud-Detector-Machine-Learning-Based-Analysis.git
   cd Credit-Card-Fraud-Detector-Machine-Learning-Based-Analysis
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main notebook:
   ```bash
   jupyter notebook
   ```

4. Execute the steps in sequence inside the notebook.

## 📂 Project Structure

```
Credit-Card-Fraud-Detector-Machine-Learning-Based-Analysis/
│
├── data/               # Dataset files (if any)
├── models/             # Trained models saved here
├── notebooks/          # Jupyter notebooks for analysis
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

## 🚀 Future Improvements

- Implement deep learning models (ANN, CNN) for further performance boosts.
- Build a real-time fraud detection API using Flask or FastAPI.
- Deploy the model as a web application for live demonstrations.

## 🤝 Contributing

Pull requests are welcome!!  
For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
