import dash
from dash import html
from pages.ml_analysis_lstm import lstm_component
from pages.ml_analysis_rsf import rsf_component

dash.register_page(__name__, path="/ml", name="Analysis-ML Analysis", order=5)


layout = html.Div(className="container mt-4", children=[
    html.H1("Machine Learning Analysis"),

    # # LSTM
    lstm_component,

    # # RSF
    rsf_component,

])
