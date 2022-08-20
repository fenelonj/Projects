from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

path = "Data/CO2_emission_clean.csv"
data = pd.read_csv(path)

countries = [i for i in data.columns[1:]]

app.layout = html.Div(className = "body", children = [
    html.H1(children = "Global CO2 Emissions by Country", 
           className = "header-title"),
    
    html.Div(children = """
    See how carbon emitted by the countries of the world has changed since 1990
    """, 
            className = "header-description"),
    
    html.Div(children=[
        html.Label(),
        dcc.Dropdown(countries, "United States", id = 'input-selection')
    ], className = "dropdown"),
    
    dcc.Graph(
        id = "Graph",
    )
])

@app.callback(
    Output("Graph", "figure"),
    Input("input-selection", "value"))

def update_figure(selection):

    figure = px.bar(data, x=data['Year'], y=data[selection],
                labels={
                    selection: "Metric Tons Per Capita"   
                }, 
                title = "{} CO2 Emissions".format(selection))
    
    return figure                           

if __name__ == "__main__":
    app.run_server(debug=True)
