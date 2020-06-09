import xadmin
from xadmin import views


class GlobalSiteSetting:
    # 设置后台顶部标题
    site_title = '博客后台管理'
    # 设置后台底部标题
    site_footer = 'robotti-blog'
    # 设置可折叠
    menu_style = 'accordion'


class BaseXadminSetting:
    enable_themes = True
    # 使用主题
    use_bootswatch = True


# 配置图标
class SafeAdmin(object):
    model_icon = 'fa fa-key'


# 注册
xadmin.site.register(views.CommAdminView, GlobalSiteSetting)
xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
