from flask import Flask, render_template

app = Flask(__name__)

titles = [
    "1. Global PM2.5 Concentration (2021)",
    "2. Air Quality Heatmap of Pollutants",
    "3. Health Incidence by Country",
    "4. Pollution Risk Distribution (Pie)",
    "5. PM2.5 vs Respiratory Death Rate",
    "6. CO and NO2 Levels by Country",
    "7. PM10 vs Respiratory Death Rate by Country",
    "8. Average Respiratory Death Rate by Pollution Risk",
    "9. Average Respiratory Illness Incidence by Pollution Risk"
]

descriptions = [
    "This bar chart displays the top 10 countries with the highest PM2.5 levels, which are fine particulate matters linked to severe respiratory issues.",
    "The heatmap compares concentration levels of major air pollutants (e.g., CO, NO2, PM10, PM2.5) across countries.",
    "A choropleth map illustrating respiratory illness incidence rates globally, providing insight into public health distribution.",
    "This pie chart shows how countries are categorized into pollution risk levels: High, Medium, Low, and Unknown.",
    "A bubble chart visualizing the relationship between PM2.5 levels and respiratory death rates across countries.",
    "A grouped bar chart comparing carbon monoxide (CO) and nitrogen dioxide (NO2) levels in selected countries.",
    "This scatter plot explores how PM10 levels correlate with respiratory death rates in different regions.",
    "This bar chart presents the average respiratory death rate grouped by each pollution risk category.",
    "This visualization displays the average incidence of illness by pollution risk grouping."
]

@app.route('/')
def index():
    return render_template('index.html', titles=titles, descriptions=descriptions)

if __name__ == '__main__':
    app.run(debug=True)
