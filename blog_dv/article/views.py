from rest_framework import generics
# from rest_framework.permissions import IsAdminUser
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from .permissions import IsAdminUserOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    # 在保存前调用
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]
