# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
#
# # Create your views here.
#
# def movielist(request):
#     movies = Movie.objects.all()
#     data = {"Movies": list(movies.values())}
#     return JsonResponse(data)
#
# def movie_details(request, reqpk):
#     movie = Movie.objects.get(pk=reqpk)
#     print(movie)
#     data = {
#         "name":movie.name,
#         "description":movie.description,
#         "active":movie.active
#     }
#     return JsonResponse(data)
