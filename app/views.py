from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b2879ddd9aefda618552a32dfe71453f'  

    cities = City.objects.all() #return all the cities in the database

    

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()


    weather_data = []
   
    SET = {"",}

    
    for city in cities:
        if city in SET:
            continue
        SET.add(city) 

        response = requests.get(url.format(city))
        if response.status_code == 404:
            continue

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form' : form}


    return render(request, 'app/weather.html', context) #returns the index.html template