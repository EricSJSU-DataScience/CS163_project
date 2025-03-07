import dash
from dash import Dash, html, dcc

external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/5.0.0/css/bootstrap.min.css"
]
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)
server = app.server

def create_nav_item(page, active=False):
    class_name = "btn btn-primary mx-2 rounded-pill" if active else "btn btn-outline-primary mx-2 rounded-pill"
    return html.Li(
        dcc.Link(
            page["name"],
            href=page["relative_path"],
            className=class_name,
            style={
                #"backgroundColor": "rgba(255, 255, 255, 0.05)",
                #"color": "#ffffff",
                #"border": "2px solid rgba(255, 255, 255, 0.3)",
                "padding": "10px 20px",
                "font-weight": "bold",
                "text-decoration": "none",
            }
        ),
        className="nav-item",
        role="presentation",
        style={
                "backgroundColor": "rgba(255, 255, 255, 0.05)",
                "color": "#000000",
            }
    )

nav_items = []
for page in dash.page_registry.values():
    is_active = (page["relative_path"] == "/")
    nav_items.append(create_nav_item(page, active=is_active))

app.layout = html.Div([
    html.Div(
        style={
            "background-image": "url('/assets/la-background.jpg')", 
            "background-size": "cover",
            "background-position": "center",
            "opacity": "0.5",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "zIndex": "-1",
        }
    ),
    html.Div([
        html.H1(
            'Business Trends and Market Analysis in LA Area',
            style={
                "text-align": "center",
                "margin-top": "20px",
                "color": "#333",
            }
        ),
        html.Ul(
            nav_items,
            className="d-flex justify-content-center list-unstyled p-3",
            id="pillNav2",
            role="tablist",
            style={
                "background-color": "rgba(255, 255, 255, 0.9)",
                "border-radius": "50px",
                "margin": "20px auto",
                "max-width": "80%",
                "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)"
            }
        ),
        dash.page_container
    ], style={"position": "relative", "zIndex": "1"})
])

if __name__ == '__main__':
    app.run(debug=True)
