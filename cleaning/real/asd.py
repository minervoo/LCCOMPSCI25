import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the cleaned dataset
df = pd.read_csv("emissions_cleaned.csv")

# Identify the country column (first column in dataset)
country_col = df.columns[0]

# 1. Line Graph: Total CO2 Emissions Over Time
df_yearly = df.groupby("Year", as_index=False)["Emissions.Type.CO2"].sum()
fig_line = px.line(df_yearly, x="Year", y="Emissions.Type.CO2", title="Total CO2 Emissions Over Time")
fig_line.show()

# 2. Bar Chart: Average Emissions by Sector
sector_cols = [
    "Emissions.Sector.Power Industry", "Emissions.Sector.Buildings", 
    "Emissions.Sector.Transport", "Emissions.Sector.Other Industry", "Emissions.Sector.Other sectors"
]
df_sector = df[sector_cols].mean().reset_index()
df_sector.columns = ["Sector", "Average Emissions"]
fig_bar = px.bar(df_sector, x="Sector", y="Average Emissions", title="Average Emissions by Sector")
fig_bar.show()

# 3. Pie Chart: Proportion of Emissions by Sector
fig_pie = px.pie(df_sector, names="Sector", values="Average Emissions", title="Proportion of Emissions by Sector")
fig_pie.show()

# 4. World Map for Emissions
def plot_world_map(emission_type):
    df_map = df.groupby([country_col])[emission_type].sum().reset_index()
    fig = px.choropleth(df_map, locations=country_col, locationmode="country names",
                         color=emission_type,
                         hover_name=country_col,
                         title=f"Global {emission_type} Levels")
    fig.show()

# Show default world map for CO2 emissions
plot_world_map("Emissions.Type.CO2")
    