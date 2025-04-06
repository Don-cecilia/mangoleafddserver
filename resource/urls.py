from django.urls import path
from .views import ListCreateLeafdiseasedetectorView, LeafdiseasedetectorDetailView

urlpatterns = [
    path('leafdiseasedetector/', ListCreateLeafdiseasedetectorView.as_view(), name="Leafdiseasedetector-list-create"),
    path('leafdiseasedetector/<int:pk>/', LeafdiseasedetectorDetailView.as_view(), name="Leafdiseasedetector-detail"),
    
]
