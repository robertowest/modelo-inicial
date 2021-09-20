from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

# @login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'UI/index.html' )
    return HttpResponse(html_template.render(context, request))
    

# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = 'UI/' + request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'UI/page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template( 'UI/page-500.html' )
        return HttpResponse(html_template.render(context, request))


# def charts(request):
#     context = {}
#     context['segment'] = 'index'
#     html_template = loader.get_template( 'UI/charts.html' )
#     return HttpResponse(html_template.render(context, request))


# def tables(request):
#     context = {}
#     context['segment'] = 'index'
#     html_template = loader.get_template( 'UI/tables.html' )
#     return HttpResponse(html_template.render(context, request))
