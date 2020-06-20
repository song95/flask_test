#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 下午8:03
# @Author  : li xin song
# @Email   : li-xin-song@foxmail.com
# @File    : manage.py

import os

from apps import create_app

env = os.environ.get("FLASK_ENV", "default")

app = create_app(env)


if __name__ == '__main__':
    app.run()
