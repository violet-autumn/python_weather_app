
### About the App

App is live at this link: https://python-weather-i1z0.onrender.com

This is a Python based app which leverages Flask for web serving. It lets the user specify a city and then queries the Open Weather Map to fetch the current temperature, status, and feels like temerature for the specified city. 

Following is a snapshot:

<img width="600" alt="image" src="https://github.com/user-attachments/assets/0f3d2e4a-5443-4f2f-9648-62082d1af25d" /> 

***

#### Resources Used 
1. Tutorial used for reference: https://www.youtube.com/watch?v=jQjjqEjZK58
2. API used to query city weather: https://openweathermap.org/current#name
3. Web service used to host: https://dashboard.render.com/

 
*** 

#### Decription of the file tree

* templates - contains `index.html` (first webpage), `weather.html` (query successful result page), and `city_not_found.html` (query failed page). All of them contain the form to enter a new city name to query its weather.
* static/styles - contains styles.css
* requirements.txt - conatins the requirements for deplying the application
* weather.py - contains the `get_current_weather()` function defination which performs the API call to Open Weather Map and returns the resultant JSON object
* server.py - contains the flask app routing and serving logic, along with a few edge cases. It performs the end-to-end logic of the app, from fetching the city via the form input to rendering the corresponding html file based on the query result.
* .env (in local env) - contains API_KEY=<api_key_from_open_weather_map> that the `get_current_weather()` function in `weather.py` file uses to query Open Weather Map. On Render, this key is provided as a parameter while deploying the app.


*** 
