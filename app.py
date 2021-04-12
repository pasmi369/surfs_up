#import Python dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import Flask dependencies
from flask import Flask, jsonify

#setup the database engine for Flask application
engine = create_engine("sqlite:///hawaii.sqlite")

#Reflects the database into classes
Base = automap_base()

#Reflect out tables
Base.prepare(engine, reflect=True)

#Create variable for each classes
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create session link from python to sqlite
session = Session(engine)

#Crete new Flask App Instance
app = Flask(__name__)

#Create Flask Routes
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Hawaii Climate Analysis API!<br />
    Available Routes:<br />
    /api/v1.0/precipitation<br />
    /api/v1.0/stations<br />
    /api/v1.0/tobs<br />
    /api/v1.0/temp/start/end<br />
    ''')
    
# Create app route for Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#Create app routes for station
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create app route for tobs
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    
#Create app route for temperature start and end
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
    

