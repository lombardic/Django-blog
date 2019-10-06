from django.urls import include, path
from rest_framework import routers
from blogging.views import detail_view, list_view, add_model, UserViewSet, GroupViewSet, PostViewSet, CategoryViewSet
from blogging.feeds import LatestEntriesFeed

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('', include(router.urls)),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('add_post/', add_model, name="new_post"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('latest/feed/', LatestEntriesFeed()),
]
