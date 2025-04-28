import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, 
                   path="/major-findings", 
                   name="Major Findings", 
                   order=6)

layout = html.Div([
    dbc.Container([
        html.H1("Major Findings", className="text-center my-4"),

        html.H2("General Static Findings"),
        html.P("Most businesses in Los Angeles close within the first few years, with a strong peak around 4 years and a right-skewed distribution overall. A few long-lasting businesses inflate the averages, while most businesses close much earlier. Significant changes across industries, real estate and other industries show a wide distribution of survival, indicating the opportunities and risks of new enterprises."),

        html.H2("User Input Based Dynamic Findings"),

        html.H3("Insights from Map-Based Analysis"),
        html.P("New business owners can use this map to find a council district for starting business."),
        html.P("Example:"),
	html.Img(src="/assets/mj1.png", className="img-fluid my-4"),
        html.P("Findings: this is the Real Estate Rental and Leasing industry in Los Angeles, we can see most businesses located in downtown LA. Since Real Estate Rental and Leasing is more related to population, a Real Estate business located in high population area is a good choice."),
        

        html.H3("Insights from KM Survival Curve"),
        html.P("New business owners can use this curve to find a sector for starting business."),
        html.P("Example:"),
        html.Img(src="/assets/mj2.png", className="img-fluid my-4"),
        html.P("Finding: according to the datasets from the year 1980 to 2024, the survival curve of all Real Estate Rental and Leasing industry of LA (blue line) on average is 90% at 60 months, 80% at 120 months. Which will give new business owners a lifespan expectation of this business."),

        html.H3("Predictive Insights from Machine Learning Model (LSTM and RSF)"),
        html.P("New business owners can use LSTM to find a year and month for starting business."),
        html.P("Example:"),
        html.Img(src="/assets/mj3.png", className="img-fluid my-4"),
        html.P("Findings: this ML model will give new business owner advice on when to start a business. The model forecasts for business numbers form 2025 to 2027 are increasing but the slope is decreasing, which means the market in LA will tend to grow slowly during this period."),
        html.P("Then, new business owners can use RSF to input year, month, council district and sector which can be found above to get a survival rate of this business."),
        html.P("Example:"),
        html.Img(src="/assets/mj4.png", className="img-fluid my-4"),
        html.P("Since the RSF uses the datasets from the year 2000 to 2024, which is different from 1980 to 2024, due to the financial crisis (2008) and covid-19 (2020), the survival rate dropped quickly during this period, it will give some reference and advice to new business owners to start the business."),

    ], fluid=True)
])
