from rest_framework import serializers

from comment.serializers import CommentSeriallizer
from user_info.serializers import UserDescSerializer
from .models import Article, Category, Tag, Avatar


# class ArticleListSerializer(serializers.ModelSerializer):
#     # 实现超链接可以用 DRF 框架提供的 HyperlinkedIdentityField
#     url = serializers.HyperlinkedIdentityField(view_name='article:detail')
#     author = UserDescSerializer(read_only=True)  # 只读
#
#     class Meta:
#         model = Article
#         fields = ['url', 'title', 'body', 'author']
#         # read_only_fields = ['author']
#
#
# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

class TagSerializer(serializers.HyperlinkedModelSerializer):

    # 检查tag text是否已存在
    @staticmethod
    def check_tag_obj_exists(validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError(f'Tag with text {text} exists.')

    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = Tag
        fields = '__all__'


class AvatarSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='avatar-detail')

    class Meta:
        model = Avatar
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    # category 的嵌套序列化字段
    category = CategorySerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )

    # 覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # category_id 字段的验证器 400 error
    @staticmethod
    def validate_category_id(value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError(f"Category with id {value} not exists.")
        return value

    avatar = AvatarSerializer(read_only=True)
    avatar_id = serializers.IntegerField(
        write_only=True,
        allow_null=True,
        required=False
    )

    @staticmethod
    def validate_avatar_id(value):
        if not Avatar.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError(f'Avatar with id {value} not exists!')
        return value


class ArticleSerializer(ArticleBaseSerializer):
    """博文序列化器"""

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}


class ArticleDetailSerializer(ArticleBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    comment = CommentSeriallizer(many=True, read_only=True)
    # 渲染后的正文
    body_html = serializers.SerializerMethodField()
    # 渲染后的目录
    toc_html = serializers.SerializerMethodField()

    @staticmethod
    def get_body_html(obj):
        return obj.get_md()[0]

    @staticmethod
    def get_toc_html(obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]
