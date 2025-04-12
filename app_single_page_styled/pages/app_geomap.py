import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
import time

# ---------------------
# Step 1. Data Loading
# ---------------------
time_start = time.time()
url = 'https://raw.githubusercontent.com/EricSJSU-DataScience/CS163_project/refs/heads/main/dataset/business_subset.csv'
df_preworked = pd.read_csv(url, dtype={"NAICS": "Int64"})
time_end = time.time()
print(f'Data Loading completed! Time: {(time_end - time_start): .1f} second')

# ---------------------
# Compute Zip Counts for Filter Dropdown
# ---------------------
st = time.time()
df_preworked['5d_zip'] = df_preworked['5d_zip'].astype(str).str.split('-').str[0].str.strip()
zip_counts = df_preworked['5d_zip'].value_counts().to_dict()
zip_options = [{"label": f"{zip_code} ({zip_counts[zip_code]})", "value": zip_code}
               for zip_code in sorted(zip_counts.keys())]
default_zips = ["90001", "90002", "90003", "90004", "90005"]
et = time.time()
print(f'Zip code processing: {et - st: 0.1f} seconds')

# ---------------------
# dictionary of NAICS 2-digits information
# ---------------------
code_sector_dict = {11: 'Agriculture, Forestry, Fishing and Hunting',
                    21: 'Mining',
                    22: 'Utilities',
                    23: 'Construction',
                    31: 'Manufacturing',
                    32: 'Manufacturing',
                    33: 'Manufacturing',
                    42: 'Wholesale Trade',
                    44: 'Retail Trade',
                    45: 'Retail Trade',
                    48: 'Transportation and Warehousing',
                    49: 'Transportation and Warehousing',
                    51: 'Information',
                    52: 'Finance and Insurance',
                    53: 'Real Estate Rental and Leasing',
                    54: 'Professional, Scientific, and Technical Services',
                    55: 'Management of Companies and Enterprises',
                    56: 'Administrative and Support and Waste… Services',
                    61: 'Educational Services',
                    62: 'Health Care and Social Assistance',
                    71: 'Arts, Entertainment, and Recreation',
                    72: 'Accommodation and Food Services',
                    81: 'Other Services (except Public Administration)',
                    92: 'Public Administration'}

# ---------------------
# Compute Zip Counts for Filter Dropdown
# ---------------------
naics_counts = df_preworked['NAICS-2'].value_counts().to_dict()
naics_options = [{"label": f"{code} - {code_sector_dict.get(code, 'Unknown')} ({naics_counts.get(code, 0)})", "value": code}
                  for code in sorted(naics_counts.keys())]
default_sectors = sorted(naics_options.keys())

# ---------------------
# Function to Build Folium Map for a Given Zip Code
# ---------------------
# def create_map(selected_zip):
#     st = time.time()
#     df_filtered = df_preworked[df_preworked['5d_zip'].isin(selected_zip)].copy()
#     map_center = [34.05525, -118.23737]
#     business_map = folium.Map(location=map_center, zoom_start=10)
#     points = df_filtered[['latitude', 'longitude']].values.tolist()
#     FastMarkerCluster(points).add_to(business_map)
#     et = time.time()
#     print(f'Function create_map: {(et - st): 0.1f} seconds')
#     return business_map._repr_html_()

# ---------------------
# Function to Build Folium Map for a Given NAICS Sector Code
# ---------------------
def create_map_naics(selected_sector):
    st = time.time()
    # Filter businesses based on the selected NAICS-2 sector codes
    df_filtered = df_preworked[df_preworked['NAICS-2'].isin(selected_sector)].copy()
    map_center = [34.05525, -118.23737]
    business_map = folium.Map(location=map_center, zoom_start=10)
    points = df_filtered[['latitude', 'longitude']].values.tolist()
    FastMarkerCluster(points).add_to(business_map)
    et = time.time()
    print(f'Function create_map: {(et - st): 0.1f} seconds')
    return business_map._repr_html_()

# ---------------------
# Define the layout for the map component
# ---------------------
# def get_map_component():
#     return html.Div([
#         html.H3("1, Business Map Dashboard"),
#         html.Div("Select a zip code to filter the displayed businesses:"),
#         dcc.Dropdown(
#             id="zip-dropdown",
#             options=zip_options,
#             value=default_zips,
#             multi=True,
#             placeholder="Select zip codes...",
#             clearable=False
#         ),
#         html.Hr(),
#         html.Div("Map View:", style={"marginTop": 20}),
#         html.Iframe(id="map", style={"width": "100%", "height": "600px", "border": "none"})
#     ])
def get_map_component():
    return html.Div([
        html.H3("1, Business Map Dashboard"),
        html.Div("Select a NAICS Sector to filter the displayed businesses:"),
        dcc.Dropdown(
            id="sector-dropdown",
            options=naics_options,
            value=default_sectors,
            multi=True,
            placeholder="Select NAICS sectors...",
            clearable=False
        ),
        html.Hr(),
        html.Div("Map View:", style={"marginTop": 20}),
        html.Iframe(id="map", style={"width": "100%", "height": "600px", "border": "none"})
    ])
# ---------------------
# Callback to update the map based on selected zip code
# ---------------------
# @callback(
#     Output("map", "srcDoc"),
#     Input("zip-dropdown", "value")
# )
# def update_map(selected_zip):
#     return create_map(selected_zip)

@callback(
    Output("map", "srcDoc"),
    Input("sector-dropdown", "value")
)
def update_map(selected_sector):
    return create_map_naics(selected_sector)
# Export the layout
layout = get_map_component()