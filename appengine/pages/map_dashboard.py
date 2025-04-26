import dash
from dash import html
from pages.app_geomap import map_layout


dash.register_page(__name__, path="/map", name="Map Dashboard")

layout = html.Div(
    className="container mt-4",
    children=[
        html.H1("Business Map Dashboard"),
        html.P("This interactive dashboard shows the geographic distribution of business closures across Los Angeles."),
        map_layout
    ]
)
