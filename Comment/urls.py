from .views import Feed_PostList, Feed_PostDetail, CommentPostList
from django.urls import path


urlpatterns = [
    path('feed/',Feed_PostList.as_view()),
    path('detail/<int:pk>/',Feed_PostDetail.as_view()),
    path('detail/<int:post_id>/comment/',CommentPostList.as_view()),
]