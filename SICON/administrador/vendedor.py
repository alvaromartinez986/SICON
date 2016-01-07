__author__ = 'JuanDiego'
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from .empleado import *


class Vendedor(User, Empleado):
    pass
