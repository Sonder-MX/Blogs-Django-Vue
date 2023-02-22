from rest_framework import viewsets

from .models import Comment
from .permissions import IsOwnerOrReader
from .serializers import CommentSeriallizer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSeriallizer
    permission_classes = [IsOwnerOrReader]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
