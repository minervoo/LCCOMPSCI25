import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate dates from 2000 to 2023
dates = pd.date_range(start='2000-01-01', end='2023-12-31', freq='D')

# List of countries (mix of major emitters and smaller countries)
countries = [
    'United States', 'China', 'India', 'Russia', 'Japan', 'Germany',
    'United Kingdom', 'Canada', 'Brazil', 'France', 'Australia', 'Mexico',
    'South Korea', 'Italy', 'Spain', 'Netherlands', 'Poland', 'Turkey',
    'Sweden', 'Norway', 'Denmark', 'Finland', 'New Zealand', 'Ireland'
]

# Generate the dataset
data = []
for date in dates:
    # Generate data for each country
    for country in countries:
        # Base emissions vary by country (some countries emit more than others)
        base_emission = np.random.normal(100, 30)  # Base emission level
        
        # Add seasonal variation
        seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.dayofyear / 365)
        
        # Add some random noise
        noise = np.random.normal(0, 10)
        
        # Calculate final emission
        emission = base_emission * seasonal_factor + noise
        
        # Ensure emissions are positive
        emission = max(0, emission)
        
        data.append({
            'Date': date,
            'Country': country,
            'Emissions.Type.CO2': emission,
            'Year': date.year
        })

# Create DataFrame
df = pd.DataFrame(data)

# Add some categorical variables for more interesting visualization
df['Region'] = np.random.choice(['North America', 'Europe', 'Asia', 'Oceania', 'South America'], size=len(df))
df['Development_Status'] = np.random.choice(['Developed', 'Developing', 'Emerging'], size=len(df))

# Save the dataset
df.to_csv('emissions.csv', index=False)

print(f"Generated emissions dataset with {len(df)} rows")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Number of countries: {df['Country'].nunique()}") 