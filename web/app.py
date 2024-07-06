from flask import Flask, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Dataset Viewer!'

@app.route('/display')
def display():
    df = pd.read_csv('processed_data.csv')
    return render_template('display.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
