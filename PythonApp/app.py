import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import create_engine
from flask import Flask, jsonify
from flask import Response,json
from flask import Flask, jsonify
from flask import Flask, render_template

#################################################
# Database Setup
#################################################
engine = create_engine("postgres://dijotinjkotssd:db7fb60a896f20e945fe8d81cfa2b4d07537011ed1ffec0d02b3d9407bd982a6@ec2-3-214-3-162.compute-1.amazonaws.com:5432/decuhc9k7edl3j")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
results = engine.execute("select * from breweries").fetchall()

#Creating a list of Dictionaries
breweries = []
for i in results:
    breweries.append({'Coordinates':[i[16], i[15]],
                      'Name': i[1],
                      'Type': i[2],
                      'Address': {
                          'Street': i[3],
                          'City': i[6],
                          'State': i[7],
                          'Post Code': i[9]
                      },
                      'Phone:': i[11],
                      'Url:': i[10],
                      'Country': i[14],
                      'Region:': i[21],
                      'Division': i[22]
                    })

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
df = pd.DataFrame(results)
columns = engine.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'breweries'").fetchall()
new_columns = []
for i in columns:
    new_columns.append(i[0])
df.columns = new_columns

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["GET"])
def welcome():
    """List all available api routes."""
    
    return (jsonify(breweries))

@app.route("/api/count_by_region")
def count_by_region():
    count_by_region = df["region"].value_counts().to_dict()

    return jsonify(count_by_region)

if __name__ == '__main__':
    app.run(debug=True)
