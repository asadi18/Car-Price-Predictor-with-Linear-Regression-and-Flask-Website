from flask import Flask , render_template, request, redirect
from flask_cors import CORS , cross_origin
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
cors = CORS(app)
df = pd.read_csv('cleaned_car_dataset.csv')
model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))


@app.route('/', methods = ['GET', 'POST'])
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    year = sorted(df['year'].unique(), reverse=True)
    fuel_type = df['fuel_type'].unique()
    #companies.insert(0, 'Select Company')
    return render_template('index.html', companies=companies, car_models = car_models, years = year, fuel_type = fuel_type )
    

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    driven=request.form.get('kilo_driven')
    prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    print(prediction)    
    return str(np.round(prediction[0],2)) 


if __name__ =="__main__":
    app.run(debug=True)