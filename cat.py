#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time ： 2021/02/13 14:00
@Auth ： luoluo
@File ：cat.py
@Description：
重写父类的 Animal 的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""
from pyton_oop.animal import Animal


class Cat(Animal):
    def __init__(self):
        # 重写父类的__init__方法，继承父类的属性
        super().__init__('咪咻')
        # 子类添加一个新的属性：毛发 = 短毛
        self.hair = 'short hair'
        print(f'毛发是：{self.hair}')

    # 子类添加一个新的方法：会捉老鼠
    def catch_mice(self):
        print(f'{self.name}会捉老鼠')

    # 重写父类的【会叫】的方法，改成【喵喵叫】
    def shout(self):
        print(f'{self.name}会喵喵叫')


if __name__ == '__main__':
    cat = Cat()
    cat.catch_mice()
    cat.shout()
