from django.urls import path

from .views import Home, MyPost
from .views import DetailPost,EditPost,UpdatePost,DeletePost
from .views import LikeHome,LikeDetail
from .views import FollowHome, FollowDetail,FollowList
from .views import CommentCreate

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('mypost/', MyPost.as_view(), name='mypost'),
    path('detail/<int:pk>', DetailPost.as_view(), name='detail'),
    path('edit/', EditPost.as_view(), name="edit"),
    path('detail/<int:pk>/update', UpdatePost.as_view(), name='update'),
    path('detail/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    #いいね機能
    path('like-home/<int:pk>', LikeHome.as_view(), name='like-home'),
    path('like-detail/<int:pk>', LikeDetail.as_view(), name='like-detail'),
    #フォロー機能
    path('follow-home/<int:pk>', FollowHome.as_view(), name='follow-home'),
    path('follow-detail/<int:pk>', FollowDetail.as_view(), name='follow-detail'),
    path('follow-list/', FollowList.as_view(), name='follow-list'),
    #コメント
    path('comment/create/<int:pk>/',CommentCreate.as_view(), name='comment_create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
