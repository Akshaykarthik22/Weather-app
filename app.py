from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index(): 
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":       
        cityName = request.form.get("cityName")  
        if cityName:
            weatherApiKey = 'b510b450cee62a320b1b1c9ea213c0ef'
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={weatherApiKey}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses
                weatherData = response.json()
            except requests.RequestException as e:
                error = 1
                weatherData = {'message': str(e)}
        else:
            error = 1    
    return render_template('index.html', data=weatherData, cityName=cityName, error=error)

if __name__ == "__main__":
    app.run(debug=False)
#run : python app.py