from django.shortcuts import render,redirect,reverse
import requests
# Create your views here.
def home(request):
    url='https://api.github.com/users/johngualteros'
    response=requests.get(url)
    data=response.json()

    return render(request,'home.html',{'profile':data})

def search(request):
    url = 'https://api.github.com/users/johngualteros'
    response = requests.get(url)
    data = response.json()
    # shot the value for find the climate
    _city = request.POST['city']

    url_weather = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=3185a5e3271f50859b92ecd87272c922&units=metric".format(_city)

    response_weather = requests.get(url_weather)
    data_weather = response_weather.json()
    temperature = data_weather["main"]["temp"]
    wind_speed = data_weather["wind"]["speed"]
    longitude = data_weather["coord"]["lon"]
    latitude = data_weather["coord"]["lat"]
    description = data_weather["weather"][0]["description"]

    context={
        'city':_city,
        'temperature':temperature,
        'wind_speed':wind_speed,
        'longitude':longitude,
        'latitude':latitude,
        'description':description,
        'profile':data
    }
    return render(request,'home.html',context)