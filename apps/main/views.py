#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午2:24
# @Author  : li xin song
# @Email   : li-xin-song@foxmail.com
# @File    : views


from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
def index():
    return render_template("index.html",)
