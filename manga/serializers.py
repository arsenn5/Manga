from rest_framework import serializers

from manga.models import Manga, Comment, Genre


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id', 'image', 'ru_name', 'eng_name', 'year']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'name'.split()


class TypeSerializer(serializers.Serializer):
    class Meta:
        model = Manga
        fields = 'title'.split()


class CommentCreateSerializer(serializers.ModelSerializer):
    users = serializers.CharField(read_only=True)
    text = serializers.CharField(max_length=250)

    class Meta:
        model = Comment
        fields = ['user', 'users', 'text', 'manga']




class MangaDetailSerializer(serializers.ModelSerializer):
    comment = CommentCreateSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Manga
        fields = '__all__'
