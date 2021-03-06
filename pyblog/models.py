from django.db import models
import uuid


class Tag(models.Model):
    id = models.AutoField('ID', primary_key=True)
    name = models.CharField('标签.', max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Article(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    is_pub = models.BooleanField('是否发布', null=False, blank=False, default=True)
    is_top = models.BooleanField('是否置顶', null=False, blank=False, default=False)
    title = models.CharField('文章标题', max_length=255)
    content = models.TextField('内容')
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(verbose_name="发布日期", auto_now_add=True)  # auto_now_add 创建时自动添加时间
    mod_date = models.DateTimeField(verbose_name="更新日期", auto_now=True)      # auto_now 更新时,自动更新时间
    sort_weight = models.IntegerField("排序权重", null=False, blank=False, default=0)

    def __str__(self):
        return self.title

    class Meta:
        # https://docs.djangoproject.com/en/2.2/ref/models/options/
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Comment(models.Model):

    id = models.AutoField('ID', primary_key=True)
    nick = models.CharField(verbose_name='昵称', max_length=15)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    email = models.CharField(verbose_name='邮箱', max_length=20)
    ip = models.GenericIPAddressField(verbose_name='IP', null=True, blank=True)
    article = models.ForeignKey(Article, verbose_name='评论的某文章', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self',
                               verbose_name='父级评论id', on_delete=models.CASCADE, null=True, blank=True)
    at = models.ForeignKey('self',
                           verbose_name='@某评论', on_delete=models.CASCADE, null=True, blank=True, related_name='reply')
    create_date = models.DateTimeField(verbose_name="评论时间", auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_two_level_comments(parent_id, page=1, size=None):
        """
        :param parent_id: 一级评论的id
        :param page:   int 第几页
        :param size:   int 每页的大小
        :return: [Comment]
        """
        page = page if isinstance(page, int) else 1
        size = size if isinstance(size, int) else None
        page = page if page >= 1 else 1
        return Comment.objects.select_related('at').values(
            "id", "nick", "content", "email", "create_date", "at__nick", "at__id", "parent_id"
        ).filter(parent=parent_id).all().order_by('create_date')[(page - 1):size]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


class Info(models.Model):

    INFO_TYPE_CHOICES = [
        (0, "关于我"),
        (1, "咖啡")
    ]
    id = models.AutoField('ID', primary_key=True)
    is_pub = models.BooleanField('是否发布', null=False, blank=False, default=True)
    title = models.CharField('标题', max_length=255)
    i_type = models.IntegerField('类型', choices=INFO_TYPE_CHOICES, unique=True, blank=True, null=True)
    content = models.TextField('内容')
    pub_date = models.DateTimeField(verbose_name="发布日期", auto_now_add=True)
    mod_date = models.DateTimeField(verbose_name="更新日期", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        # https://docs.djangoproject.com/en/3.0/ref/models/options/
        verbose_name = '网站信息'
        verbose_name_plural = '网站信息'



