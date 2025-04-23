
---
dataset_la_business_EDA.ipynb
---

Overview
This notebook explores the "Listing of All Businesses" dataset from Los Angeles, focusing on business distribution, survival analysis, and industry comparisons. Key steps include data cleaning, geospatial visualization, and statistical analysis.

Descriptions
1. Dataset Loading & Basic Information
The dataset is loaded using pandas, with specific attention given to parsing date columns (LOCATION START DATE, LOCATION END DATE) and handling missing values. Records without NAICS codes or start dates are dropped to ensure data quality. This step provides an initial understanding of the dataset structure, including column types and non-null counts.

2. NAICS Industry Classification
To categorize businesses by industry, a cleaned NAICS code-to-sector mapping file is loaded. The first two digits of the NAICS codes are extracted to classify businesses into broader sectors, and sector titles are added to the dataset. This allows for high-level comparisons across industries, such as Retail Trade versus Arts and Entertainment.

3. Geospatial Visualization
Business locations are visualized on a map using parsed latitude and longitude coordinates from the LOCATION column. Invalid or unrealistic coordinates (e.g., outside LA or the US) are filtered out. The folium library is used to create an interactive map with clustered markers, though rendering challenges with large datasets necessitated switching to FastMarkerCluster for better performance.

4. Filtering by Zip Code
To focus the analysis on Los Angeles, businesses are filtered using a list of valid LA zip codes. Debugging steps ensure proper matching between the dataset's zip codes and the reference list. The resulting filtered dataset (df2) contains only businesses located within LA, improving the accuracy of subsequent geospatial and temporal analyses.

5. Temporal Analysis
The year and month of business openings are extracted from LOCATION START DATE, and business duration (in months) is calculated along with open/closed status. Histograms of business openings by year reveal trends, such as a noticeable decline during the COVID-19 pandemic, providing context for broader economic conditions.

6. Industry Distribution
Business counts are aggregated by NAICS_2_Title to compare sector distributions. Bar plots created with Seaborn and Plotly highlight dominant sectors, with Retail Trade and Arts/Entertainment selected for deeper analysis due to their economic and cultural significance. This step identifies key industries for further survival and longevity studies.

7. Survival Analysis
The Kaplan-Meier estimator is used to plot survival curves, showing the probability of businesses remaining open over time. Survival rates are compared across industries, and log-rank tests statistically validate differences between sectors. The lifelines library facilitates this analysis, revealing insights into which industries exhibit higher resilience or volatility.

8. Boxplots for Duration Analysis
Boxplots and stripplots are combined to compare business lifespans by open/closed status, with a focus on Retail and Arts sectors. Open businesses generally show longer durations, but outliers—such as very short-lived businesses—highlight the variability within sectors. This step provides a granular view of business sustainability.
