import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# External styles/scripts
external_stylesheets = [
    "/assets/css/bootstrap.min.css",
    "/assets/css/all.min.css"
]

external_scripts = [
    "/assets/js/jquery-3.5.1.slim.min.js",
    "/assets/js/popper.min.js",
    "/assets/js/bootstrap.min.js"
]

# Initialize app
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)

server = app.server

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
<<<<<<< HEAD
            dbc.NavItem(dcc.Link("Welcome", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Objective-Goals and Datasets", href="/objective-goals-datasets", className="nav-link")),
            dbc.NavItem(dcc.Link("Analysis-Visualization", href="/visualization", className="nav-link")),
            dbc.NavItem(dcc.Link("Analysis-Map Dashboard", href="/map", className="nav-link")),
            dbc.NavItem(dcc.Link("Analysis-KM Survival Curve", href="/survival", className="nav-link")),
            dbc.NavItem(dcc.Link("Analysis-ML Analysis", href="/ml", className="nav-link")),
	    dbc.NavItem(dcc.Link("Major Findings", href="/major-findings", className="nav-link")),
            dbc.NavItem(dcc.Link("About", href="/about", className="nav-link")),
        ],
        brand="Los Angeles Business Trends",
        color="dark",
        dark=True
=======
            html.Div(
                # className="container",
                className="container-fluid",
                children=[
                    # html.A(["Los Angeles", html.Br(), "Business"], className="navbar-brand", href="/"),
                    html.A(
                        [
                            html.Span("Los Angeles", className="d-block"),
                            html.Span("Business",    className="d-block"),
                        ], 
                        className="navbar-brand text-center", 
                        href="/",
                    ),

                    html.Div(children=[

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
                        children=html.Ul(
                            className="navbar-nav ml-3 align-items-center",
                            children=nav_items,
                        )
                    )
                    ]),
                ]
            )
        ]
>>>>>>> 2c310d5da62b3ccba5f3eafc6531d902bab51d51
    ),
    dash.page_container
])

if __name__ == "__main__":
    app.run_server(debug=True)
