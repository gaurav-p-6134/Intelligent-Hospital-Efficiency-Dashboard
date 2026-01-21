import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 1. Load the Data
df = pd.read_csv('train_data.csv')

# 2. Data Cleaning (Handling Missing Values)
# 'Bed Grade' and 'City_Code_Patient' often have nulls in this dataset.
# We fill them with mode (most frequent value) or a placeholder.
df['Bed Grade'] = df['Bed Grade'].fillna(df['Bed Grade'].mode()[0])
df['City_Code_Patient'] = df['City_Code_Patient'].fillna(0)

# 3. Resume Requirement: "Data Modeling" - Convert 'Stay' to Numeric
# The 'Stay' column is categorical (e.g., '0-10'). We need numbers for Power BI averages.
stay_map = {
    '0-10': 5, '11-20': 15, '21-30': 25, '31-40': 35, 
    '41-50': 45, '51-60': 55, '61-70': 65, '71-80': 75, 
    '81-90': 85, '91-100': 95, 'More than 100 Days': 105
}
df['Length_of_Stay_Days'] = df['Stay'].map(stay_map)

# 4. Resume Requirement: "Admission Trends" - Generate Synthetic Dates
# The dataset has no dates. We create them to enable Time Series analysis in Power BI.
# We'll spread admissions over the year 2024.
np.random.seed(42) # Ensure reproducibility
start_date = datetime(2024, 1, 1)
total_days = 365

# Generate a random day offset for each row
random_days = np.random.randint(0, total_days, size=len(df))
df['Admission_Date'] = [start_date + timedelta(days=int(x)) for x in random_days]

# Calculate Discharge Date based on LOS
df['Discharge_Date'] = df.apply(
    lambda row: row['Admission_Date'] + timedelta(days=row['Length_of_Stay_Days']), 
    axis=1
)

# 5. Export for Power BI
# We select only the columns we need for the dashboard to keep it efficient.
cols_to_keep = [
    'case_id', 'Hospital_code', 'Hospital_type_code', 'City_Code_Hospital',
    'Hospital_region_code', 'Department', 'Ward_Type', 'Ward_Facility_Code',
    'Bed Grade', 'Type of Admission', 'Severity of Illness', 
    'Visitors with Patient', 'Age', 'Admission_Deposit', 
    'Admission_Date', 'Discharge_Date', 'Length_of_Stay_Days', 'Stay'
]

final_df = df[cols_to_keep]
final_df.to_csv('Hospital_Efficiency_Data.csv', index=False)

print("ETL Complete. 'Hospital_Efficiency_Data.csv' is ready for Power BI.")
print(f"Total records processed: {len(final_df)}")