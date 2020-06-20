#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午1:10
# @Author  : li xin song
# @Email   : li-xin-song@foxmail.com
# @File    : __init__.py


from flask import Flask

from apps.demo import bp
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(bp)

    return app