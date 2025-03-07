import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)
server = app.server

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
    html.H1('Business Trends and Market Analysis in LA Area'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)