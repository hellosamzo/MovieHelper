from django.shortcuts import render
from .models import Post
import requests, smtplib, ssl
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
        port = 465  # For SSL       
        # Create a secure SSL context
        context = ssl.create_default_context()

        # do email stuff here
        return render(request, 'blog/about.html', {

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
    # get the current month

    
    # get latest film titles using bs4
    url = "https://www.imdb.com/movies-coming-soon/2020-05/?ref_=cs_dt_nx"
    html = req.urlopen(url).read().decode('utf8')
    html[:60]

    # array which will hold titles
    latest_titles = []

    # fetch titles
    soup = bs.BeautifulSoup(html, 'html.parser')
    for link in soup.find_all("a", href=lambda href: href and href.startswith("/title/tt")):
        latest_titles.append(link.get('title'))

    return render(request, 'blog/latest.html', {
        'titles': latest_titles,
    })

def announcements(request):
    return render(request, 'blog/announcements.html', {

    })

def calendars(request):
    return render(request, 'blog/calendars.html', {

    })

def dev(request):
    return render(request, 'blog/dev.html', {
        
    })


#def spotify(request):
 #   return render(request, 'blog/')