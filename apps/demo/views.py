#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午1:19
# @Author  : li xin song
# @Email   : li-xin-song@foxmail.com
# @File    : views


from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/')
def test():
    return 'hello'

