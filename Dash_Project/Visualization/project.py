from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
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
    ),
    
    html.Div(children=[
        html.Label("Compare CO2 outputs between countries"),
        dcc.Dropdown(countries, ["United States", "Mexico"], multi=True, id = "inputs")
    ], className = "dropdown"),
    
    dcc.Graph(
        id = "Graph2"
    )
])

@app.callback(
    Output("Graph", "figure"),
    Input("input-selection", "value"),
)

def update_figure(selection):

    figure = px.bar(data, x=data['Year'], y=data[selection],
                labels={
                    selection: "Metric Tons Per Capita"   
                }, 
                title = "{} CO2 Emissions".format(selection))   
    return figure

@app.callback(
    Output("Graph2", "figure"),
    Input("inputs", "value")
)

def figure2(selections):
    figure2 = go.Figure(data = [
    go.Bar(name = selections[0], x = data['Year'], y = data[selections[0]]),
    go.Bar(name = selections[1], x = data['Year'], y = data[selections[1]])
])    
    return figure2
    
if __name__ == "__main__":
    app.run_server(debug=True)
