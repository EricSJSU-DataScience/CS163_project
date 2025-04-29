import dash
from dash import html


# ---------------------
# Define the layout for the Survival Plot component
# ---------------------
def alternating_layout(entries):
    children = []
    for i, (title, img_path, description) in enumerate(entries):
        is_even = i % 2 == 0
        row = html.Div(className="row align-items-center my-4", children=[
            html.Div(className="col-md-6", children=[
                html.H4(title),
                html.P(description)
            ]) if is_even else html.Div(className="col-md-6", children=[
                html.Img(src=img_path, className="img-fluid", style={"max-width": "100%"})
            ]),
            html.Div(className="col-md-6", children=[
                html.Img(src=img_path, className="img-fluid", style={"max-width": "100%"})
            ]) if is_even else html.Div(className="col-md-6", children=[
                html.H4(title),
                html.P(description)
            ])
        ])
        children.append(row)
    return children

def get_lstm_detail():
    return html.Div(className="container mt-4", 
                    style={
                        'backgroundColor': 'rgba(239, 163, 177, 0.2)',
                        'padding': '20px',
                        'minHeight': '100vh'
                    },
                    children=[

                        # # LSTM 
                        html.H2("Long Short Term Memory (LSTM)"),

                        html.H4("Purpose"),
                        html.P(
                            "Use an LSTM on historical monthly business counts to predict future retail trade numbers."
                            "By analyzing long-term trends and seasonal patterns, "
                            "this tool helps assess market capacity in Retail Trade—"
                            "predicting whether future demand will shrink or expand—"
                            "to gauge risks for new store openings."
                        ),

                        *alternating_layout([
                            ("LSTM – Model Architecture", "/assets/ml1.png", 
                            "The LSTM model consists of stacked LSTM layers followed by dense and dropout layers, trained on sequential business number data over time."),
                            ("Retail Trade – Business Number Prediction (Test)", "/assets/retail_accuracy_plot.png", 
                            "The test results show that the LSTM model approximately tracks actual business trends from 2000 to 2024, it indicates the LSTM model performs approximately well."),
                            ("Retail Trade – Future Forecasting", "/assets/retail_prediction.png", 
                            "The model forecasts business numbers for 2025 to 2027, continuing the growth trend. However, the growth rate becomes smoother, indicating slower expansion in Retail Trade and heightened competition for new store openings."),
                        ]),

                        
                        # html.H4("LSTM – Model Architecture"),
                        # html.Img(src="/assets/ml1.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        # html.P("The LSTM model consists of stacked LSTM layers followed by dense and dropout layers, trained on sequential business number data over time."),

                        # html.H4("Retail Trade – Business Number Prediction (Test)"),
                        # html.Img(src="/assets/retail_accuracy_plot.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        # html.P("The test results show that the LSTM model approximately tracks actual business trends from 2000 to 2024, it indicates the LSTM model performs approximately well."),

                        # html.H4("Retail Trade – Future Forecasting"),
                        # html.Img(src="/assets/retail_prediction.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        # html.P(
                        #     "The model forecasts business numbers for 2025 to 2027, continuing the growth trend. "
                        #     "However, the growth rate becomes smoother, indicating slower expansion in Retail Trade and heightened competition for new store openings."
                        # ),

                        ])


# ---------------------
# Export the survival_plot
# ---------------------
lstm_component = get_lstm_detail()
