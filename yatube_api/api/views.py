from posts.models import Follow, Group, Post, User
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer, UserSerializer)

from .logic_views import FollowMixin, MyMixinViewSet, MyQuerySetMixin
from .permissions import ReadPermission


class PostViewSet(MyMixinViewSet, viewsets.ModelViewSet):
    """ViewSet для создания, получения, удаления и редактирования постов.
    Методы, которые необходимо переопределить унаследовали от
    кастомного миксина.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ReadPermission,)
    pagination_class = LimitOffsetPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для получения информации о группе, только для чтения.
    Информацию получить могут только авторизованные пользователи."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(MyMixinViewSet, MyQuerySetMixin, viewsets.ModelViewSet):
    """ViewSet для создания, получения, удаления и редактирования комментариев.
    Наследуемся от двух кастомных миксинов, переопределяем 4 метода.
    """
    queryset = Follow.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для получения информации о пользователях, только для чтения."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowViewSet(FollowMixin, viewsets.ModelViewSet):
    """ViewSet для создания, получения подписок. Поиск по подписке.
    Наследуемся от кастомного миксина, переопределяем 2 метода.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
