#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from huey import crontab

from config import huey
from app import do_request


@huey.periodic_task(crontab(minute='*/15'))
def flood_site():
    do_request()
