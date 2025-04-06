from django.forms import model_to_dict
from rest_framework import serializers

from .models import Leafdiseasedetector


class LeafdiseasedetectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leafdiseasedetector
        fields = "__all__"
        image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
        # fields = ["id", "title", date, "description", "images"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.capacity = validated_data.get("capacity", instance.capacity)
        instance.images = validated_data.get("images", instance.images)

        instance.save()
        return instance

