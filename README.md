# FastAPI Insurance Premium Prediction API 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.6.1-orange)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-red)
![Pandas](https://img.shields.io/badge/Pandas-2.2.2-blue)

An end-to-end Machine Learning API built with **FastAPI** and **Pydantic** to predict insurance premium categories (High/Medium/Low) based on user health and financial attributes.

## 📌 Project Overview
This project demonstrates the deployment of a Random Forest classification model. It uses a custom **Pydantic schema** with `@computed_field` to perform real-time feature engineering (BMI, Age Group, Lifestyle Risk) before passing data to the model for inference.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Framework:** FastAPI
* **Data Handling:** Pandas
* **Machine Learning:** Scikit-Learn (v1.6.1)
* **Validation:** Pydantic v2
* **Server:** Uvicorn

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/kamalsharma04/FastAPI-Insurance-Prediction.git](https://github.com/kamalsharma04/FastAPI-Insurance-Prediction.git)
cd FastAPI-Insurance-Prediction
2. Set up Virtual Environment
Bash
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Run the API
Bash
uvicorn app:app --reload
🧪 API Usage
Once the server is running, visit http://127.0.0.1:8000/docs to access the interactive Swagger UI.

Endpoint: /predict_insurance_premium
Method: POST

Input: JSON object containing age, weight, height, income_lpa, smoker, city, and occupation.

Output: Returns the predicted insurance category.

Developed by Kamal