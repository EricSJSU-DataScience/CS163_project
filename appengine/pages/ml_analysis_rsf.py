import dash
from dash import html


# ---------------------
# Define the layout for the Survival Plot component
# ---------------------
def get_rsf_detail():
    return html.Div(className="container mt-4", 
                    style={
                        'backgroundColor': 'rgba(242, 213, 25, 0.2)',
                        'padding': '20px',
                        'minHeight': '100vh'
                    },
                    children=[
                        html.H2("Random Survival Forest (RSF)"),
                        
                        html.H4("Purpose"),
                        html.P(
                            "The RSF model estimates business survival probabilities based on location and industry. "
                            "It helps entrepreneurs assess failure risks and make data-driven decisions about "
                            "where and in which sector to start a business."
                        ),
                        
                        html.H4("RSF – Model Parameters"),
                        html.Img(src="/assets/mla.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        html.P("The RSF model is configured with 6 trees, depth of 5, and uses 'Council District' and 'NAICS Code' to estimate survival probability of businesses over time."),
                        
                        html.H4("RSF – Predicted Survival Curve"),
                        html.Img(src="/assets/mlb.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        html.P("For a business starting in 2026 in Council District 3 and NAICS Code 53, the survival probability declines from 50% to below 20% within 60 months."),
                        
                        html.H4("RSF – Model Performance (C-index)"),
                        html.Img(src="/assets/mlc.png", className="img-fluid", style={"max-width": "800px", "display": "block", "margin": "auto"}),
                        html.P("The model achieves a Concordance Index of 0.7574, indicating strong predictive power and consistent ranking of business survival times."),
                    ])


# ---------------------
# Export the survival_plot
# ---------------------
rsf_component = get_rsf_detail()
