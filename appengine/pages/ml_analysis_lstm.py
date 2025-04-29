import dash
from dash import html


# ---------------------
# Define the layout for the Survival Plot component
# ---------------------
def get_lstm_detail():
    return html.Div(className="container mt-4", 
                    style={
                        'backgroundColor': 'rgba(239, 163, 177, 0.5)',
                        'padding': '20px',
                        'minHeight': '100vh'
                    },
                    children=[

                        # # LSTM 
                        html.H2("Long Short Term Memory (LSTM)"),
                        html.H4("LSTM – Model Architecture"),
                        html.Img(src="/assets/ml1.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        html.P("The LSTM model consists of stacked LSTM layers followed by dense and dropout layers, trained on sequential business number data over time."),

                        html.H4("Retail Trade – Business Number Prediction (Test)"),
                        html.Img(src="/assets/retail_accuracy_plot.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        html.P("The test results show that the LSTM model accurately tracks actual business trends from 2000 to 2024, with a high correlation between predicted and actual values."),

                        html.H4("Retail Trade – Future Forecasting"),
                        html.Img(src="/assets/retail_prediction.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        html.P("The model forecasts business numbers for 2025 to 2027, continuing the growth trend and capturing seasonal variations based on past patterns."),

                        ])


# ---------------------
# Export the survival_plot
# ---------------------
lstm_component = get_lstm_detail()
