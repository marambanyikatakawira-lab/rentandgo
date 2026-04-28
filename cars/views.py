from django.shortcuts import render
from .models import Car
from .sorting import bubble_sort, selection_sort, quick_sort
from .searching import linear_search, binary_search

def home(request):
    cars = Car.objects.filter(is_available=True)
    
    # Sorting Section
    if 'sort' in request.GET:
        algorithm = request.GET.get('algorithm')
        column = request.GET.get('column')
        order = request.GET.get('order')
        reverse = True if order == 'desc' else False
        
        if algorithm == 'bubble':
            cars = bubble_sort(cars, column, reverse)
        elif algorithm == 'selection':
            cars = selection_sort(cars, column, reverse)
        elif algorithm == 'quick':
            cars = quick_sort(cars, column, reverse)
    
    # Searching Section
    if 'search' in request.GET:
        search_algorithm = request.GET.get('search_algorithm')
        search_column = request.GET.get('search_column')
        search_value = request.GET.get('search_value')
        
        if search_value: # Only search if user typed something
            if search_algorithm == 'linear':
                cars = linear_search(cars, search_column, search_value)
            elif search_algorithm == 'binary':
                cars = binary_search(cars, search_column, search_value)
    
    context = {'cars': cars}
    return render(request, 'cars/home.html', context)