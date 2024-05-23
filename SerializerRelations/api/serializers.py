from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    #Provide name of the song
    # song=serializers.StringRelatedField(many = True, read_only=True)
    #Provide the id of the songs
    # song=serializers.PrimaryKeyRelatedField(many = True, read_only=True)  
    # Provide the link to the song
    # song=serializers.HyperlinkedRelatedField(many = True, read_only=True, view_name='song-detail')
    #Provide the data related to field
    # song=serializers.SlugRelatedField(many = True, read_only=True, slug_field='duration')
    song=serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender','song']