# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    vk_id = models.IntegerField(default=1)
    name = models.CharField(max_length=24, blank=True, null=True, default=None)

    def __unicode__(self):
        return u"%s, %s" % (self.vk_id, self.name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        self.name = vkApiTest(self.id)

        super(User, self).save( *args, **kwargs)
