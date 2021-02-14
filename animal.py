#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Time ： 2021/02/13 14:00
@Auth ： luoluo
@File ：animal.py
@Description：
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），
类方法（会叫，会跑）创建子类【猫】，继承【动物类】
"""


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        print(f'动物的名字叫{self.name}，'
              f'颜色是：{self.color},'
              f'年龄是：{self.age},'
              f'性别是：{self.gender}')

    def shout(self):
        print(f'{self.name} 会叫')

    def run(self):
        print(f'{self.name} 会跑')


if __name__ == '__main__':
    cat = Animal('咪咻', '白色', 8, '母')
    cat.shout()
    cat.run()

