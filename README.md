# 🚀 AI Sales Intelligence System

An AI-powered Sales Intelligence and Business Analytics Platform built using Python, Streamlit, MySQL, Machine Learning, and Data Visualization.

This system helps businesses monitor sales, analyze performance, predict future demand, track inventory, and generate actionable business insights through an interactive dashboard.

---

# 📌 Features

## 📊 Sales Analytics
- Daily Sales Tracking
- Monthly Revenue Analysis
- Top Selling Products
- Sales Trend Visualization
- Revenue Dashboard

## 📦 Inventory Management
- Real-Time Stock Monitoring
- Low Stock Alerts
- Product Management
- Inventory Insights

## 🤖 AI Sales Forecasting
- Future Sales Prediction
- Demand Forecasting
- Trend Analysis
- Machine Learning Forecast Models

## 👥 Customer Analytics
- Customer Purchase History
- Repeat Customer Analysis
- Customer Segmentation
- Revenue Contribution Tracking

## 📈 Business Intelligence Dashboard
- KPI Monitoring
- Revenue Insights
- Product Performance Analysis
- Interactive Charts

## 🔐 Authentication System
- Admin Login
- Manager Login
- Employee Login
- Role-Based Access Control

## 📄 Reporting System
- PDF Report Generation
- Sales Reports
- Inventory Reports
- Downloadable Business Reports

---

# 🛠️ Technology Stack

### Frontend
- Streamlit

### Backend
- Python

### Database
- MySQL

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib

### Reporting
- ReportLab

---

# 📂 Project Structure

```text
AI_Sales_Intelligence/
│
├── app/
│   ├── auth/
│   ├── dashboard/
│   ├── forecasting/
│   ├── reports/
│   └── chatbot/
│
├── database/
│   ├── db.py
│   └── models.py
│
├── datasets/
│
├── screenshots/
│   ├── login.png
│   ├── dashboard.png
│   ├── forecasting.png
│   └── inventory.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Sales-Intelligence.git

cd AI-Sales-Intelligence
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

Create MySQL Database:

```sql
CREATE DATABASE sales_ai;
```

Update database credentials inside your .env file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=sales_ai
```

---

# ▶️ Run Application

```bash
streamlit run main.py
```

Application will open at:

```text
http://localhost:8501
```

---

# 📊 Dashboard Modules

### Sales Dashboard
- Revenue Tracking
- Sales Charts
- KPI Monitoring

### Inventory Dashboard
- Stock Levels
- Low Stock Alerts
- Product Analysis

### Forecast Dashboard
- Future Sales Prediction
- Demand Forecasting
- Trend Analysis

### Customer Dashboard
- Customer Insights
- Purchase Analysis
- Repeat Customer Tracking

---

# 🤖 AI Forecasting

The system uses Machine Learning techniques to analyze historical sales data and predict future demand.

Models Used:

- Linear Regression
- Random Forest Regressor
- Time Series Analysis

Benefits:

- Better Inventory Planning
- Reduced Stock-Outs
- Improved Business Decisions

# 🔒 Security Features

- Environment Variable Support
- Role-Based Authentication
- Secure Database Connection
- Password Protection
- User Access Management

---

# 🚀 Future Enhancements

- Gemini AI Integration
- OpenAI Chat Assistant
- Auto Reorder Prediction
- Automated Purchase Orders
- Email Notifications
- SMS Alerts
- Barcode Scanning
- Multi-Store Analytics
- Advanced Forecasting Models
- Cloud Deployment

---

# 🎯 Business Benefits

✔ Improved Sales Visibility

✔ Better Inventory Management

✔ Accurate Demand Forecasting

✔ Faster Decision Making

✔ Increased Operational Efficiency

✔ Data-Driven Business Insights

---

# 👨‍💻 Author

**Your Name**

LinkedIn: Your LinkedIn Profile

GitHub: https://github.com/yourusername

---

# 📜 License

This project is developed for educational, internship, and learning purposes.

---

# ⭐ If you found this project useful, please give it a star on GitHub.
