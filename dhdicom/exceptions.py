# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


class RegisterNotFound(Exception):

    def __init__(self):
        msg = "Register does not exist."
        super().__init__(msg)