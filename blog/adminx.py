import xadmin
from xadmin import views
from .models import Article, Category, Tag


class GlobalSiteSetting:
    # 设置后台顶部标题
    site_title = '博客后台管理'
    # 设置后台底部标题
    site_footer = 'robotti-blog'
    menu_style = "accordion"  # 设置菜单折叠，在左侧，默认的


xadmin.site.register(views.CommAdminView, GlobalSiteSetting)


class BaseXadminSetting:
    enable_themes = True
    # 使用主题
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseXadminSetting)


class ArticleAdmin:
    list_display = ('id', 'category', 'title', 'author', 'view', 'comment', 'created_time', 'modified_time')
    # 文章列表里显示想要显示的字段
    list_per_page = 20
    # 满50条数据就自动分页
    ordering = ('-created_time',)
    # 后台数据列表排序方式
    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面


xadmin.site.register(Article, ArticleAdmin)


class CategoryAdmin:
    list_display = ('id', 'name')


xadmin.site.register(Category, CategoryAdmin)


class TagAdmin:
    list_display = ('id', 'tag_name')


xadmin.site.register(Tag, TagAdmin)
