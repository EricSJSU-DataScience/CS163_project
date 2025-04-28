import dash
from dash import html

dash.register_page(__name__, path="/objective-goals-datasets", name="Objective, Goals, and Datasets")

layout = html.Div(
    className="container mt-4",
	style={
        'backgroundColor': '#fff8e7',
        'padding': '50px',
        'minHeight': '100vh'
    },

    children=[

        html.H1("Project Goals", style={'color': 'black'}),
        html.P(
            "This project aims to develop a data-driven business advisory tool to help new business "
            "owners make informed decisions about starting and sustaining their ventures. Using large-scale "
            "datasets from Los Angeles city records, it will analyze trends in active and closed businesses, "
            "applying machine learning and statistical analysis to provide actionable insights. The final "
            "product will be an interactive web-based application where users can input key business details "
            "such as industry, location, and startup size. The system will then generate personalized "
            "recommendations, including estimated startup costs (covering labor, materials, and rent), the "
            "probability of business closure over one, three, and seven years, and strategic advice for "
            "sustainability.",
            #className="lead",
            #style={'color': '#333'}
        ),

        html.H1("Broader Impacts", style={'color': 'black', 'marginTop': '40px'}),
        html.P(
            "This project will provide valuable insights for multiple stakeholders, including new business owners, "
            "investors, policymakers, city planners, and economic researchers. New business owners will benefit "
            "from actionable insights that help them make informed decisions about selecting sustainable locations "
            "and industries. Investors and policymakers can use the findings to guide investment strategies and "
            "urban development initiatives by identifying areas of economic growth and market saturation. City "
            "planners will be able to assess which regions are oversaturated or underserved, allowing for targeted "
            "economic development and infrastructure planning. Additionally, economic researchers will find value "
            "in the analysis, as it contributes to studies on business survival trends and broader economic patterns, "
            "offering a data-driven perspective on the factors influencing business success and failure.",
            #className="lead",
            #style={'color': '#333'}
        ),

        html.Hr(style={'marginTop': '50px', 'marginBottom': '40px'}),

        html.H1("Datasets - Summarize the Dataset"),

        html.P([
            "The dataset, comprising ",
            html.Strong("1,593,026 rows"),
            " and ",
            html.Strong("16 columns"),
            ", focuses on analyzing business closures and trends by leveraging key variables: ",
            html.Strong("NAICS (Number)"),
            ", which categorizes businesses by industry type to identify industries with the highest closure rates; ",
            html.Strong("LOCATION START DATE (Floating Timestamp)"),
            ", indicating when a business began operations to determine its lifespan; ",
            html.Strong("LOCATION END DATE (Floating Timestamp)"),
            ", which identifies when a business ceased operations and serves as the primary target variable for closures; and ",
            html.Strong("LOCATION (Latitude & Longitude)"),
            ", providing geographic coordinates to visualize and analyze spatial trends in closures. These features enable a comprehensive examination of business closures over time, across industries, and by location."
        ]),

        html.H3("Handling Missing Data"),
        html.P([
            "Dropped missing data on column of: ", html.Strong("NAICS, LOCATION"), ". ",
            "Since the area of interest involves NAICS code and location start to end dates, we drop missing records, ",
            "leaving ", html.Strong("624,379 entries remaining"), ". ",
            "We may also drop the data missing coordinates on the location column, around ",
            html.Strong("500k entries remaining after dropping missing NAICS and LOCATION.")
        ]),

        html.H1("Statistics", style={"marginTop": "40px"}),
        html.P("Calculate measures like mean, median, standard deviation, and correlations:"),

        html.H3("1. Business Lifespan Statistics (Mean, Median, Standard Deviation) in LA"),
        html.P([
            "Business Lifespan Statistics (Mean, Median, Std Dev) show how long businesses last on average, "
            "the typical lifespan, and how much variation exists between businesses. "
            "The average business lifespan is 8.57 years, with a median of 5.96 years, meaning many businesses "
            "close within 6 years. The standard deviation of 8.66 years suggests high variability—some businesses "
            "last much longer while others fail quickly."
        ]),
        html.Img(src="/assets/S1.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"})

      ]
)
