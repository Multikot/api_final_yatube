from posts.models import Group, Post, User
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer, UserSerializer)

from .logic_views import CreateMixin, FollowMixin, QuerySetMixin
from .permissions import ReadOnlyPermission


class PostViewSet(CreateMixin, viewsets.ModelViewSet):
    """ViewSet для создания, получения, удаления и редактирования постов.
    Методы, которые необходимо переопределить унаследовали от
    кастомного миксина.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (ReadOnlyPermission,)
    pagination_class = LimitOffsetPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для получения информации о группе, только для чтения.
    Информацию получить могут только авторизованные пользователи."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnlyPermission,)


class CommentViewSet(
    CreateMixin, QuerySetMixin, viewsets.ModelViewSet
):
    """ViewSet для создания, получения, удаления и редактирования комментариев.
    Наследуемся от двух кастомных миксинов, переопределяем 4 метода.
    """
    serializer_class = CommentSerializer
    permission_classes = (ReadOnlyPermission,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для получения информации о пользователях, только для чтения."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowViewSet(FollowMixin):
    """ViewSet для создания, получения подписок. Поиск по подписке.
    Наследуемся от кастомного миксина, переопределяем 2 метода.
    """
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')
