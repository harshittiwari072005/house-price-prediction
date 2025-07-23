# 🏠 House Price Prediction - Django Deployment Project

This is a full-stack Django web application that predicts house prices based on machine learning. It allows users to upload or use a preloaded CSV (`houseprice.csv`) to make predictions and view results in a web interface.

## 🔧 Technologies Used

- Python 3.8+
- Django – Backend Web Framework
- Pandas, NumPy, scikit-learn – For ML and data handling
- HTML/CSS + Bootstrap – For frontend UI
- SQLite3 – Default Django database

## 🤖 Machine Learning Overview

The project uses a trained machine learning model (e.g., Linear Regression or Random Forest Regressor) to predict house prices based on input features such as:

- Number of rooms
- Area (in square feet)
- Location
- Number of bathrooms
- And other relevant parameters

The model is trained using data from `houseprice.csv` and integrated within Django views for live predictions.

## 🌐 How to Deploy the Django App

Clone the repository:
git clone https://github.com/harshittiwari072005/house-price-prediction.git
cd house-price-prediction

Create a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate   (for Windows)
# source venv/bin/activate   (for macOS/Linux)

Install the dependencies:
pip install -r requirements.txt

If requirements.txt is not available, generate it using:
pip freeze > requirements.txt

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

Then open your browser and go to: http://127.0.0.1:8000/

## 🧪 How the Prediction Works

1. User uploads or inputs data
2. Django reads and processes the data using Pandas
3. A pre-trained ML model is used to make the prediction
4. Results are displayed on the frontend

## 📁 Project Folder Structure

HOUSEPRICEPREDICTION/
├── HousePricePrediction/
│   ├── housepriceprediction/        # Main Django app
│   ├── manage.py                    # Django manager
│   ├── db.sqlite3                   # SQLite database
├── houseprice.csv                   # Dataset for prediction
├── README.md                        # Project overview
└── requirements.txt                 # Python dependencies (if added)

## 🚀 Future Enhancements

- Add live model training with new input data
- Deploy on cloud platforms (Render, PythonAnywhere, Railway, etc.)
- Add file upload interface for CSV
- Add visualizations using Chart.js or Plotly
- Improve UI/UX with advanced templates
- Add user login/authentication system

## 🙌 Author

**Harshit Tiwari**  
GitHub: https://github.com/harshittiwari072005
