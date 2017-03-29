# coding: utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser
import time
# from jasset.models import Asset, AssetGroup


class Checker(models.Model):
    checker_um = models.CharField(max_length=50, unique=True)
    checker_name = models.CharField(max_length=50, null=True)
    checker_role = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.checker_name


class CheckOrder(models.Model):
    check_order = models.IntegerField(unique=True)
    checker = models.ForeignKey(Checker, related_name='check_order')
    check_desc = models.CharField(max_length=100, null=True)
   


class RightApply(models.Model):
    app_name = models.CharField(max_length=100, unique=True)
    app_desc = models.CharField(max_length=100, null=True)
    insert_time = models.TimeField(auto_now=True)
    finish_time = models.TimeField(null=True)
    checkorder = models.ForeignKey(CheckOrder, related_name='right_app')
    asset = models.ManyToManyField(Asset, related_name='right_app')
    asset_group = models.ManyToManyField(AssetGroup, related_name='right_app')
    user = models.ManyToManyField(User, related_name='right_app')
    user_group = models.ManyToManyField(UserGroup, related_name='right_app')
    role = models.ManyToManyField(PermRole, related_name='right_app')
    APP_TYPE_CHOICES = (
        ('ZCQX', u'资产权限申请'),
        ('GPQX', u'用户组权限申请')
    )
    app_type = models.CharField(max_length=8, choices=APP_TYPE_CHOICES, default='ZCQX')

    def __unicode__(self):
        return self.app_name


class CheckList(models.Model):
    rightapply = models.ForeignKey(RightApply, related_name='check_list')
    checkorder = models.ForeignKey(CheckOrder, related_name='check_list')
    insert_time = models.TimeField(auto_now=True)
    finish_time = models.TimeField(null=True)
    check_status = models.NullBooleanField(null=True)
    check_if = models.NullBooleanField(default=False)
    check_desc = models.TextField(null=True)
