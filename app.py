#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from random import randint, choice
from string import ascii_letters, digits, punctuation

import requests


def generate_user_agents():
    users_agents = {
        0: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        1: 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
        2: 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
        3: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        4: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
        5: 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        6: 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)',
    }

    index = randint(0, len(users_agents) - 1)

    return users_agents.get(index)


def generate_headers():
    return {'User-Agent': generate_user_agents()}


def generate_data():
    to_acc = ascii_letters + digits
    min_char_acc = 6
    max_char_acc = 20
    acc = "".join(choice(to_acc) for x in range(randint(min_char_acc, max_char_acc)))

    to_pass = ascii_letters + digits + punctuation
    min_char_pass = 6
    max_char_pass = 29
    pass_ = "".join(choice(to_pass) for x in range(randint(min_char_pass, max_char_pass)))

    token = "".join(choice(to_pass) for x in range(randint(min_char_pass, max_char_pass)))

    return {
        'loginname': acc,
        'loginpassword': pass_,
        'token': token
    }


def do_request(url='https://igaodocs.000webhostapp.com/dados.php'):
    headers = generate_headers()
    data = generate_data()
    try:
        requests.post(url, data=data, headers=headers, timeout=10)
    except requests.exceptions.ReadTimeout:
        pass
