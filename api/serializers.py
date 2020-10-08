from rest_framework import serializers
from posts.models import Post, Comment
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        read_only_fields = ['author']
        model = Post


class CommentSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ['author']
        model = Comment
