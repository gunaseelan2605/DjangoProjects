from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import WatchListAV, WatchListDetailAV,StreamPlatformAV,StreamPlatformDetailsAV

urlpatterns = [
    # path('list/', movie_list, name="movie_list"),
    # path('<int:reqpk>/', movie_details, name="movie_details"),
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('<int:pk>', WatchListDetailAV.as_view(), name="movie-detail"),
    path('stream/', StreamPlatformAV.as_view(), name="stream-list"),
    path('stream/<int:reqpk>/', StreamPlatformDetailsAV.as_view(), name="stream-detail"),

]
