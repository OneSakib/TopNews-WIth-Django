from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
import html5lib


def get_state_wise():
    URL = "https://www.mygov.in/corona-data/covid19-statewise-status/"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html5lib')
    case = soup.findAll('div', attrs={'class': 'field-collection-item-field-covid-statewise-data'})
    state_name = []
    for i in range(0, 36):
        state_name.append(case[i].find_next("div").find_next("div").find_next("div").find_next("div").text)

    case = soup.findAll('div', attrs={'class': 'field-name-field-total-confirmed-indians'})
    confirmed = []
    for i in range(0, 36):
        confirmed.append(case[i].find_next("div").find_next("div").text)
    case = soup.findAll('div', attrs={'class': 'field-name-field-cured'})
    discharged = []
    for i in range(0, 36):
        discharged.append(case[i].find_next("div").find_next("div").text)
    case = soup.findAll('div', attrs={'class': 'field-name-field-deaths'})
    death = []
    for i in range(0, 36):
        death.append(case[i].find_next("div").find_next("div").text)
    data = list(zip(state_name, confirmed, discharged, death))

    return data


def getcases():
    URL = 'https://www.mygov.in/corona-data/covid19-statewise-status/'
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html5lib')
    active = soup.find_all("div", class_='field-name-field-total-active-case')[0]
    active = active.text[14:]
    discharge = soup.find_all("div", class_='field-name-field-total-cured-discharged')[0]
    discharge = discharge.text[18:]
    death = soup.find_all("div", class_='field-name-field-total-death-case')[0]
    death = death.text[8:]
    return {'active': active, 'discharged': discharge, 'death': death}


# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=587b095f89ab4af7955d778b674005ea')
    response = requests.get(url)
    response = response.json()
    if response['status'] == 'ok':
        total = response['totalResults']
        articles = response['articles']
        return render(request, 'index.html', {'total': total, 'articles': articles, 'cases': getcases()})
    return HttpResponse('No Data is Found. please try again.')


def statewise(request):
    return render(request, 'statewise.html', {'data': get_state_wise()})
