# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


class RegisterNotFound(Exception):

    def __init__(self):
        super().__init__("Register does not exist.")
