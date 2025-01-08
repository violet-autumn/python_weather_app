from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    ## Get the input city from the form
    city = request.args.get('city')

    ## Check if the city name is empty
    if not bool(city.strip()):
        city="Bengaluru"

    ## Run the API call
    weather_data = get_current_weather(city)

    ## Check if city name is not found
    if not weather_data["cod"] == 200:
        return render_template('city_not_found.html')
    
    ## Return results if it is
    return render_template(
        'weather.html',
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
