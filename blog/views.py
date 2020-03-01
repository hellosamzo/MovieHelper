from django.shortcuts import render
from .models import Post
import requests, smtplib

def home(request):
    if request.method == 'POST':
        print(request.POST)
    # defining the api-endpoint
    serviceurl = 'http://www.omdbapi.com/?'
    omdbapi = "a37cd09d"
    apikey = '&apikey='+omdbapi
    s='The Office'
    params = "t=%27"+s+"%27"
    API_ENDPOINT = serviceurl+params+apikey
    #print(API_ENDPOINT)
    response = requests.get(API_ENDPOINT)
    result = response.json()

    return render(request, 'blog/home.html', {
        'Title': result['Title'],
        'imdbRating': result['imdbRating'],
        'imdbID': result['imdbID'],
        'Genre': result['Genre'],
        'Plot': result['Plot'],
        'Type': result['Type']   })

def about(request):
    return render(request, 'blog/about.html', {
            'test' : 'Testing123'       
            })

def cinemafinder(request):
        response = requests.get('https://ipapi.co/8.8.8.8/json/')
        geodata = response.json()
        return render(request, 'blog/cinemafinder.html', {
        'city': geodata['city'],
        'region': geodata['region'],
        'latitude': '36.778259',
        'longitude': '-119.417931',
        'api_key': ''
    })

def latest(request):
    return render(request, 'blog/latest.html', {

    })

#def spotify(request):
 #   return render(request, 'blog/')