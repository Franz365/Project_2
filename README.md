# Project_2

![Beer](https://github.com/Franz365/Project_2/blob/main/images/beer.gif)

## Requirements

Building a dashboard page with multiple charts that update from the same data.

## Breweries in the United States

In this project we're going to visualize the following details of breweries in the United States:

- location marker on an interactive heat map with tooltips
- breakdown [by type](https://www.openbrewerydb.org/documentation/01-listbreweries#by_type)
- breakdown [by region](https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf)

## Data extraction

We extracted the breweries data files (.csv, .json, .sql) from the [Open Brewery DB](https://github.com/openbrewerydb/openbrewerydb) on: 06/04/2021.

## Data transformation

We used Jupyter Notebook to clean up the data and make the following transformations:

- delete all entries without latitude and longitude details (cannot be visualised)
- delete all entries outside of the United States (UK and Scottland were also in the DB)
- replace all NaN with "Not Available"
- group all states into regions and divisions using the [US census grouping](https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf). We used the .csv-file from [cphalpert](https://github.com/cphalpert/census-regions/blob/master/us%20census%20bureau%20regions%20and%20divisions.csv)
- write cleaned data in CSV-file

## Data load to Heroku Postgres

We uploaded our cleaned data to a remote database on Heroku with the following steps:

- create a new app on Heroku
- connect a remote database using Heroku Postgres (free plan "hobby-dev")
- use the Database Credentials from the Heroku website and connected it to PGAdmin
- create a new table, see [schema](https://github.com/Franz365/Project_2/blob/main/data/schema.sql)
- importe the [cleaned data](https://github.com/Franz365/Project_2/blob/main/data/breweries_clean.csv) into the remote database

## Flask setup

We used Python and Flask to setup our application ([app.py](https://github.com/Franz365/Project_2/blob/main/PythonApp/app.py)). The main route will render our dashboard. The "/test" route will display the json data.
