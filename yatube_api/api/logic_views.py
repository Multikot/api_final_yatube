from django.shortcuts import get_object_or_404
from posts.models import Post


class CreateMixin:
    """Кастомный миксин, который переопределяет встроенные методы:."""
    def perform_create(self, serializer):
        """При создании автора поста или комментария берем из request."""
        serializer.save(author=self.request.user)


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
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """При создании подписки user берем из request."""
        serializer.save(user=self.request.user)
