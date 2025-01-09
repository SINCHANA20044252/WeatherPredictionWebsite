import requests
from django.shortcuts import render
from .models import Weather

def weather_view(request):
    api_key = 'c854342626ec43a1b05143242241812'  # Replace with your WeatherAPI key
    weather_data = None

    if request.method == 'POST':
        city = request.POST.get('city')  # Get city from the form
        if city:  # Ensure city is not empty
            url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['location']['name'],
                    'temperature': data['current']['temp_c'],
                    'condition': data['current']['condition']['text'],
                    'humidity': data['current']['humidity'],
                    'wind_speed': data['current']['wind_kph'],
                }

                # Save weather data to the database
                Weather.objects.create(
                    city=weather_data['city'],
                    temperature=weather_data['temperature'],
                    condition=weather_data['condition'],
                    humidity=weather_data['humidity'],
                    wind_speed=weather_data['wind_speed']
                )

            else:
                weather_data = {'error': 'City not found or API error'}
    
    return render(request, 'weather_app/weather.html', {'weather_data': weather_data})





