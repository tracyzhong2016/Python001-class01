# coding: utf-8
"""
#作业一：
容器序列: list, tuple, dict
扁平序列: str, collections.deque
可变序列: list, dict
不可变序列: str, tuple, collections.deque
"""

#作业二
def f_map(func, iter_list):
    for i in iter_list:
        yield func(i)

#作业三
import time
def timer(func,*args,**kwargs):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f'{func.__name__}运行时间: {end_time - start_time}')
    return wrapper

@timer
def test1():
    print('test')


