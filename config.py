#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from huey.contrib.sqlitedb import SqliteHuey

huey = SqliteHuey('tibia-flooder', filename='huey.db')