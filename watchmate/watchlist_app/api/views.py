from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
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


class StreamPlatformAV(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailsAV(APIView):

    def get(self, request, reqpk):
        try:
            platform = StreamPlatform.objects.get(pk = reqpk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Stream Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, reqpk):
        platform = StreamPlatform.objects.get(pk = reqpk)
        serializer = StreamPlatformSerializer(platform,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request, reqpk):
        platform = StreamPlatform.objects.get(pk=reqpk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class WatchListDetailAV(APIView):

    def get(self, request, pk):
        if request.method == 'GET':
            try:
                movie = WatchList.objects.get(pk=pk)
            except WatchList.DoesNotExist:
                return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = WatchListSerializer(movie, many=False)
            return Response(serializer.data)

    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
