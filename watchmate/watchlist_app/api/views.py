from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Rseponse(serializer.errors)
#
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, reqpk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=reqpk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, many=False)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=reqpk)
#         serializer = MovieSerializer(movie,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Rseponse(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=reqpk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Rseponse(serializer.errors)

class MovieDetailAV(APIView):

    def get(self, request, reqpk):
        if request.method == 'GET':
            try:
                movie = Movie.objects.get(pk=reqpk)
            except Movie.DoesNotExist:
                return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = MovieSerializer(movie, many=False)
            return Response(serializer.data)

    def put(self,request,reqpk):
        movie = Movie.objects.get(pk=reqpk)
        serializer = MovieSerializer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Rseponse(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)

    def delete(self,request, reqpk):
        movie = Movie.objects.get(pk=reqpk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
