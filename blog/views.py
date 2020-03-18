from django.shortcuts import render
from .models import Post
import requests, smtplib
import bs4 as bs
from urllib import request as req

def home(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)
        if search_query:
            serviceurl = 'http://www.omdbapi.com/?'
            omdbapi = "a37cd09d"
            apikey = '&apikey='+omdbapi
            s = search_query
            params = "t=%27"+s+"%27"
            API_ENDPOINT = serviceurl+params+apikey
            response = requests.get(API_ENDPOINT)
            result = response.json()
            response = result['Response']
            if response == 'True':
                return render(request, 'blog/home.html', {
                'Title': result['Title'],
                'imdbRating': result['imdbRating'],
                'imdbID': result['imdbID'],
                'Genre': result['Genre'],
                'Plot': result['Plot'],
                'Type': result['Type']   })
            elif response == 'False':
                return render(request, 'blog/home.html', {
                'Title': 'Movie Not Found!'  })
        else:
            return render(request, 'blog/home.html')

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
    url = "https://imdb.com"
    html = req.urlopen(url).read().decode('utf8')
    html[:60]
    soup = bs.BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    #print(title.string)
    return render(request, 'blog/latest.html', {

    })

#def spotify(request):
 #   return render(request, 'blog/')