import dash
from dash import html, dcc
from pages.app_survivalplot import survival_plot


dash.register_page(__name__, path="/survival", name="KM Survival Curve", order=3)

layout = html.Div(
    className="container mt-4",
    children=[
        html.H1("Kaplan-Meier Survival Curve Analysis"),
        html.P(
            "This page visualizes business survival over time by industry using Kaplan-Meier survival curves."
        ),
        dcc.Markdown(
            r"""
            The Kaplan-Meier estimator formula:

            $$
            S(t)=\prod_{i:t_i\leq t}\left(1-\frac{d_i}{n_i}\right)
            $$

            Where:
            - $t_i$ = Time when at least one event occurred
            - $d_i$ = Number of events (business closures)
            - $n_i$ = Number of businesses at risk
            """,
            mathjax=True,
        ),
        survival_plot,
    ],
)
