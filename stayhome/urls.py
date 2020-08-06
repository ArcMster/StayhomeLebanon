from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<pk>', views.category, name = 'category'),
    path('categoryar/<pk>', views.categoryar, name = 'categoryar'),
    path('description/<pk>', views.description, name='description'),
    path('descriptionar/<pk>', views.descriptionar, name='descriptionar'),
    path('about.html', views.about,name = "about"),
    path('add.html', views.add, name = "add"),
    path('contact.html', views.contact, name= "contact"),
    path('eabout.html', views.eabout,name = "eabout"),
    path('eadd.html', views.eadd, name = "eadd"),
    path('econtact.html', views.econtact, name= "econtact"),
    path('eget10.html', views.eget,name = 'eget'),
    path('get10.html', views.get, name = "get"),
    path('products1.html', views.products, name = "products"),
    path('eproducts1.html', views.eproducts, name = "eproducts"),
    path('en.html', views.home, name = "en"),
    path('index.html', views.index, name = 'index'),
    path('index.html/about.html', views.about,name = "about"),
    path('index.html/add.html', views.add, name = "add"),
    path('index.html/contact.html', views.contact, name= "contact"),
    path('en.html/eabout.html', views.eabout,name = "eabout"),
    path('en.html/eadd.html', views.eadd, name = "eadd"),
    path('en.html/econtact.html', views.econtact, name= "econtact"),
    path('en.html/eget10.html', views.eget,name = 'eget'),
    path('index.html/get10.html', views.get, name = "get"),
    path('index.html/products1.html', views.products, name = "products"),
    path('en.html/eproducts1.html', views.eproducts, name = "eproducts"),
    path('en.html', views.home, name = "en"),
    path('add_service', views.add_service, name = "add_service"),
    path('add_servicear', views.add_servicear, name = "add_servicear"),
    path('message', views.usercontact, name = "usercontact"),
    path('messagear', views.usercontactar, name = "usercontactar"),
    path('search',views.search, name = 'search'),
    path('searchar', views.searchar, name = 'searchar')
    

]

urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)