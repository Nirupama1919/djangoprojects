
from django.shortcuts import render
import requests

def index(request):

    weather_data = None
    error = None

    if request.method == "POST":

        city = request.POST.get('city')

        api_key = "51705b71fcd13df1041e25029d8c1e38"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)

        data = response.json()

        if data.get("cod") == 200:

            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
                "wind": data["wind"]["speed"],
            }

        else:
            error = "City not found"

    return render(request, 'index.html', {
        'weather_data': weather_data,
        'error': error
    })