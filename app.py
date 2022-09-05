from flask import Flask, request, json, jsonify

from pip._vendor import requests

app = Flask(__name__)


@app.route('/Bmi', methods=['POST'])
def Bmi():
    data = request.get_json()
    l= len(data)
    

    
    for i in range(0,l):
        temp= list(data[i].values())
        Height = temp[1]/100
        bmi = temp[2]/(Height**2)

        if bmi <= 18.5:

            BMICategory = "Under Weight"
            HealthRisk = "Malnutrition risk"

        elif (bmi >= 18.5 and bmi <= 24.9):

            BMICategory = "Normal weight"
            HealthRisk = "Malnutrition risk"

        elif (bmi >= 25 and bmi <= 29.9):

            BMICategory = "Overweight"
            HealthRisk = "Low risk"

        elif (bmi >= 30 and bmi <= 39.9):

            BMICategory = "Moderately obese"
            HealthRisk = "Enhanced risk"

        elif (bmi >= 40):

            BMICategory = "Severely obese"
            HealthRisk = "High risk"

        else:

            BMICategory = "Very severely obese"
            HealthRisk = "Very high risk"

        data[i]["BMI"] = bmi
        data[i]["BMICategory"] = BMICategory
        data[i]["HealthRisk"] = HealthRisk
    
    return data
    
@app.route('/unhealthy', methods=['POST'])
def Unhealthy():
    data = request.get_json()
    var= requests.post('http://127.0.0.1:5000/Bmi', json= data).json()

    l= len(var)
    total=0
    for i in range(0,l):
        temp= list(var[i].values())
        HealthRisk = temp[1]
        
        if HealthRisk == "Overweight":
            total = total+1
    return ("Total Over weight persors are " + str(total))






if __name__ == '__main__':
    app.run(debug=True)
