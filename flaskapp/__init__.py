from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import pygrib
import json
import numpy
from scipy import stats
from sklearn import linear_model
from DBFun import survRegress
import psycopg2
import urlparse
from getscores import getrank


# Initialize the Flask application
def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()
# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/_sun')
def index():
    return render_template('index1.html')

@app.route('/_boot')
def bindex():
    return render_template('boottest.html')

@app.route('/_health')
def cindex():
    return render_template('indexcancerwgraph.html')

@app.route('/_Los_Angeles')
def dindex():
    return render_template('Page2.html')

# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)
@app.route('/_get_clouds')
def get_clouds():
    lat = request.args.get('lat', 0, type=int) #lat and lon will be sent as integers *100 so integer class may be used and preserve precision
    lon = request.args.get('lon', 0, type=int)
    grbs = pygrib.open('/var/www/html/clouddata/ds.sky.bin') #open the cloud data file using the pygrib data interpreter
    cloudPct = []
    for i in range(1,25):
       grb = grbs.message(i)
       lo = float(lon/100) #process lat and lon to decimal (pygrib takes negative longitudes in W hemi)
       la = float(lat/100)
       data, lats, lons = grb.data(lat1=la-0.03,lat2=la+0.03,lon1=lo-0.03,lon2=la+0.03)
       cloudPct.append(int(data.mean()))

    return json.dumps(cloudPct)

@app.route('/_get_predictions')
def get_predictions():
  colNames = request.args
  colNames = colNames.getlist('colnames[]')
  resulting = survRegress(colNames)
  resulting[1]=resulting[1].tolist()
  return json.dumps(resulting)

@app.route('/_neighb_rank')
def neighb_rank():
  colNames = request.args
  colNames = colNames.getlist('colnames[]')
  resulting = getrank(colNames)
  return json.dumps(resulting)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
