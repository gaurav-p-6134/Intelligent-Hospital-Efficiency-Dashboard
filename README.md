# 🏥 Healthcare Efficiency Analytics Dashboard

![Dashboard Preview]('Screenshot 2026-01-21 141914.png')

## 📌 Project Overview
This project is an end-to-end business intelligence solution designed to optimize hospital resource allocation and patient flow. By integrating **Python for ETL** and **Power BI for advanced visualization**, the dashboard provides actionable insights into Length of Stay (LOS), departmental bottlenecks, and patient admission trends.

The goal was to move beyond simple reporting and perform **Root Cause Analysis** on hospital efficiency metrics to support data-driven decision-making.

## 🛠️ Tech Stack
* **Data Processing:** Python (Pandas, NumPy)
* **Visualization:** Power BI (DAX, Decomposition Trees)
* **Data Modeling:** Star Schema Implementation
* **Statistics:** Root Cause Analysis, Trend Forecasting

## 🚀 Key Features
### 1. Advanced ETL Pipeline (Python)
* Engineered a robust preprocessing script to handle missing values and inconsistencies in a 300,000+ record dataset.
* Generated synthetic time-series data to simulate realistic admission cycles for trend analysis.
* **Code Snippet:**
    ```python
    # Synthetic Date Generation for Time-Series Analysis
    df['Admission_Date'] = [start_date + timedelta(days=int(x)) for x in np.random.randint(0, 365, size=len(df))]
    ```

### 2. Deep Dive Analytics (Power BI)
* **Root Cause Analysis:** Implemented a **Decomposition Tree** to drill down into high LOS metrics, identifying that "Extreme" severity cases in the Surgery department were the primary driver of bed shortages.
* **Dynamic KPI Monitoring:** Created complex DAX measures to track **Readmission Risk (17.81%)** and **Total Revenue ($1.55bn)** in real-time.
* **Forecasting:** Visualized seasonal admission spikes (e.g., August peak) to aid in staff capacity planning.

### 3. User Experience (UI/UX)
* Designed a **Glassmorphism-style** interface to enhance readability and visual hierarchy.
* Integrated interactive slicers and conditional formatting (Red flags for high LOS) to guide executive attention immediately to problem areas.

## 📊 Key Insights Uncovered
1.  **Surgery Department Bottleneck:** The Surgery department has the highest average Length of Stay (37+ days), significantly higher than the hospital average of 32 days.
2.  **Severity Correlation:** Patients flagged with "Extreme" severity are staying 40% longer than minor cases, suggesting a need for a specialized high-dependency ward.
3.  **Seasonal Trends:** Patient admissions peak in **August**, indicating a requirement for temporary resource scaling during Q3.

## 💡 How to Run This Project
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/gaurav-p-6134/Healthcare-Efficiency-Dashboard.git](https://github.com/gaurav-p-6134/Healthcare-Efficiency-Dashboard.git)
    ```
2.  **Run the ETL Script:**
    * Navigate to the `scripts/` folder.
    * Run `ETL.py` to generate the clean CSV dataset.
3.  **Open the Dashboard:**
    * Launch `Dashboard.pbix` in Microsoft Power BI Desktop.
    * Refresh the data source to load the latest metrics.

---
*Author: Gaurav Parkhedkar | [LinkedIn Profile](https://www.linkedin.com/in/gaurav-parkhedkar-3b7374324/)*
