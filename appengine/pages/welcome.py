# welcome.py

import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", name="Welcome")

layout = html.Div(
    style={
        'position': 'relative',
        'backgroundImage': 'url("/assets/w1.webp")',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center',
        'minHeight': '100vh',
        'padding': '50px',
        'color': 'white',
        'overflow': 'hidden'
    },
    children=[
        # Dark overlay
        html.Div(style={
            'position': 'absolute',
            'top': 0,
            'left': 0,
            'width': '100%',
            'height': '100%',
            'backgroundColor': 'rgba(0,0,0,0.7)', 
            'zIndex': 0
        }),
        
        # Content
        dbc.Container([
            html.Div([
                html.H1(
                    "Welcome to Business Survival Analysis",
                    style={'textAlign': 'center', 'fontSize': '48px', 'marginBottom': '30px'}
                ),
                html.P(
                    "Explore business trends, survival probabilities, and machine learning predictions "
                    "based on real business closure data in Los Angeles.",
                    style={'textAlign': 'center', 'fontSize': '24px', 'marginBottom': '40px'}
                ),
                html.Hr(style={'borderColor': 'white'}),

                html.Div([
                    html.H4("Our project helps entrepreneurs, investors, and policymakers by offering:", 
                            style={'marginBottom': '20px'}),
                    html.Ul([
                        html.Li("Insights into historical business trends", style={'fontSize': '20px'}),
                        html.Li("Data-driven survival rate estimations", style={'fontSize': '20px'}),
                        html.Li("Predictive tools for new businesses based on industry and location", style={'fontSize': '20px'}),
                    ], style={'listStyleType': 'circle', 'paddingLeft': '30px'})
                ], style={'maxWidth': '800px', 'margin': 'auto', 'marginTop': '40px'})
            ], style={'position': 'relative', 'zIndex': 1})  # <-- put text above overlay
        ], fluid=True)
    ]
)
