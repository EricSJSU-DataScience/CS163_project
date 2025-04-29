import dash
from dash import html
from pages.ml_analysis_lstm import lstm_component
from pages.ml_analysis_rsf import rsf_component

dash.register_page(__name__, path="/ml", name="Analysis-ML Analysis", order=5)


layout = html.Div(className="container mt-4", children=[
    html.H1("Machine Learning Analysis"),

    # # LSTM
    lstm_component,

    # html.H2("Long Short Term Memory (LSTM)"),
    # html.H4("LSTM – Model Architecture"),
    # html.Img(src="/assets/ml1.png", className="img-fluid", style={"max-width": "800px"}),
    # html.P("The LSTM model consists of stacked LSTM layers followed by dense and dropout layers, trained on sequential business number data over time."),

    # html.H4("Retail Trade – Business Number Prediction (Test)"),
    # html.Img(src="/assets/retail_accuracy_plot.png", className="img-fluid", style={"max-width": "800px"}),
    # html.P("The test results show that the LSTM model accurately tracks actual business trends from 2000 to 2024, with a high correlation between predicted and actual values."),

    # html.H4("Retail Trade – Future Forecasting"),
    # html.Img(src="/assets/retail_prediction.png", className="img-fluid", style={"max-width": "800px"}),
    # html.P("The model forecasts business numbers for 2025 to 2027, continuing the growth trend and capturing seasonal variations based on past patterns."),


    # # RSF
    rsf_component,

    # html.H2("Random Survival Forest (RSF)"),
    # html.H4("MLA – Model Parameters"),
    # html.Img(src="/assets/mla.png", className="img-fluid", style={"max-width": "800px"}),
    # html.P("The RSF model is configured with 6 trees, depth of 5, and uses 'Council District' and 'NAICS Code' to estimate survival probability of businesses over time."),

    # html.H4("MLB – Predicted Survival Curve"),
    # html.Img(src="/assets/mlb.png", className="img-fluid", style={"max-width": "800px"}),
    # html.P("For a business starting in 2026 in Council District 3 and NAICS Code 53, the survival probability declines from 50% to below 20% within 60 months."),

    # html.H4("MLC – Model Performance (C-index)"),
    # html.Img(src="/assets/mlc.png", className="img-fluid", style={"max-width": "800px"}),
    # html.P("The model achieves a Concordance Index of 0.7574, indicating strong predictive power and consistent ranking of business survival times.")
])
