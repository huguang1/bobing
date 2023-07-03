# -*- coding: utf-8 -*-
# 18-9-11 下午12:40
# AUTHOR:June
from django.db import models


class BaseModel(models.Model):
    """抽象模型基类"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        # 指定这个类是一个抽象模型类
        abstract = True