from rest_framework import serializers
from .models import *



        
        




class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'avatar',
            'slug',
        )

        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields= '__all__'   


class CommmentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields= ['id','article','user','context']      
        
        
class ArticleSerializer(serializers.ModelSerializer):

    rating = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='count'
     )

    author = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Article
        fields= ['id','author','title','content','date_pub','image_art','category','rating']
        

        