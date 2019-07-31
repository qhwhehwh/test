from django.shortcuts import render,redirect
from .models import Portfolio

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def newportfolio(request):
    return render(request, 'newportfolio.html')

def createe(request):
    portfolio=Portfolio()
    portfolio.title=request.GET['title']
    portfolio.description=request.GET['description']
    portfolio.image=request.GET['file']
    portfolio.save() 
    return redirect('/portfolio/')

