from django.shortcuts import render
from .models import Post
import requests, smtplib, ssl, datetime
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
    if request.method == 'GET': 
        emailRecv = request.GET.get('email', None)
        if emailRecv:
            favCinema = "London Oval" #placeholder
            genres = "Action" #placeholder

            # do email stuff here
            sender = 'todo'
            receivers = emailRecv
            message = """From: From Person <sender>
                    To: To Person <receivers>
                    Subject: Movie Helper Email Test

                    This is a test email from Movie Helper.
                    """
            smtpObj = smtplib.SMTP()
            smtpObj.starttls()
            mailserver = smtpObj.SMTP('smtp.gmail.com',587)
            mailserver.ehlo()
            mailserver.login('moviehelpr838fhsu@gmail.com', 'mypassword')
            mailserver.sendmail('moviehelpr838fhsu@gmail.com', receivers, message)
            mailserver.quit()


    return render(request, 'blog/about.html')

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
    dt = datetime.datetime.today()
    print(dt.month)
    month = dt.month
    monthStr = dt.strftime("%B");
    year = datetime.datetime.today().year

    # get correct url based on the month
    if month > 9:
        url = "https://www.imdb.com/movies-coming-soon/2020-" + str(month) + "/?ref_=cs_dt_nx"
    else:
        url = "https://www.imdb.com/movies-coming-soon/2020-0" + str(month) + "/?ref_=cs_dt_nx"

    # get latest film titles using bs4
    html = req.urlopen(url).read().decode('utf8')
    html[:60]

    # array which will hold titles
    latest_titles = []

    # fetch titles
    soup = bs.BeautifulSoup(html, 'html.parser')
    for link in soup.find_all("a", href=lambda href: href and href.startswith("/title/tt")):
        
        title = link.get('title')

        if title is not None:
            latest_titles.append(link.get('title'))

        # use api to get descriptions etc
        
    return render(request, 'blog/latest.html', {
        'titles': latest_titles,
        'month': monthStr,
        'year': year
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