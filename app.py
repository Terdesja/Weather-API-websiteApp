from flask import Flask, render_template, request
import requests

app = Flask(__name__)
if __name__ == "__main__":
    app.run()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather_url = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9bad8e2313cfb62122df582901b39148")

        weather_data = weather_url.json()

        temp = round(weather_data['main']['temp'] - 273.15)
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        min_temp = int(weather_data['main']['temp_min'] - 273.15)
        max_temp = int(weather_data['main']['temp_max'] - 273.15)
        pressure = weather_data['main']['pressure']

        return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city, min_temp=min_temp, max_temp=max_temp, pressure=pressure)

    return render_template("index.html")
