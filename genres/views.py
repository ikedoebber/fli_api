from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from django.http import JsonResponse
from app.permissions import GlobalDefaultPermission


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 

    def delete(self, *args, **kwargs): 
        try:
            instance = self.get_object()
            instance.delete()
            return JsonResponse({'message': 'Genero deletado com sucesso.'}, status=204)
        except Exception as e: 
            return JsonResponse({'error': str(e)}, status=500)
