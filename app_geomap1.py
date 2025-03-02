# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# ---------------------
# Step 1. Data Loading & Cleaning
# ---------------------

# Load business data
file_path = 'dataset\\Listing_of_All_Businesses_20250202.csv'
df = pd.read_csv(file_path,
                 dtype={"NAICS": "Int64"},
                 parse_dates=["LOCATION START DATE", "LOCATION END DATE"])
df['LOCATION END DATE'] = pd.to_datetime(df['LOCATION END DATE'], errors='coerce')

# Drop rows missing critical fields
df1 = df.dropna(subset=['NAICS', 'LOCATION START DATE']).copy()

# Load zip code data and prepare list of valid 5-digit zip codes
zip_code = pd.read_csv('dataset\\zip_code.csv')
zip_code_list = zip_code['Zip_Code'].to_list()
zip_code_list = [str(z).zfill(5) for z in zip_code_list]

# Extract 5-digit zip from the "ZIP CODE" column
df1.loc[:, '5d_zip'] = df1['ZIP CODE'].astype(str).str.split('-').str[0]

# Filter to only include records whose 5-digit zip is in the valid list
df2 = df1[df1['5d_zip'].isin(zip_code_list)]

# ---------------------
# Step 2. Parse Coordinates from the "LOCATION" Column
# ---------------------
def parse_location(location_str):
    try:
        lat, lon = location_str.strip('()').split(', ')
        return float(lat), float(lon)
    except Exception:
        return None, None

# Create separate latitude and longitude columns
df2[['latitude', 'longitude']] = df2['LOCATION'].apply(lambda x: pd.Series(parse_location(x)))
df2 = df2.dropna(subset=['latitude', 'longitude'])

# ---------------------
# Step 3. Filter Data Based on Coordinate Range
# ---------------------
latitudes_max = 34.45
latitudes_min = 33.24
longitudes_max = -116.8
longitudes_min = -118.7

df2_filtered = df2[
    (df2['latitude'] >= latitudes_min) & (df2['latitude'] <= latitudes_max) &
    (df2['longitude'] >= longitudes_min) & (df2['longitude'] <= longitudes_max)
]
df2_sample = df2_filtered.sample(n=1000)
# ---------------------
# Step 4. Build a Folium Map with Marker Clusters
# ---------------------
# Set the map center (manually set to LA Union Station Parking as an example)
map_center = [34.05525, -118.23737]
business_map = folium.Map(location=map_center, zoom_start=12)
marker_cluster = MarkerCluster().add_to(business_map)

# Add markers for each business in the filtered dataset
for _, row in df2_sample.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(f"{row['BUSINESS NAME']}<br>{row['STREET ADDRESS']}", max_width=250),
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(marker_cluster)

# Convert the Folium map to an HTML representation
map_html = business_map._repr_html_()

# ---------------------
# Step final. Create the Dash App
# ---------------------
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Business Map Dashboard"),
    html.Div("Businesses filtered by valid zip codes and within specific coordinate bounds."),
    html.Hr(),
    dash_table.DataTable(
        id='data-table',
        data=df2_sample.to_dict('records'),
        columns=[{"name": col, "id": col} for col in df2_sample.columns],
        page_size=10,
        style_table={'overflowX': 'auto'},
    ),
    html.Hr(),
    html.Div("Map View:", style={"marginTop": 20}),
    # Embed the Folium map in an IFrame using the srcDoc property.
    html.Iframe(id="map", srcDoc=map_html, style={"width": "100%", "height": "600px", "border": "none"})
])

if __name__ == '__main__':
    app.run(debug=True)
