from flask import Flask, render_template, jsonify
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# load dataset
df = pd.read_csv("emissions_cleaned.csv")

# identify the country column which is the first column
country_col = df.columns[0]


# emissions line graph
@app.route('/generateGraphEmissionsOverTime')
def generate_graph_emissions():
    df_yearly = df.groupby("Year", as_index=False)[["Emissions.Type.CO2", "Emissions.Type.N2O", "Emissions.Type.CH4"]].sum()

    fig_line = px.line(df_yearly, x="Year", 
                   y=["Emissions.Type.CO2", "Emissions.Type.N2O", "Emissions.Type.CH4"], 
                   title="Total Emissions Over Time",
                   labels={"value": "Emissions", "variable": "Gas Type"},
                   markers=True)  # Adds dots to the lines

    fig_line.update_layout(legend_title_text="Gas Type")  # Adds legend title

    return jsonify(graphResult=fig_line.to_html(full_html=False))


# avg emissions by sector bar chart
@app.route('/generateGraphAverageEmissionsBySector')
def generate_graph_sector_emissions():
    sector_cols = [
        "Emissions.Sector.Power Industry", "Emissions.Sector.Buildings", 
        "Emissions.Sector.Transport", "Emissions.Sector.Other Industry", "Emissions.Sector.Other sectors"
    ]
    df_sector = df[sector_cols].mean().reset_index()
    df_sector.columns = ["Sector", "Average Emissions"]
    fig_bar = px.bar(df_sector, x="Sector", y="Average Emissions", title="Average Emissions by Sector")
    
    return jsonify(graphResult=fig_bar.to_html(full_html=False))

# sector proportion of emissions pie chart
@app.route('/generateGraphEmissionsBySectorPie')
def generate_graph_emissions_pie():
    sector_cols = [
        "Emissions.Sector.Power Industry", "Emissions.Sector.Buildings", 
        "Emissions.Sector.Transport", "Emissions.Sector.Other Industry", "Emissions.Sector.Other sectors"
    ]
    df_sector = df[sector_cols].mean().reset_index()
    df_sector.columns = ["Sector", "Average Emissions"]
    fig_pie = px.pie(df_sector, names="Sector", values="Average Emissions", title="Proportion of Emissions by Sector")
    
    return jsonify(graphResult=fig_pie.to_html(full_html=False))

# co2 emissions world map
@app.route('/generateWorldMapCO2')
def generate_world_map_co2():
    df_map = df.groupby([country_col])["Emissions.Type.CO2"].sum().reset_index()
    fig_map = px.choropleth(df_map, 
                            locations=country_col, 
                            locationmode="country names",
                            color="Emissions.Type.CO2",
                            hover_name=country_col,
                            color_continuous_scale="RdYlGn_r",
                            title="Global CO2 Emissions")

    return jsonify(graphResult=fig_map.to_html(full_html=False))

# routes for mean median and mode
@app.route('/mean')
def mean():
    mean_CO2 = df['Emissions.Type.CO2'].mean()
    return jsonify(resultMean=f'The Mean CO2 Emissions is: {round(mean_CO2, 2)}')

@app.route('/median')
def median():
    median_CO2 = df['Emissions.Type.CO2'].median()
    return jsonify(resultMedian=f'The Median CO2 Emissions is: {median_CO2}')

@app.route('/mode')
def mode():
    mode_CO2 = df['Emissions.Type.CO2'].mode()[0]
    return jsonify(resultMode=f'The Mode CO2 Emissions is: {mode_CO2}')

# route to render index html page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    print("Server started")
    app.run(debug=True, port=5002)