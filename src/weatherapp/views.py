from django.shortcuts import render,HttpResponse
import requests
import json


def weather_api(city):
    api_key = 'b548c4f65bd7d27a750421dfb3dd12aa'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&type=hour&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    results = {}
    results['City_Name'] = data['name']
    results['Country'] = data['sys']['country']
    results['Weather'] = data['weather'][0]['description']
    results['Tem'] = data['main']['temp']
    results['Humidity'] = data['main']['humidity']
    results['Sunrise'] = data['sys']['sunrise']
    results['Sunset'] = data['sys']['sunset']
    return results



def home_view(request):
    if request.method =="POST" and "city" in request.POST:
        city = request.POST.get('city')
        results = weather_api(city)
        context = {'results':results}
    else:
        context = {}
    
    return render(request, 'home.html', context)