# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.db.models import Q


class CustomManager(models.Manager):
    def current(self):
        current_event = self.filter(Q(date=datetime.date.today(), date_end__isnull=True) |
                                    Q(date__lte=datetime.date.today(),
                                    date_end__isnull=False,
                                    date_end__gte=datetime.date.today()))
        return current_event

    def archive(self):
        archive_event = self.filter(Q(date__lt=datetime.date.today(), date_end__isnull=True) |
                                    Q(date_end__isnull=False, date_end__lt=datetime.date.today()))
        return archive_event


class Event(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=255)
    announce = models.CharField(verbose_name=u'Анонс', max_length=255, blank=True)
    date = models.DateField(verbose_name=u'Дата')
    date_end = models.DateField(verbose_name=u'Дата до', null=True, blank=True)
    objects = CustomManager()

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

    def __unicode__(self):
        return self.title










