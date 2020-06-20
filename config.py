#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 上午1:07
# @Author  : li xin song
# @Email   : li-xin-song@foxmail.com
# @File    : config


def get_db_uri(db_info: dict):
    engine = db_info.get("ENGINE")
    driver = db_info.get("DRIVER")
    user = db_info.get("USER")
    password = db_info.get("PASSWORD")
    host = db_info.get("HOST")
    port = db_info.get("PORT")
    name = db_info.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config(object):
    TESTING = False

    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def init_app(cls, app):
        pass


class DevelopConfig(Config):
    DEBUG = True

    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "NAME": "test"
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


config = {
    "development": DevelopConfig,
    "default": DevelopConfig
}
