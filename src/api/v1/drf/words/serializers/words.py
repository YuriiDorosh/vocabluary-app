from rest_framework import serializers
from src.apps.words.models.words import Word
from src.apps.words.enums import LevelEnum


class ListWordSerializer(serializers.ModelSerializer):
    level = serializers.ChoiceField(choices=LevelEnum.choices)

    class Meta:
        model = Word
        fields = ['id', 'word', 'definition', 'level', 'owner']
        

class CreateWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'definition', 'level']
        

class UpdateWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'definition', 'level']
        

class DetailWordSerializer(serializers.ModelSerializer):
    level = serializers.ChoiceField(choices=LevelEnum.choices)

    class Meta:
        model = Word
        fields = [
            'id', 
            'word', 
            'definition', 
            'level', 
            'owner',
            
            ]