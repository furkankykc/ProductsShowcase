import sys

from django.apps import apps
from django.shortcuts import render

from .models import *


#

# Create your views here.

def currentFuncName(n=0):
    return sys._getframe(n + 1).f_code.co_name.title()


def index(request):
    # for page in Page.objects.all():
    # urlpatterns.append(path(page.name + '/', views.dynamic))
    # print(page)
    title = currentFuncName()
    context = {'title': title,
               'contact': Contact.objects.all(),
               'prices': PricingPlan.objects.all().order_by('price')

               }
    return render(request, 'index.html', context)


def about(request):
    title = currentFuncName()
    context = {'title': title,
               'contact': Contact.objects.all()
               }
    return render(request, 'about.html', context)


def contact(request):
    title = currentFuncName()
    contact = Contact.objects.all()
    context = {'title': title,
               'contact': contact
               }
    return render(request, 'contact.html', context)


def pricing(request):
    title = currentFuncName()
    prices = PricingPlan.objects.all().order_by('price')
    context = {'title': title,
               'pricingplan': prices
               }
    return render(request, 'pricing.html', context)


def product(request):
    # for page in Page.objects.all():
    # urls.urlpatterns.append(path(page.name + '/', dynamic))
    title = currentFuncName()
    context = {'title': title}
    return render(request, 'product.html', context)


def dynamic(request, page_name):
    page = Page.objects.get(name=page_name)
    context = {'page': page

               }
    for comp in page.components.all():
        try:
            my_model = apps.get_model(app_label='product', model_name=str(comp.model))
            context.update({str(comp.model).lower(): my_model.objects.all()})
            # print(my_model.objects.all())
        except:
            continue
    return render(request, page.template, context)
