from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer
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

@app.route('/api/data')
def get_data():
    data = Data.query.all()
    data_json = [{column.name: getattr(item, column.name) for column in item.__table__.columns} for item in data]
    return jsonify(data_json)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)