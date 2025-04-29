import dash
from dash import html, dcc
import dash_bootstrap_components as dbc


# Define the paths to local CSS and JS files
external_stylesheets = [
    "/assets/css/bootstrap.min.css",
    "/assets/css/all.min.css"
]

external_scripts = [
    "/assets/js/jquery-3.5.1.slim.min.js",
    "/assets/js/popper.min.js",
    "/assets/js/bootstrap.min.js",
    'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML',
]

# Initialize the Dash app with local resources
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)

server = app.server

nav_items = []
for page in dash.page_registry.values():
    nav_items.append(
        html.Li(
            className="nav-item",
            children=dcc.Link(
                page["name"],
                href=page["relative_path"],
                className="nav-link"
            ),
        )
    )

app.layout = html.Div([

    # # Navigation bar # Eric
    html.Nav(
        id="mainNav",
        className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top",
        children=[
            html.Div(
                className="container",
                children=[
                    html.A("Los Angeles Business", className="navbar-brand", href="/"),
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
                            className="navbar-nav ml-auto",
                            children=nav_items,
                        )
                    )
                ]
            )
        ]
    ),

    html.Div(
        id="page-content",
        style={"padding-top": "140px"},  # Adjust based on your navbar height
        children=[
            # All your page content goes here
            dash.page_container 
        ]
    ),
    
    # # Footer Section
    html.Footer(
        className="bg-black small text-center text-white-50",
        children=html.Div("SJSU CS163")
    )

])

if __name__ == "__main__":
    app.run_server(debug=True)
