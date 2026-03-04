# 🏅 Turkey at the Olympics — Data Analysis & ML Project

> Deep-dive analysis of Turkey's Olympic performance (1896–2016) using Python, Pandas, Plotly & Machine Learning.

---

## 📌 Project Overview

This project explores **120 years of Olympic history** through the lens of Turkey's athletic performance. Using the Kaggle Athlete Events dataset (271,116 rows), the analysis covers the full data science pipeline — from raw data cleaning to an interactive Streamlit dashboard and a medal prediction model.

---

## 📁 Project Structure

```
turkey-olympics-analysis/
│
├── data/
│   └── athlete_events.csv
├── notebooks/
│   ├── 01_EDA_cleaning.ipynb
│   ├── 02_turkey_analysis.ipynb
│   ├── 03_statistical_analysis.ipynb
│   └── 04_ml_model.ipynb
├── src/
│   └── streamlit_app.py
├── visuals/
├── requirements.txt
└── README.md
```

---

## 🔍 What Was Done

### 1. EDA & Data Cleaning
- Handled missing values across Age, Height, Weight, Medal columns
- Created binary medal indicator columns (Gold, Silver, Bronze)
- Filtered dataset by country (Turkey) and season (Summer)

### 2. Turkey-Specific Analysis
- Year-by-year medal breakdown (1936–2016)
- Top sports: **Wrestling**, Weightlifting, Boxing
- Top athletes by total medal count
- Physical attribute profiling of medalists vs non-medalists

### 3. Statistical Analysis
- **T-test:** Age difference between medalists and non-medalists (p < 0.05)
- **Pearson Correlation:** Year vs total medals — positive trend detected
- **Benchmarking:** Turkey vs Greece, Iran, Bulgaria, Hungary

### 4. Machine Learning
- **Model:** Random Forest Classifier
- **Features:** Age, Height, Weight, Year, Sport, Sex
- **Target:** Medal win probability (binary)
- Handled class imbalance with `class_weight='balanced'`

### 5. Streamlit Dashboard
- KPI cards (Gold / Silver / Bronze / Total)
- Filterable bar charts by sport and year
- Treemap of medal distribution by sport

---

## 📊 Key Findings

| Finding | Detail |
|--------|--------|
| 🥇 Most successful sport | Wrestling |
| 📈 Best year | 1948 |
| 👤 Age difference | Statistically significant (p < 0.05) |
| 📉 Trend | Positive correlation between year and medals |

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| ML | Scikit-learn, SciPy |
| Dashboard | Streamlit |
| Environment | Jupyter Notebook, GitHub |

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Bkskn/turkey-olympics-analysis.git
cd turkey-olympics-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run src/streamlit_app.py
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
scipy
streamlit
jupyter
```

---

## 📄 Dataset

- **Source:** [Kaggle — 120 years of Olympic history](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- **Rows:** 271,116
- **Years:** 1896–2016

---

## 👤 Author

**Bora Keskin**  
[GitHub](https://github.com/Bkskn)

---

*This project was built as part of a data science portfolio.*
