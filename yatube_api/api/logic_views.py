from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Follow, Post


class CreateDestroyUpdateMixin:
    """Кастомный миксин, который переопределяет встроенные методы:."""
    def perform_create(self, serializer):
        """При создании автора поста или комментария берем из request."""
        serializer.save(author=self.request.user)

    def perform_destroy(self, serializer):
        """при удалении объекта нужна проверка на авторство."""
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(serializer)

    def perform_update(self, serializer):
        """при изменении объекта нужна проверка на авторство."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)


class QuerySetMixin:
    """Ксатомный миксин для переопределения запроса."""
    def get_queryset(self):
        """Получаем post_id, который понадобится для создания комментария."""
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()


class FollowMixin:
    """Миксимн для подписок."""
    def get_queryset(self):
        """Получаем запрос, где юзера берем из request."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """При создании подписки user берем из request."""
        serializer.save(user=self.request.user)
