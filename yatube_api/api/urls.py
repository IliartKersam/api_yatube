from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                   basename='comments')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('follow', FollowViewSet, basename='follow')

jwtpatterns = [
    re_path(r'^create/?', views.TokenObtainPairView.as_view(), name='jwt-create'),
    re_path(r'^refresh/?', views.TokenRefreshView.as_view(), name='jwt-refresh'),
    re_path(r'^verify/?', views.TokenVerifyView.as_view(), name='jwt-verify'),
]

urlpatterns = [
    path(r'v1/jwt/', include(jwtpatterns)),
    path(r'v1/', include(v1_router.urls)),
]
