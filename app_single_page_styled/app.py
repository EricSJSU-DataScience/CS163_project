import dash
from dash import html
from pages.app_geomap import map_layout  # Import the map layout
from pages.app_survivalplot import survival_plot

# Define the paths to local CSS and JS files
external_stylesheets = ["/assets/css/bootstrap.min.css", "/assets/css/all.min.css"]

external_scripts = [
    "/assets/js/jquery-3.5.1.slim.min.js",
    "/assets/js/popper.min.js",
    "/assets/js/bootstrap.min.js",
]

# Initialize the Dash app with local resources
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)

server = app.server

# Define the layout
app.layout = html.Div(
    [
        # Navigation bar
        html.Nav(
            id="mainNav",
            className="navbar navbar-expand-lg navbar-light fixed-top",
            children=[
                html.Div(
                    className="container",
                    children=[
                        html.A(
                            "Los Angeles", className="navbar-brand", href="#page-top"
                        ),
                        html.Button(
                            className="navbar-toggler navbar-toggler-right",
                            type="button",
                            **{
                                "data-toggle": "collapse",
                                "data-target": "#navbarResponsive",
                                "aria-controls": "navbarResponsive",
                                "aria-expanded": "false",
                                "aria-label": "Toggle navigation",
                            },
                            children=["Menu ", html.I(className="fas fa-bars")]
                        ),
                        html.Div(
                            className="collapse navbar-collapse",
                            id="navbarResponsive",
                            children=html.Ul(
                                className="navbar-nav ml-auto",
                                children=[
                                    html.Li(
                                        className="nav-item",
                                        children=html.A(
                                            "Home",
                                            className="nav-link js-scroll-trigger",
                                            href="#page-top",
                                        ),
                                    ),
                                    html.Li(
                                        className="nav-item",
                                        children=html.A(
                                            "About",
                                            className="nav-link js-scroll-trigger",
                                            href="#about",
                                        ),
                                    ),
                                    html.Li(
                                        className="nav-item dropdown",
                                        children=[
                                            html.A(
                                                "Projects",
                                                className="nav-link dropdown-toggle",
                                                href="#",
                                                **{
                                                    "id": "projectsDropdown",
                                                    "role": "button",
                                                    "data-toggle": "dropdown",
                                                    "aria-haspopup": "true",
                                                    "aria-expanded": "false",
                                                }
                                            ),
                                            html.Div(
                                                className="dropdown-menu",
                                                **{
                                                    "aria-labelledby": "projectsDropdown"
                                                },
                                                children=[
                                                    html.A(
                                                        "Datasets",
                                                        className="dropdown-item",
                                                        href="#datasets",
                                                    ),
                                                    html.A(
                                                        "Statistics",
                                                        className="dropdown-item",
                                                        href="#statistics",
                                                    ),
                                                    html.A(
                                                        "Data Visualization",
                                                        className="dropdown-item",
                                                        href="#datavisualization",
                                                    ),
                                                    html.A(
                                                        "Preliminary Insights",
                                                        className="dropdown-item",
                                                        href="#preliminary-insights",
                                                    ),
                                                ]
                                            ),
                                        ],
                                    ),
                                    html.Li(
                                        className="nav-item",
                                        children=html.A(
                                            "Contact",
                                            className="nav-link js-scroll-trigger",
                                            href="#contact",
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                )
            ],
        ),
        # Header (Masthead) Section
        html.Header(
            id="page-top",
            className="masthead",
            children=html.Div(
                className="container d-flex h-100 align-items-center",
                children=html.Div(
                    className="mx-auto text-center",
                    children=[
                        html.H1("Business Trends and Market Analysis"),
                        html.H2(
                            "Get professional data analysis for your new business",
                            className="text-white-50 mx-auto mt-2 mb-5",
                        ),
                        html.A(
                            "Get Started",
                            className="btn btn-primary js-scroll-trigger",
                            href="#about",
                        ),
                    ],
                ),
            ),
        ),
        # About Section (Updated with Broader Impacts)
        html.Section(
            id="about",
            className="about-section text-center",
            children=html.Div(
                className="container",
                children=html.Div(
                    className="row",
                    children=html.Div(
                        className="col-lg-8 mx-auto",
                        children=[
                            html.H2("Project Summary", style={"color": "white"}),
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
                                className="lead",
                                style={"color": "#f5f5fc"},
                            ),
                            # Broader Impacts Section
                            html.H2("Broader Impacts", style={"color": "white"}),
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
                                className="lead",
                                style={"color": "#f5f5fc"},
                            ),
                        ],
                    ),
                ),
            ),
        ),
        # Projects Section - Datasets
        html.Section(
            id="datasets",
            className="section",
            children=[
                html.Div(
                    className="container",
                    children=[
                        html.H1("Datasets-Summarize the dataset"),
                        html.P(
                            [
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
                                html.Strong(
                                    "LOCATION (Location – Latitude & Longitude)"
                                ),
                                ", providing geographic coordinates to visualize and analyze spatial trends in closures. These features enable a comprehensive examination of business closures over time, across industries, and by geographic location, offering insights into how different sectors and regions have been affected.",
                            ]
                        ),
                        # Handling Missing Data Section
                        html.H3("Handling Missing Data"),
                        html.P(
                            [
                                "Dropped missing data on column of: ",
                                html.Strong("NAICS, LOCATION"),
                                ". ",
                                "Since the area of interest involves NAICS code and Location start date to end date, we drop the missing records, ",
                                "leaving ",
                                html.Strong("624,379 entries remaining"),
                                ". ",
                                "We may also drop the data missing records of coordinates on the Location column. ",
                                html.Strong(
                                    "584,508 entries remaining after dropping missing NAICS and LOCATION."
                                ),
                            ]
                        ),
                    ],
                )
            ],
        ),
        # Statistics Section
        html.Section(
            id="statistics",
            className="section bg-light",
            children=[
                html.Div(
                    className="container",
                    children=[
                        html.H1("Statistics"),
                        html.P(
                            [
                                "Calculate measures like mean, median, standard deviation, and correlations:"
                            ]
                        ),
                        # Business Lifespan Statistics
                        html.H3(
                            "1, Business Lifespan Statistics (Mean, Median, Standard Deviation) in LA"
                        ),
                        html.P(
                            [
                                "Business Lifespan Statistics (Mean, Median, Std Dev) show how long businesses last on average, "
                                "the typical lifespan, and how much variation exists between businesses. "
                                "The average business lifespan is 8.57 years, with a median of 5.96 years, meaning many businesses "
                                "close within 6 years. The standard deviation of 8.66 years suggests high variability—some businesses "
                                "last much longer while others fail quickly."
                            ]
                        ),
                        html.Img(
                            src="/assets/S1.png",
                            className="img-fluid",
                            style={"width": "100%", "max-width": "800px"},
                        ),  # Image added
                        # Yearly Business Closure Count & Moving Average Statistics in LA
                        html.H3(
                            "2, Yearly Business Closure Count & 3-Year Moving Average Statistics in LA"
                        ),
                        html.P(
                            [
                                "Yearly Business Closure Trends provide insights into whether business closures are increasing or decreasing, "
                                "and the 3-Year Moving Average helps smooth short-term fluctuations to highlight long-term trends. "
                                "The Yearly Business Closures graph shows spikes in closures in certain years, possibly due to economic downturns "
                                "or other external factors. The 3-Year Moving Average (blue line) reveals a smoother trend, showing overall "
                                "increases and decreases in business closures over time."
                            ]
                        ),
                        html.Img(
                            src="/assets/S2.png",
                            className="img-fluid",
                            style={"width": "100%", "max-width": "800px"},
                        ),  # Image added
                    ],
                )
            ],
        ),
        # Data Visualization Section
        html.Section(
            id="datavisualization",
            className="section",
            children=[
                html.Div(
                    className="container",
                    children=[
                        html.H1("Data Visualization"),
                        html.P(
                            "Create insightful visualizations (e.g., histograms, scatter plots, heatmaps):"
                        ),
                        # use app_geomap from pages folder
                        map_layout,
                        # Description of the histogram and business closure trends ## may not suitable to explain anything
                        # html.H3("2, Business Closure Trends Histogram"),
                        # html.P(
                        #     [
                        #         "The histogram shows that most businesses close within a short time, with a peak in closures within the first 50 months (about 4 years). "
                        #         "The distribution is right-skewed, indicating that fewer businesses survive long-term. The median business lifespan is around 72 months (6 years), "
                        #         "meaning half of the businesses close within this period. The mean lifespan is approximately 102 months (8.5 years), showing that a small number of "
                        #         "long-lasting businesses pull the average higher. The long tail suggests that while some businesses survive 300+ months (25+ years), they are rare. "
                        #         "This pattern highlights the high early failure rate and the difficulty of long-term business survival."
                        #     ]
                        # ),
                        # # Add the barchart image (D2.png)
                        # html.Img(
                        #     src="/assets/D1.png",
                        #     className="img-fluid",
                        #     style={"width": "100%", "max-width": "800px"},
                        # ),  # Image added
                        # Closed Businesses by Sector in LOS ANGELES
                        html.H3("3, Closed Businesses by Sector in LOS ANGELES"),
                        html.P(
                            [
                                "The bar chart shows that Retail Trade had the highest number of closures, with over 8,000 businesses shut down, "
                                "followed by Other Services (6,000+) and Professional, Scientific, and Technical Services (5,500+). "
                                "The total number of closed businesses in Los Angeles is 48,396."
                                "Sectors like Wholesale Trade (4,800+), Real Estate Rental (4,000+), and Manufacturing (3,800+) also faced high closures, "
                                "while Mining and Agriculture had the least. This pattern suggests that high-competition sectors, "
                                "especially those relying on consumer demand and services, struggle the most to sustain long-term operations."
                            ]
                        ),
                        html.Img(
                            src="/assets/D2.png",
                            className="img-fluid",
                            style={"width": "100%", "max-width": "800px"},
                        ),  # Image added
                        # Average Business Lifespan by Sector in LOS ANGELES
                        html.H3(
                            "4, Average Business Lifespan by Sector in LOS ANGELES"
                        ),
                        html.P(
                            [
                                "\tThe bar chart displays both the mean and median business lifespans across sectors in Los Angeles, highlighting not only the averagesurvival time but also how most businesses actually perform. "
                                "In nearly all sectors, the mean is greater than the median, indicating right-skewed distributions—a small number of long-lasting businesses pull the average upward, while most close earlier. "
                                "For example, Real Estate Rental and Leasing shows a mean lifespan over 13 years, while the median is around 10 years. "
                                "In contrast, Accommodation and Food Services hasmean of 8.5 years but a median around 7 years, reflecting quicker turnover. "
                                "These findings suggest that while some businesses enjoy long-termsuccess, the typical business closes sooner than the average implies, especially in consumer-facing or low-margin industries. "
                                "Sectors with higher capital investment and longer-term contracts, like real estate and wholesale trade, tend to support greater stability and longevity."
                            ]
                        ),
                        html.Img(
                            src="/assets/D3.png",
                            className="img-fluid",
                            style={"width": "100%", "max-width": "800px"},
                        ),  # Image added
                        # use app_survivalplot from pages folder
                        survival_plot,
                    ],
                ),
            ],
        ),
        # Preliminary Insights Section
        html.Section(
            id="preliminary-insights",
            className="section bg-light",
            children=[
                html.Div(
                    className="container",
                    children=[
                        html.H1("Preliminary Insights"),
                        html.P(
                            [
                                "This is the overall closed businesses survival rate graph, there are observable sudden drops at each 12 months on the Duration axis."
                                "This observation might be since the leasing contract could be re-signed yearly. "
                                "To compare business survival between industries, we use a log-rank test. "
                                "This test checks if two industries have the same survival pattern over time."
                            ]
                            ),
                        html.P([
                            "Hypothesis test:",
                            html.Br(),
                            "\tNull Hypothesis (H0):The survival rates of businesses in Industry A and Industry B are the same.",
                            html.Br(),
                            "\tAlternative Hypothesis (HA):The survival rates of businesses in Industry A and Industry B are different.",
                            ]),
                        html.Img(
                            src="/assets/P1.png",
                            className="img-fluid",
                            style={"width": "100%", "max-width": "800px"},
                        ),  # Image added
                    ],
                )
            ],
        ),
        # Contact Section
        html.Section(
            id="contact",
            className="contact-section bg-black",
            children=html.Div(
                className="container",
                children=html.Div(
                    className="row justify-content-center",
                    children=[
                        html.Div(
                            className="col-md-8 mb-3 mb-md-0",
                            children=html.Div(
                                className="card py-4 h-100",
                                children=html.Div(
                                    className="card-body text-center",
                                    children=[
                                        html.I(
                                            className="fas fa-map-marked-alt text-primary mb-2"
                                        ),
                                        html.H4(
                                            "E-mail Address",
                                            className="text-uppercase m-0",
                                        ),
                                        html.H6(
                                            "Ruxin Xie: ruxin.xie01@sjsu.edu",
                                            className="m-0",
                                        ),
                                        html.H6(
                                            "Eric Zhao: eric.zhao@sjsu.edu",
                                            className="m-0",
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                ),
            ),
        ),
        # Footer Section
        html.Footer(
            className="bg-black small text-center text-white-50",
            children=html.Div(className="container", children="SJSU CS163"),
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
