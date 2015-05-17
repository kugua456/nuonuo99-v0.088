#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from location.models import County

import datetime
import base.models as choice_set


class WedEssential(models.Model):
    boy = models.CharField(u'新郎', max_length=255)
    girl = models.CharField(u'新娘', max_length=255)
    t_wed = models.DateField(u'婚期')

    user = models.ForeignKey(User, verbose_name=u'用户')

    expect = models.TextField(u'婚礼期望', max_length=2000, blank=True)
    loc = models.ForeignKey(County, verbose_name=u'地点')
    btm_table_num = models.IntegerField(u'桌数(最少)', blank=True)
    top_table_num = models.IntegerField(u'桌数(最多)', blank=True)

    def __unicode__(self):
        return u'%s-%s(%s)' % (self.boy, self.girl, self.t_wed)

    class Meta:
        verbose_name = u"婚礼基本信息"
        verbose_name_plural = verbose_name


class CartInfo(models.Model):
    """under decision
    """
    buyer = models.ForeignKey(User, verbose_name=u'购买人')
    amount = models.PositiveIntegerField(u'数量', default=0)

    content_type = models.ForeignKey(ContentType, verbose_name=u'商品类型')
    object_id = models.PositiveIntegerField(u'商品 ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    t_add = models.DateTimeField(u'加入时间', default=datetime.datetime.now)

    def __unicode__(self):
        return self.buyer.username

    class Meta:
        verbose_name = u"购物车"
        verbose_name_plural = verbose_name
        unique_together = ("buyer", "content_type", "object_id")


class Order(models.Model):
    """decided

    keypoint: status, deadline. current progress
    """
    buyer = models.ForeignKey(User, verbose_name=u'购买人')
    t_wed = models.DateField(u'婚期')
    status = models.PositiveIntegerField(u'状态', choices=choice_set.C_ORDER_STATUS)
    t_add = models.DateTimeField(u'加入时间', default=datetime.datetime.now)
    t_paid = models.DateTimeField(u'付款时间', blank=True, null=True)
    amount = models.PositiveIntegerField(u'数量', default=0)

    content_type = models.ForeignKey(ContentType, verbose_name=u'商品类型')
    object_id = models.PositiveIntegerField(u'商品 ID')
    content_object = GenericForeignKey('content_type', 'object_id')

    progress = models.CharField(u'准备进展', max_length=255, blank=True)

    def __unicode__(self):
        return self.buyer.username

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name