from flask import Flask, jsonify, send_from_directory
import dask.dataframe as daskDataframe
import os

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')

# Load and process data
def load_and_process_data():
    dataframe = daskDataframe.read_csv('../tests/test_data.csv')
    dataframe = dataframe.dropna()
    dataframe['mean_salary'] = dataframe['salary'].mean().compute()
    return dataframe.compute()

@app.route('/api/data')
def get_data():
    data = load_and_process_data()
    data_json = data.to_json(orient='records')
    return jsonify(data_json)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
