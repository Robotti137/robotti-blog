from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


# Create your models here.

# 文章类型
class Category(models.Model):
    name = models.CharField('文章类型', max_length=30)

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    tag_name = models.CharField('标签名', max_length=30)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


# 评论
class Comment(models.Model):
    title = models.CharField('标题', max_length=100)
    source_id = models.CharField('文章id或source名称', max_length=25)
    create_time = models.DateTimeField('评论时间', auto_now=True)
    user_name = models.CharField('评论用户', max_length=25)
    url = models.CharField('链接', max_length=100)
    comment = models.CharField('评论内容', max_length=500)


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章类型')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)
    digest = models.TextField('文章摘要', max_length=200, blank=True)  # 文章摘要
    content = MDTextField('文章正文', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    view = models.BigIntegerField('阅读数', default=0)
    comment = models.BigIntegerField('评论数', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    picture = models.ImageField(upload_to='article_picture/%Y/%m/%d/', verbose_name='文章封面')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
