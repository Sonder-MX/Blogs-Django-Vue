from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReader(BasePermission):
    message = '你必须是发布者才可以修改！'

    @staticmethod
    def safe_methods_or_owner(request, func):
        if request.method in SAFE_METHODS:
            return True
        return func()

    def has_permission(self, request, view):
        """登录验证"""
        return self.safe_methods_or_owner(
            request,
            lambda: request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """obj为评论模型的实例，执行晚于视图集中perform_create()方法"""
        return self.safe_methods_or_owner(
            request,
            lambda: obj.author == request.user
        )
