<a name="readme-top"></a>

<!-- PROJECT TITLE / LOGO -->
<div align="center">
  <!-- Optional logo -->
  <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
    <!-- 🚀 -->
  <!-- <h3 align="center">Business Trends <br> & Market Analysis <br>in Los Angeles</h3> -->



  <h3 align="center">
    <b>Business Trends</b><br> 
    & <b>Market Analysis</b><br>
    in <b>Los Angeles</b>
  </h3>

  <p align="center">
    End-to-end analytics &amp; interactive Dash site for exploring the survival patterns of Los Angeles businesses
    <br />
    <a href="<!-- ✍️ TODO: GitHub repo link -->"><strong>Explore the repo »</strong></a>
    ·
    <a href="<!-- ✍️ TODO: issue link -->">Report Bug</a>
    ·
    <a href="<!-- ✍️ TODO: issue link -->">Request Feature</a>
  </p>
</div>

---

<details>
<summary><strong>Table of Contents</strong></summary>

1. [About the Project](#-about-the-project) 
2. [Directory Information](#-directory-information) 
3. [Initial Data Exploration](#-initial-data-exploration) 
4. [Visualization of Business Location](#-visualization-of-business-location) 
5. [Survival Analysis & Graph](#-survival-analysis--graph) 
6. [Machine Learning-Based Data Interpretation](#-machine-learning-based-data-interpretation) 
    - [LSTM Model](#-lstm-model) 
    - [Random Survival Forest Model](#-random-survival-forest-model) 
7. [Website](#-website) 

8. [Environment & Setup](#-environment--setup) 
9. [Contact](#-contact)


</details>




---

## 📑 About the Project
<!-- ✍️ TODO: 2-3 sentence elevator pitch (What/Why/Outcome). -->
Launching a small business in Los Angeles can feel like flying blind: public data on where companies succeed or fail is plentiful, but it’s scattered across open-data portals and wrapped in jargon like “NAICS” codes, making it hard for first-time owners to act on. Our project turns that raw information into clear, personalized guidance. By mining city-wide licensing records we estimate survival probabilities by industry and location (district-level coordinates), then surface the results in an interactive Dash web app. A prospective owner can explore questions such as “What’s the three-year closure risk for cafés in Koreatown versus Santa Monica?” or “How long do auto-repair shops typically survive city-wide?”—and receive data-backed recommendations before signing a lease or drafting a business plan.

In short, we bridge the gap between complex municipal datasets and everyday decision-making, giving entrepreneurs a sharper picture of where to open, what industry risks look like, and how those factors translate into real-world failure probabilities and start-up budgeting.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- ## 🔄 Pipeline Walk-through
A high-level view from raw data to published site: -->





## 📁 Directory Information

```
.
├── app_multi_page/                   # Main Dash multipage application
├── app_multi_page_styled/            # Production build w/ custom Bootstrap theme
├── app_single_page_styled/           # Lightweight single-page Dash variant
├── dataset/                          # Raw & processed data assets (tracked via Git LFS)
├── pic/                              # picture graph plot 
│
├── dataset_business_city_list.ipynb               # City info in map
├── dataset_business_naics_code.ipynb              # NAICS info for industry in map
├── dataset_business_zipcode_list.ipynb            # Zip info for map
├── dataset_la_business.ipynb                      # Initial data cleaning & feature eng.
├── dataset_la_business_EDA.ipynb                  # Exploratory data analysis
├── dataset_la_business_ml.ipynb                   # Machine learning
├── dataset_la_business_rox.ipynb                  # Ruxin original analysis
├── dataset_la_business_visualization.ipynb        # Plotly visual drafts
│
├── requirements.txt                 # Python dependencies for notebooks & app
└── README.md                        # 👉 Project overview, setup & pipeline guide

```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---
## 🔍 Initial Data Exploration


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---


## 🗺️ Visualization of Business Location

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📊 Survival Analysis & Graph

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---



## 📊 Machine Learning-Based Data Interpretation

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### 📈 LSTM Model



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### 📉 Random Survival Forest

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ⚙️ Environment & Setup

This project is built in Python 3.10, using two main components: Jupyter notebooks (`.ipynb`) for analysis and a Dash/Flask web application (`.py`) to display results. The codebase has minimal dependencies, all listed in `requirements.txt` (Dash, Plotly, pandas, Flask, gunicorn, etc.).

To get started locally, create a new virtual or conda environment and run `pip install -r requirements.txt`. This installs the exact stack required by the notebooks and the WSGI server for the web app. Running `python app.py` launches a local Dash server, enabling real-time iteration on notebooks with immediate updates to the frontend.

For website, the code runs on Google App Engine. The `app.yaml` configuration file sets the runtime to Python 3.10, uses an F2 instance class (memory usage more than 256MB, F1 doesn't work). Deploy updates with termianl command `gcloud app deploy`. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🌐 Website

[Eric's link](https://my-project-cs122-20241114.uw.r.appspot.com/)

[Ruxin's link](https://cs163b.uw.r.appspot.com/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## ℹ️ Contact

[Eric's LindedIn](https://www.linkedin.com/in/eric-zhao-data-scientist/)

[Ruxin's LinkedIn](https://www.linkedin.com/in/ruxin-xie-1a76232b3/)



<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

<!-- 
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
Boxplots and stripplots are combined to compare business lifespans by open/closed status, with a focus on Retail and Arts sectors. Open businesses generally show longer durations, but outliers—such as very short-lived businesses—highlight the variability within sectors. This step provides a granular view of business sustainability. -->
