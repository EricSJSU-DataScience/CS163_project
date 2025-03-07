import dash
from dash import html, dcc
import dash_bootstrap_components as dbc  # Optional if you want to use additional Bootstrap components

# Use the external resources from your example app.py
external_stylesheets = [
    "/assets/css/bootstrap.min.css",
    "/assets/css/all.min.css"
]
external_scripts = [
    "/assets/js/jquery-3.5.1.slim.min.js",
    "/assets/js/popper.min.js",
    "/assets/js/bootstrap.min.js"
]

# Initialize the Dash app with multi-page support
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    suppress_callback_exceptions=True
)
server = app.server

# Build the navigation bar based on dash.page_registry
nav_items = []
for page in dash.page_registry.values():
    nav_items.append(
        html.Li(
            dcc.Link(
                page["name"],
                href=page["relative_path"],
                className="nav-link js-scroll-trigger"
            ),
            className="nav-item"
        )
    )

# Define the overall layout using the structure from app.py
app.layout = html.Div([
    # Navigation bar
    html.Nav(
        id="mainNav",
        className="navbar navbar-expand-lg navbar-light fixed-top",
        children=[
            html.Div(
                className="container",
                children=[
                    html.A("Business Trends and Market Analysis in LA Area", className="navbar-brand", href="/"),
                    html.Button(
                        className="navbar-toggler navbar-toggler-right",
                        type="button",
                        **{
                            "data-toggle": "collapse",
                            "data-target": "#navbarResponsive",
                            "aria-controls": "navbarResponsive",
                            "aria-expanded": "false",
                            "aria-label": "Toggle navigation"
                        },
                        children=[
                            "Menu ",
                            html.I(className="fas fa-bars")
                        ]
                    ),
                    html.Div(
                        className="collapse navbar-collapse",
                        id="navbarResponsive",
                        children=html.Ul(nav_items, className="navbar-nav ml-auto")
                    )
                ]
            )
        ]
    ),

    # Header Section (Masthead)
    # html.Header(
    #     className="masthead",
    #     children=html.Div(
    #         className="container d-flex h-100 align-items-center",
    #         children=html.Div(
    #             className="mx-auto text-center",
    #             children=[
    #                 html.H1("Business Trends and Market Analysis in LA Area"),
    #                 html.H2("Data-Driven Insights and Interactive Visualizations"),
    #                 html.A("Learn More", className="btn btn-primary js-scroll-trigger", href="#about")
    #             ]
    #         )
    #     )
    # ),

    # Content container for page content (renders pages registered via Dash)
    html.Div(dash.page_container),

    # Footer Section
    html.Footer(
        className="bg-black small text-center text-white-50",
        children=html.Div("SJSU CS163")
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
