# Brainhacks of the past - geographical distribution

import json
import os

import geopandas as gpd
import pandas as pd

from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer

path = "../data"
fnames = [os.path.join(path, elem)
          for elem in sorted(os.listdir(path))
          if os.path.isfile(os.path.join(path, elem)) and
          elem.endswith(".csv")]

# Read shapefile
shapefile = "../data/ne_110m_admin_0_countries.shp"

# Read the columns of interest
geo_df = gpd.read_file(shapefile)[["ADMIN", "geometry"]]

# Rename columns for convenience
geo_df.columns = ["country", "geometry"]

# Read brainhack data
event_df = pd.read_csv(fnames[0])

# Plot event locations
# ToDo

# Plot continent event density
# ToDo

# Plot yearly country event density

# Filter data for a given year
# ToDo
# Use a timedate util to make date data digestible
year = "2017"
df_year = event_df[event_df["dates (DD/MM/YYYY)"].str.contains(
    year, na=False, regex=False)]

# Create a new dataframe with the country event count
df_country = pd.DataFrame(
    data=df_year.groupby("country").size().rename("event_count"))

# Merge geographical and event dataframes and account for missing values
df = geo_df.merge(
    df_country, left_on="country", right_on="country", how="left")

# Bokeh consumes GeoJSON format which represents geographical features with
# JSON
features_dict = json.loads(df.to_json())

# Convert to string-like object
features = json.dumps(features_dict)

# Input GeoJSON source that contains features for plotting
geosource = GeoJSONDataSource(geojson=features)

# Compute the scales max value
max_events = df_country["event_count"].max()

# Define a sequential multi-hue color palette
# ToDo
# This palette has tuples in the range [3..8]. A parameterized value or
# another palette should be used
palette = brewer["YlGnBu"][3]

# Reverse color order so that dark blue is highest value in scale
palette = palette[::-1]

# Instantiate LinearColorMapper that linearly maps numbers in a range into
# a sequence of colors
color_mapper = LinearColorMapper(palette=palette, low=0, high=max_events)

# Define custom tick labels for the color bar
# ToDo
# Fix the label positions
tick_labels = {}
for val in range(max_events):
    tick_labels[str(val)] = str(val)

# Create the color bar
color_bar = ColorBar(
    color_mapper=color_mapper, label_standoff=5, width=500, height=20,
    border_line_color=None, location=(0, 0), orientation="horizontal")

# color_bar = ColorBar(
#    color_mapper=color_mapper, label_standoff=5, width=500, height=20,
#    border_line_color=None, location=(0, 0), orientation="horizontal",
#    major_label_overrides=tick_labels)

title = "Brainhack events per country ({})".format(year)
p = figure(title=title, plot_height=600, plot_width=950,
           toolbar_location=None)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# Turn off axes
p.axis.visible = False

# Add patch renderer to figure
p.patches(
    "xs", "ys", source=geosource,
    fill_color={"field": "event_count", "transform": color_mapper},
    line_color="black", line_width=0.25, fill_alpha=1)

p.add_layout(color_bar, "below")

# Display figure inline in Jupyter Notebook
output_notebook()

show(p)

# Cumulated
# ToDo
# Compute the accumulated event count over years

# Plot city event density using circles as markers parameterized over
# the number of events or simply use a gradient map
# ToDo


# Plot institution event density
# ToDo