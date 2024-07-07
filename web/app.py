from flask import Flask, jsonify, send_from_directory, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer
import pandas as pd
import os

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

class Data(db.Model, Base):
    __tablename__ = 'data'
    id = Column(String(50), primary_key=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Read the CSV file
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'processed_train.csv')
    df = pd.read_csv(csv_path)
    
    # Prepare data for visualization
    trip_duration_data = df['trip_duration'].value_counts().sort_index()
    passenger_count_data = df['passenger_count'].value_counts().sort_index()
    
    data = {
        'trip_duration': {
            'labels': trip_duration_data.index.tolist(),
            'values': trip_duration_data.values.tolist()
        },
        'passenger_count': {
            'labels': passenger_count_data.index.tolist(),
            'values': passenger_count_data.values.tolist()
        }
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)