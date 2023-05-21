from rest_framework import serializers
from tweets_app.models import Tuit


class TuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuit
        fields = '__all__'
