import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster
import time

# Register this file as a Dash page.
dash.register_page(__name__, path='/geomap4', name='Business Map Dashboard')

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
# default_zip = "90012"
# default_zips = [option["value"] for option in zip_options]  # Default to all zip codes
default_zips = ["90001", "90002", "90003", "90004", "90005"]
et = time.time()
print(f'Zip code processing: {et - st: 0.1f} seconds')
# ---------------------
# Function to Build Folium Map for a Given Zip Code
# ---------------------
def create_map(selected_zip):
    st = time.time()
    df_filtered = df_preworked[df_preworked['5d_zip'].isin(selected_zip)].copy()
    
    # if 'LOCATION' in df_filtered.columns:
    #     df_filtered['LOCATION'] = df_filtered['LOCATION'].str.strip('()')
    #     df_filtered[['latitude', 'longitude']] = df_filtered['LOCATION'].str.split(', ', expand=True)
    #     df_filtered['latitude'] = pd.to_numeric(df_filtered['latitude'], errors='coerce')
    #     df_filtered['longitude'] = pd.to_numeric(df_filtered['longitude'], errors='coerce')
    #     df_filtered = df_filtered.dropna(subset=['latitude', 'longitude'])
    
    map_center = [34.05525, -118.23737]
    business_map = folium.Map(location=map_center, zoom_start=10)
    # marker_cluster = MarkerCluster().add_to(business_map)
    # for _, row in df_filtered.iterrows():
    #     folium.Marker(
    #         location=[row['latitude'], row['longitude']],
    #         popup=folium.Popup(f"{row['BUSINESS NAME']}<br>{row['STREET ADDRESS']}", max_width=250),
    #         icon=folium.Icon(color='blue', icon='info-sign')
    #     ).add_to(marker_cluster)
    points = df_filtered[['latitude', 'longitude']].values.tolist()
    FastMarkerCluster(points).add_to(business_map)
    et = time.time()
    print(f'Funtion create_map: {(et - st): 0.1f} seconds')
    return business_map._repr_html_()

# def create_map(selected_zip):
#     if selected_zip in map_cache:
#         return map_cache[selected_zip]
    
#     df_filtered = df_preworked[df_preworked['5d_zip'] == selected_zip].copy()
#     map_center = [34.05525, -118.23737]
#     business_map = folium.Map(location=map_center, zoom_start=12)
#     marker_cluster = MarkerCluster().add_to(business_map)
    
#     for _, row in df_filtered.iterrows():
#         folium.Marker(
#             location=[row['latitude'], row['longitude']],
#             popup=folium.Popup(f"{row['BUSINESS NAME']}<br>{row['STREET ADDRESS']}", max_width=250),
#             icon=folium.Icon(color='blue', icon='info-sign')
#         ).add_to(marker_cluster)
        
#     map_html = business_map._repr_html_()
#     map_cache[selected_zip] = map_html
#     return map_html

# def create_map(selected_zip):
#     df_filtered = df_preworked[df_preworked['5d_zip'] == selected_zip].copy()
#     map_center = [34.05525, -118.23737]
#     business_map = folium.Map(location=map_center, zoom_start=12)
    
#     # Prepare list of points
#     points = df_filtered[['latitude', 'longitude']].dropna().values.tolist()
#     FastMarkerCluster(points).add_to(business_map)
    
#     return business_map._repr_html_()

# ---------------------
# Define the layout for the page
# ---------------------
layout = html.Div([
    html.H1("Business Map Dashboard"),
    html.Div("Select a zip code to filter the displayed businesses:"),
    dcc.Dropdown(
        id="zip-dropdown",
        options=zip_options,
        value=default_zips,
        multi=True,
        placeholder="Select zip codes...",
        clearable=False
    ),
    html.Hr(),
    html.Div("Map View:", style={"marginTop": 20}),
    html.Iframe(id="map", style={"width": "100%", "height": "600px", "border": "none"})
])

# ---------------------
# Callback to update the map based on selected zip code
# ---------------------
@callback(
    Output("map", "srcDoc"),
    Input("zip-dropdown", "value")
)
def update_map(selected_zip):
    return create_map(selected_zip)
