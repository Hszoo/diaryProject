from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

class PostViewSet(ModelViewSet) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 게시글 생성시 writer는 요청한 사용자로 자동 지정되도록
    # def perform_create(self, serializer) :
    #     serializer.save(writer=self.request.user)


class CommentViewSet(ModelViewSet) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def perform_create(self, serializer) :
    #     serializer.save(writer=self.request.user)
    def get_queryset(self, **kwargs) :
        id = self.kwargs['post_id']
        return self.queryset.filter(post=id)

# Create your views here.
