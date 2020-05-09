from rest_framework import serializers


class PicSerializer(serializers.Serializer):
    pic = serializers.ImageField(max_length=100)
