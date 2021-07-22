#! /usr/bin/python
#
# Copyright (C) 2021 paradox.ai
#
# Release: 1.0
# @link olivia.paradox.ai
#
__author__ = "thong.tran@paradox.ai"
__date__ = "21/07/2021"

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
