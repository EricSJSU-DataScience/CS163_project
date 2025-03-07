import dash
from dash import html

# Initialize the Dash app
external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css",
    # Grayscale custom theme (if hosted or if you have a direct URL)
    # "https://your-cdn-or-github-pages/grayscale.css",
]

external_scripts = [
    "https://code.jquery.com/jquery-3.5.1.slim.min.js",
    "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js",
    "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js",
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)

# Define the layout mimicking the Grayscale structure
app.layout = html.Div([
    # Navigation bar
    html.Nav(
        id="mainNav",
        className="navbar navbar-expand-lg navbar-light fixed-top",
        children=[
            html.Div(
                className="container",
                children=[
                    html.A("Start Bootstrap", className="navbar-brand", href="#page-top"),
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
                            children=[
                                html.Li(className="nav-item", children=html.A("Home", className="nav-link js-scroll-trigger", href="#page-top")),
                                html.Li(className="nav-item", children=html.A("About", className="nav-link js-scroll-trigger", href="#about")),
                                html.Li(className="nav-item", children=html.A("Projects", className="nav-link js-scroll-trigger", href="#projects")),
                                html.Li(className="nav-item", children=html.A("Contact", className="nav-link js-scroll-trigger", href="#contact")),
                            ]
                        )
                    )
                ]
            )
        ]
    ),
    
    # Header (Masthead) Section
    html.Header(
        className="masthead",
        children=html.Div(
            className="container d-flex h-100 align-items-center",
            children=html.Div(
                className="mx-auto text-center",
                children=[
                    html.H1("Your Favorite Source of Free Bootstrap Themes", className="mx-auto my-0 text-uppercase"),
                    html.H2("Start Bootstrap can help you build better websites with free, open source, and easy to use themes.", className="text-white-50 mx-auto mt-2 mb-5"),
                    html.A("Get Started", className="btn btn-primary js-scroll-trigger", href="#about")
                ]
            )
        )
    ),
    
    # About Section
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
                        html.H2("Built with Bootstrap 4"),
                        html.P("This theme features a variety of sections and elements, all built with Bootstrap.", className="lead")
                    ]
                )
            )
        )
    ),
    
    # Projects Section
    html.Section(
        id="projects",
        className="projects-section bg-light",
        children=html.Div(
            className="container",
            children=[
                html.Div(
                    className="row align-items-center no-gutters mb-4 mb-lg-5",
                    children=[
                        html.Div(
                            className="col-xl-8 col-lg-7",
                            children=html.Img(src="/assets/img/demo-image-01.jpg", className="img-fluid mb-3 mb-lg-0", alt="Demo image")
                        ),
                        html.Div(
                            className="col-xl-4 col-lg-5",
                            children=html.Div(
                                className="featured-text text-center text-lg-left",
                                children=[
                                    html.H4("Mighty Desktop"),
                                    html.P("A great desktop application built with modern technologies.", className="text-black-50")
                                ]
                            )
                        )
                    ]
                ),
                # Additional project rows can be added here following the same structure.
            ]
        )
    ),
    
    # Contact Section
    html.Section(
        id="contact",
        className="contact-section bg-black",
        children=html.Div(
            className="container",
            children=html.Div(
                className="row",
                children=[
                    html.Div(
                        className="col-md-4 mb-3 mb-md-0",
                        children=html.Div(
                            className="card py-4 h-100",
                            children=html.Div(
                                className="card-body text-center",
                                children=[
                                    html.I(className="fas fa-map-marked-alt text-primary mb-2"),
                                    html.H4("Address", className="text-uppercase m-0"),
                                    html.H6("1234 Street Name, City, State", className="m-0")
                                ]
                            )
                        )
                    ),
                    # Additional contact columns can be added here.
                ]
            )
        )
    ),
    
    # Footer Section
    html.Footer(
        className="bg-black small text-center text-white-50",
        children=html.Div(
            className="container",
            children="SJSU CS163"
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
