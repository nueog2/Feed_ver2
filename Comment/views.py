
from .models import Feed_Post, Comment
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import APIView
from .serializer import Feed_PostSerializer, CommentSerializer
from django.db import models 

class Feed_PostList(ListCreateAPIView):
    queryset = Feed_Post.objects.all()
    serializer_class = Feed_PostSerializer

class Feed_PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Feed_Post.objects.all()
    serializer_class = Feed_PostSerializer




class CommentPostList(ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post=post_id)

# class ClickLikeAPIView(APIView):
#     def get(self, request, pk, format=None):
#         post = Feed_Post.objects.get(pk=pk)
#         post.save()
#         return Response(status=status.HTTP_200_OK)
    

# class Comment(models.Model):
#     content = models.TextField(default="빈 댓글입니다.")
#     # post = models.ForeignKey(Feed_Post,on_delete=models.CASCADE)
#     users = models.ManyToManyField('User', related_name='comments')
#     pub_date = models.DateTimeField(null = True, auto_now_add=True)

#     class Meta:
#         db_table = 'comments'

# class User(models.Model):
#     username = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'users'



    
    
# #1. 댓글에 유저정보를 저장할 공간을 (필드 )만들기
# #2. manytomanyfield 사용 
# #3. POST클릭해서 받는 댓글에 manytomanyfield 추가해주기
# #4. 댓글에 유저정보를 저장하기 위해 댓글을 저장하는 시점에 유저정보를 저장해주기