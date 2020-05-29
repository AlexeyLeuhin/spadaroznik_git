from django.shortcuts import render
import newsapi
import requests


def index(request):
    url = 'https://prime.exchangerate-api.com/v5/5df56df208553f49c68f7c31/latest/USD'
    response = requests.get(url)
    curr_response = response.json()
    USDtoEUR = curr_response['conversion_rates']['EUR']
    USDtoCAD = curr_response['conversion_rates']['CAD']
    return render(request, 'main_page/homePage.html', context={"USDtoCAD":USDtoCAD, "USDtoEUR":USDtoEUR, })
