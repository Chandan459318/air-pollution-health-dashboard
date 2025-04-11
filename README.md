# 🌍 Air Pollution & Health Dashboard (2021)

This interactive dashboard visualizes air pollution levels and their impact on global health outcomes in 2021. Built using **Plotly**, **HTML**, and **Flask**, it offers rich insights into pollutant concentrations and associated respiratory issues by country.

## 📊 Dashboard Features

- **Global PM2.5 Concentration**: Bar chart of top 10 countries with the highest PM2.5 levels.
- **Pollutants Heatmap**: Comparison of air pollutant levels (e.g., CO, NO2, O3, PM10, PM2.5, SO2) across countries.
- **Health Incidence Choropleth**: World map showing respiratory illness rates.
- **Pollution Risk Distribution (Pie)**: Share of countries by pollution risk category.
- **PM2.5 vs Respiratory Death Rate**: Bubble chart showing correlation across countries.
- **CO vs NO2 Levels**: Grouped bar chart of toxic gas concentrations.
- **PM10 vs Respiratory Death Rate**: Scatter plot showing trends.
- **Average Death Rate by Pollution Risk**: Risk category vs death rate.
- **Average Illness Incidence by Risk**: Risk category vs health incidence.

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 5, Plotly.js
- **Backend**: Flask (Python)
- **Deployment**: GitHub + Render/Heroku/Localhost

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/air-pollution-health-dashboard.git
cd air-pollution-health-dashboard
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python app.py
```

Visit the dashboard at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧹 Folder Structure

```
air-pollution-health-dashboard/
│
├── static/
│   └── json/
│       ├── fig1.json
│       ├── fig2.json
│       └── ... (up to fig9.json)
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── Procfile
```

---

## 🌐 Deployment Instructions

### Deploy on Render or Heroku:

1. Create a new web service (select Python)
2. Upload the repo or connect to GitHub
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**: `gunicorn app:app`
5. Add a `Procfile` with this content:
   ```
   web: gunicorn app:app
   ```
