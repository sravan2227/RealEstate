from django.urls import path

from . import views

# urlpatterns is used to fetch the data from views and display it thru the path
# and we need to add the below path in the main path which is Realstate.urls
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
