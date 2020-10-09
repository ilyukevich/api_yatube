from rest_framework import serializers
from posts.models import Post, Comment
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    """Class PostSerializer for Post"""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Class CommentSerializer for Comment"""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
