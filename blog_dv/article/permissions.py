from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员可以修改
    其他用户只可以查看
    """

    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD, OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True
        # 仅管理员可进行其他操作
        return request.user.is_superuser
