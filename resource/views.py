from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
import os
import json

# predict is a function that takes an image path and returns the prediction result
from .ml import predict
from django.http import JsonResponse


from .models import Leafdiseasedetector
from .serializers import LeafdiseasedetectorSerializer
from .decorators import validate_leafdiseasedetector_data

from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateLeafdiseasedetectorView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Leafdiseasedetector.objects.all()
    serializer_class = LeafdiseasedetectorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_leafdiseasedetector_data
    def post(self, request, *args, **kwargs):
        a_tag = Leafdiseasedetector.objects.create(
            user=User.objects.get(pk=request.user.pk),
            images=request.data["images"],
        )
        
        # server_path
        
        absolute_path = a_tag.images
        
        print(absolute_path, 'http://localhost:8000/'+str(absolute_path))
        prediction = predict('http://localhost:8000/'+str(absolute_path))
        print(prediction)
        
        
        return Response(
            data=LeafdiseasedetectorSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class LeafdiseasedetectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Leafdiseasedetector.objects.all()
    serializer_class = LeafdiseasedetectorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_leafdiseasedetector = self.queryset.get(pk=kwargs["pk"])
            return Response(LeafdiseasedetectorSerializer(a_leafdiseasedetector).data)
        except Leafdiseasedetector.DoesNotExist:
            return Response(
                data={
                    "message": "Leafdiseasedetector with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_leafdiseasedetector_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = LeafdiseasedetectorSerializer()
            updated_leafdiseasedetector = serializer.update(a_tag, request.data)
            return Response(LeafdiseasedetectorSerializer(updated_leafdiseasedetector).data)
        except Leafdiseasedetector.DoesNotExist:
            return Response(
                data={
                    "message": "Leafdiseasedetector with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_leafdiseasedetector = self.queryset.get(pk=kwargs["pk"])
            a_leafdiseasedetector.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Leafdiseasedetector.DoesNotExist:
            return Response(
                data={
                    "message": "Leafdiseasedetector with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
