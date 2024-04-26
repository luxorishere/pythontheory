from flask import Flask, render_template
import pandas as pd
app=Flask(__name__,template_folder='templates')
car = pd.read_csv('cardata.csv')
@app.route('/')
def index ():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)