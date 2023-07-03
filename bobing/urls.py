# -*- coding: utf-8 -*-
# 18-9-11 下午2:16
# AUTHOR:June
from django.conf.urls import url
from bobing.views import RecordView, MineView, InfoView, LoginView, IndexView

urlpatterns = [
    url(r'^$',IndexView.as_view(), name='index'),
    url(r'^lottery/records$', RecordView.as_view(), name='recs'),
    url(r'^lottery/verify$', LoginView.as_view(), name='new'),
    url(r'^lottery/records/mine$', MineView.as_view(), name='mine'),
    url(r'^lottery/info$',InfoView.as_view(), name='info')

]
