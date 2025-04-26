import dash
from dash import html
from pages.app_survivalplot import survival_plot


dash.register_page(__name__, path="/survival", name="KM Survival Curve")

layout = html.Div(
    className="container mt-4",
    children=[
        html.H1("Kaplan-Meier Survival Curve Analysis"),
        html.P("This page visualizes business survival over time by industry using Kaplan-Meier survival curves."),
        survival_plot
    ]
)
