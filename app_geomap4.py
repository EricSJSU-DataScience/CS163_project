# Import packages
from dash import Dash, html, dcc, Output, Input
import pandas as pd
import folium
from folium.plugins import MarkerCluster
import time

# ---------------------
# Step 1. Data Loading
# ---------------------
time_start = time.time()
# Load business data
file_path = 'dataset\\business_subset.csv'
df_preworked = pd.read_csv(file_path,
                           dtype={"NAICS": "Int64"})
time_end = time.time()
print(f'Data Loading completed! Time: {(time_end - time_start): .1f} second')

# ---------------------
# Compute Zip Counts for Filter Dropdown
# ---------------------
# Make sure the 5-digit zip codes are stored as strings
df_preworked['5d_zip'] = df_preworked['5d_zip'].astype(str).str.split('-').str[0].str.strip()
# Compute the counts (this dictionary maps zip code to number of records)
zip_counts = df_preworked['5d_zip'].value_counts().to_dict()
# Build dropdown options (e.g., "90012 (123)")
zip_options = [{"label": f"{zip_code} ({zip_counts[zip_code]})", "value": zip_code}
               for zip_code in sorted(zip_counts.keys())]
default_zip = "90012"

# ---------------------
# Function to Build Folium Map for a Given Zip Code
# ---------------------
def create_map(selected_zip):
    # Filter data based on the selected zip code
    df_filtered = df_preworked[df_preworked['5d_zip'] == selected_zip].copy()
    
    # Check if the 'LOCATION' column exists.
    if 'LOCATION' in df_filtered.columns:
        # Parse coordinates from the "LOCATION" column (vectorized approach)
        df_filtered['LOCATION'] = df_filtered['LOCATION'].str.strip('()')
        df_filtered[['latitude', 'longitude']] = df_filtered['LOCATION'].str.split(', ', expand=True)
        df_filtered['latitude'] = pd.to_numeric(df_filtered['latitude'], errors='coerce')
        df_filtered['longitude'] = pd.to_numeric(df_filtered['longitude'], errors='coerce')
        df_filtered = df_filtered.dropna(subset=['latitude', 'longitude'])
    else:
        pass
    
    # Set the map center (fixed for example)
    map_center = [34.05525, -118.23737]
    business_map = folium.Map(location=map_center, zoom_start=12)
    
    marker_cluster = MarkerCluster().add_to(business_map)

    # Add markers for each business in the filtered dataset
    for _, row in df_filtered.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=folium.Popup(f"{row['BUSINESS NAME']}<br>{row['STREET ADDRESS']}", max_width=250),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)
    
    return business_map._repr_html_()

# ---------------------
# Step final. Create the Dash App
# ---------------------
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Business Map Dashboard"),
    html.Div("Select a zip code to filter the displayed businesses:"),
    dcc.Dropdown(
        id="zip-dropdown",
        options=zip_options,
        value=default_zip,  # default selection is 90012
        clearable=False
    ),
    html.Hr(),
    html.Div("Map View:", style={"marginTop": 20}),
    html.Iframe(id="map", style={"width": "100%", "height": "600px", "border": "none"})
])

@app.callback(
    Output("map", "srcDoc"),
    Input("zip-dropdown", "value")
)
def update_map(selected_zip):
    # Rebuild the Folium map for the selected zip code
    return create_map(selected_zip)

if __name__ == '__main__':
    app.run(debug=True)
