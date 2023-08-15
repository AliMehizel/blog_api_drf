from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .models import User
from .serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404

#Get all article
@api_view(['GET'])
def GetArticles(request, format=None):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles,many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)
    # return Response()
#with users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetPArticles(request, format=None):
    articles = Article.objects.filter(author =request.user).all()
    if articles:
        
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)



#Get One artcile work
@api_view(['GET'])
def GetArticle(request,pk,formt=None):
    article = Article.objects.get(id=pk)
    
    if article:
        serializer = ArticleSerializer(article,many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#CREATE AN ARTICLE work
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createArticle(request,format=None):
    
    article= {
        'title':request.data['title'],
        'content':request.data['content'],
        'category':request.data['category'],
        'image_art':request.data['image_art'],
        } #contain all data about post article
    print(request.data)
    serializer = ArticleSerializer(data = article)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        print('not valid')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#UPDATE ARTICLE 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateArticle(request, pk, format=None):
    article = Article.objects.get(id =pk)
    data = request.data 
    if article:
        serializer = ArticleSerializer(article,data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

#DELETE ARTICLE work
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteArticle(request,pk,format=None):
    article = Article.objects.get(id=pk)
    if article:
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

"""  """
#manage RATING
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addRating(request,format=None):
    article = get_object_or_404(Article, title=request.data['title'])
    rating ,created = Rating.objects.get_or_create(article=article,user=request.user)
    
    if rating.count == 1:
        rating.count = 0
        rating.save()
    else:
        rating.count = 1
        rating.save()
    article = Article.objects.get(title= article)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data,status=status.HTTP_201_CREATED)



#get all comment work
@api_view(['GET'])
def GetComment(request,pk,format=None):
    article = Article.objects.get(id=pk)
    comment = Comment.objects.filter(article=article).all()
    if comment.exists():
        serializer = CommmentSerializer(comment,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
 
#create comment work
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createComment(request,format=None):
    data = request.data
    serializer = CommmentSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)   

    

    
      

""" 
#by user permission
-get private article
-create article DONE
-update article DONE
-delete article DONE
-addRating DONE
-create comment DONE
-update comment DONE
#out of this
-getallRate DONE
-getallcomment DONE
-search for articles
-filter by category
#specify all status code
"""
    


