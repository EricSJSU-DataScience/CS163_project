import dash
from dash import html

dash.register_page(__name__, path="/visualization", 
                   name="Analysis-Visualization", order=2)

layout = html.Div(
    className="container mt-4",
    style={
        'backgroundColor': 'rgba(185, 225, 219, 0.5)',
        'padding': '50px',
        'minHeight': '100vh'
    },
    children=[
        html.H1("Data Visualization"),
        html.P("Create insightful visualizations (e.g., histograms, scatter plots, heatmaps):"),

        html.H3("1. Business Closure Trends Histogram"),
        html.P([
            "The histogram shows that most businesses close within a short time, with a peak in closures within the first 50 months (about 4 years). ",
            "The distribution is right-skewed, indicating that fewer businesses survive long-term. The median business lifespan is around 72 months (6 years), ",
            "meaning half of the businesses close within this period. The mean lifespan is approximately 102 months (8.5 years), showing that a small number of ",
            "long-lasting businesses pull the average higher. The long tail suggests that while some businesses survive 300+ months (25+ years), they are rare. ",
            "This pattern highlights the high early failure rate and the difficulty of long-term business survival."
        ]),
        html.Img(src="/assets/D1.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"}),

        html.H3("2. Closed Businesses by Sector in LOS ANGELES"),
        html.P([
            "The bar chart shows that Retail Trade had the highest number of closures, with over 8,000 businesses shut down, ",
            "followed by Other Services (6,000+) and Professional, Scientific, and Technical Services (5,500+). ",
            "The total number of closed businesses in Los Angeles is 48,396. ",
            "Sectors like Wholesale Trade (4,800+), Real Estate Rental (4,000+), and Manufacturing (3,800+) also faced high closures, ",
            "while Mining and Agriculture had the least. This pattern suggests that high-competition sectors, ",
            "especially those relying on consumer demand and services, struggle the most to sustain long-term operations."
        ]),
        html.Img(src="/assets/D2.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"}),

        html.H3("3. Mean vs. Median Business Lifespan by Sector (1980-2024)"),
        html.P([
            "The updated bar chart displays both the mean and median business lifespans across sectors in Los Angeles, highlighting not only the average ",
            "survival time but also how most businesses actually perform. In nearly all sectors, the mean is greater than the median, indicating right-",
            "skewed distributions—a small number of long-lasting businesses pull the average upward, while most close earlier. For example, Real Estate ",
            "Rental and Leasing shows a mean lifespan over 13 years, while the median is around 10 years. In contrast, Accommodation and Food Services has ",
            "mean of 8.5 years but a median around 7 years, reflecting quicker turnover. These findings suggest that while some businesses enjoy long-term ",
            "success, the typical business closes sooner than the average implies, especially in consumer-facing or low-margin industries. Sectors with ",
            "higher capital investment and longer-term contracts, like real estate and wholesale trade, tend to support greater stability and longevity."
        ]),
        html.Img(src="/assets/D3.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"}),

        html.H3("4. Distribution of Business Lifespan by Sector (2000-2024)", style={"marginTop": "50px"}),
        html.P([
            "Each violin represents the density and spread of how long businesses survive in a specific industry. The thicker areas show where most ",
            "businesses are clustered in terms of lifespan, while the thinner tails highlight outliers — businesses that lasted unusually short or long.",
            "This visualization gives us a more complete picture than just averages — helping us identify not only central tendencies but also the ",
            "variability and skewness within each industry."
        ]),
        html.Img(src="/assets/P1.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"}),

	html.H3("5. Net Business Change Pre Month in LA (2000-2024)", style={"marginTop": "50px"}),
        html.P([
            "Here we examined the monthly net change in businesses from 2000 to 2024. This is calculated as the number of new businesses started minus ",
	    "those that closed each month. We observe that earlier years, especially before 2010, show mostly positive or balanced net change — ",
	    "indicating a growing economy. However, We see clear patterns of drops, including major dips during the 2008 financial crisis and COVID-19.",
            "This pattern suggests seasonal business closures, possibly due to financial year-end reviews, lease expirations, or holiday-related factors. "
        ]),
        html.Img(src="/assets/dv1.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"}),

	html.H3("6. Net Change Bussiness by month (all year combined)", style={"marginTop": "50px"}),
        html.P([
            "Seasonal waves repeat annually, with peaks in JAN, and significantly reduced in DEC. This pattern highlights how macroeconomic events and ", 	    "policy shifts impact business dynamics over time."
        ]),
        html.Img(src="/assets/dv2.png", className="img-fluid", style={"width": "100%", "maxWidth": "800px"})
    ]
)
