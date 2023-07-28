from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from .models import Post, Comment

class PostSerializer(ModelSerializer) :
    # 이거 해줘야 writer의 id값이 아닌 username으로 불러옴 
    # writer = serializers.ReadOnlyField(source='writer.username')
    class Meta :
        model = Post 
        fields = ['id', 'title', 'content', ]

class PostRetrieveModelSerializer(PostSerializer) : # base 상속받아야됨 
    class Meta(PostSerializer.Meta) :
        depth = 1
        
class CommentSerializer(ModelSerializer) :
    #writer = serializers.ReadOnlyField(source='writer.username')
    class Meta :
        model = Comment
        fields = ['comment', 'post', ]