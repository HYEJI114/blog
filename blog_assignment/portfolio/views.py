from django.shortcuts import render, get_object_or_404, redirect
from .models import Portfolio
# Create your views here.


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})

def detailport(request, port_id):
    port_detail = get_object_or_404(Portfolio, pk = port_id)
    return render(request,'detailport.html', {'portfolio' : port_detail})

def newport(request):
    return render(request, 'newport.html')

def createport(request):
    port = Portfolio()
    port.title = request.GET['title']
    port.description = request.GET['description']
    port.image = request.GET['image'] 
    port.save()
    return redirect('/portfolio/' + str(port.id))