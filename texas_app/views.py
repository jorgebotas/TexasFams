from django.shortcuts import render

def context(request):
    return render(request, 'texas_app/context.html', {})
