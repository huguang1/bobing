# -*- coding: utf-8 -*-
# 18-9-11 下午2:26
# AUTHOR:June
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from extra_apps import xadmin
from bobing.models import Prize, Rule, Member, Rec, Info, Sysmem
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import datetime, pytz
from import_export import resources  # 导入excel按钮
from xadmin.plugins.actions import BaseActionView
from xadmin import views


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView, BaseSetting)


class MenberResources(resources.ModelResource):
    """会员导入类"""

    class Meta:
        model = Member
        fields = ('id', 'username', 'score', 'extra_str')


class RuleResources(resources.ModelResource):
    """规则导入类"""

    class Meta:
        model = Rule
        fields = ('id', 'username', 'prize_id')


class Globalsettings(object):
    site_title = '博饼后台管理系统'
    site_footer = 'By Office Seven'
    # menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, Globalsettings)


class PrizeAdmin(object):
    list_display = ['prize_id', 'name', 'desc', 'probability', 'num', 'is_show']
    search_fields = ['prize_id', 'name', 'desc', 'probability', 'is_show']
    ordering = ['prize_id']
    list_per_page = 15
    list_editable = ['probability', 'name', 'num']
    model_icon = 'fa fa-gift'


class RuleAdmin(object):
    list_display = ['id', 'username', 'prize_id', 'is_use', 'use_time', 'create_time', 'is_delete']
    search_fields = ['username', 'prize_id', 'is_use', 'is_delete']
    list_filter = ['prize_id', 'is_delete', 'create_time']
    ordering = ['use_time']
    list_per_page = 15
    ordering = ['-id']
    import_export_args = {'import_resource_class': RuleResources}  # 导入规则
    model_icon = 'fa fa-play'


class MemberAdmin(object):
    list_display = ['id', 'username', 'score', 'create_time', 'update_time', 'is_delete']
    search_fields = ['username', 'score', 'extra_int', 'extra_str', 'is_delete']
    list_filter = ['create_time', 'update_time', 'is_delete', 'score']
    ordering = ['-create_time']
    list_per_page = 15
    list_editable = ['score', 'is_delete']
    import_export_args = {'import_resource_class': MenberResources}  # 导入会员
    model_icon = 'fa fa-user'


class SendAction(BaseActionView):
    action_name = "send_action"
    description = u'发送所选的 奖品'
    model_perm = 'change'

    def do_action(self, queryset):
        now = datetime.datetime.utcnow().replace(tzinfo=pytz.timezone('UTC'))
        queryset.update(is_sent=True, send_time=now)


class RecAdmin(object):
    list_display = ['id', 'user', 'is_sent', 'prize', 'desc', 'send_time', 'user_ip', 'way', 'create_time', 'update_time',
                    'is_delete']
    search_fields = ['user', 'prize__prize_id', 'is_sent', 'way', 'is_delete']
    list_filter = ['prize', 'send_time', 'user_ip', 'way', 'create_time', 'update_time', 'is_sent', 'is_delete']
    ordering = ['-create_time']
    list_per_page = 15
    list_editable = ['is_sent', 'is_delete', 'send_time']
    actions = [SendAction, ]
    model_icon = 'fa fa-check-square'
    refresh_times = [30, 60, 300]
    def desc(self, obj):
        return obj.prize.desc
    desc.short_description = '<font color="#428BCA">礼品</font>'

class InfoAdmin(object):
    list_display = ['name', 'is_open', 'errmsg', 'start_time', 'end_time', 'times', 'timee', 'create_time', 'update_time', 'is_delete']
    list_editable = ['is_open', 'is_delete', 'start_time', 'end_time', 'times', 'timee']
    ordering = ['create_time']
    list_per_page = 10
    model_icon = 'fa fa-calendar'


class XadminUser(UserCreationForm):
    class Meta:
        fields = ("username", "is_staff",'nickname')


class sysAdmin(object):
    list_display = ['username', 'nickname', 'last_login']

    def get_model_form(self, **kwargs):
        if self.org_obj is None:
            self.form = XadminUser
        else:
            self.form = UserChangeForm
        return super(sysAdmin, self).get_model_form(**kwargs)


xadmin.site.unregister(Sysmem)
xadmin.site.register(Prize, PrizeAdmin)
xadmin.site.register(Rule, RuleAdmin)
xadmin.site.register(Member, MemberAdmin)
xadmin.site.register(Rec, RecAdmin)
xadmin.site.register(Info, InfoAdmin)
xadmin.site.register(Sysmem,sysAdmin)






