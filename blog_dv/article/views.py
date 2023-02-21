from rest_framework import viewsets

from .filters import ArticleFilter
# from rest_framework.permissions import IsAdminUser
from .models import Article
from .permissions import IsAdminUserOrReadOnly
from .serializers import ArticleSerializer


# class ArticleList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     # 在保存前调用
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#     permission_classes = [IsAdminUserOrReadOnly]


# 视图集类把列表、详情等逻辑都集成到一起，并且提供了默认的增删改查的实现
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filterset_class = ArticleFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
