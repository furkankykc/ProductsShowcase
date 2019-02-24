from django.urls import path

from product import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('product/', views.product, name='product'),
    path('page/<str:page_name>', views.dynamic, name='dynamic'),

]
# for page in models.Page.objects.all():
#     urlpatterns.append(path(page.name+'/',views.dynamic))
