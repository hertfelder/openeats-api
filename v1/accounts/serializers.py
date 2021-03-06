#!/usr/bin/env python
# encoding: utf-8

from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Standard `rest_framework` ModelSerializer """
    class Meta:
        model = User
        fields = '__all__'
