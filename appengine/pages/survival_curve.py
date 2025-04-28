import dash
from dash import html, dcc
from pages.app_survivalplot import survival_plot


dash.register_page(__name__, 
                   path="/survival", 
                   name="KM Survival Curve", 
                   order=4)
layout = html.Div(
    className="container mt-4",
    children=[
        html.H1("Kaplan-Meier Survival Curve Analysis"),
        html.P("This page visualizes business survival over time by industry using Kaplan-Meier survival curves."),
        
        
        # Formula as image (fallback)
        html.H3("Kaplan-Meier Estimator Formula:"),
        html.Img(
            src="https://latex.codecogs.com/svg.latex?S(t)%20%3D%20%5Cprod_%7Bi%3At_i%20%5Cleq%20t%7D%20%5Cleft(1%20-%20%5Cfrac%7Bd_i%7D%7Bn_i%7D%5Cright)",
            className="mx-auto d-block",
            style={'margin': '24px 0'},
        ),
        html.H6("Where:"),
        html.Ul([
            html.Li("tᵢ = Time when at least one event occurred"),
            html.Li("dᵢ = Number of events (business closures)"),
            html.Li("nᵢ = Number of businesses at risk"),
        ]),

        # # from app_survivalplot.py
        survival_plot,
    ],
)
