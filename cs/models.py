# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Finalyearstudents(models.Model):
    PRIORITIES = (
        (0, 'I year'),
        (1, 'II year'),
        (2, 'III year')
    )
    studentname=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    state = models.CharField(max_length=155)
    priority = models.IntegerField(choices=PRIORITIES, default=1)
    assignee = models.TextField( )
    studentmail = models.EmailField()
    message_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ##attachments = GenericRelation(MailAttachment)

##    def publish(self):
##        self.save()
##
##    def __str__(self):
##        return self.studentname
