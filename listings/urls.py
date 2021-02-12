from django.urls import path

from . import views

# if we leave as '' it will directly routed to listing app
# Int was declared in second path to display the particular listing. like
#listing/25(which is listing_id)
# urlpatterns is used to fetch the data from views and display it thru the path
# and we need to add the below path in the main path which is Realstate.urls
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
