from rest_framework.serializers import ModelSerializer

from .models import BookModel


class BookSerializer(ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('__all__')
