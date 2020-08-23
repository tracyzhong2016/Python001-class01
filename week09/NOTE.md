学习笔记

django源码
1. urlconf-url调度器
python 标准库 partial： 固定函数的参数
https://docs.python.org/zh-cn/3.7/library/functools.html#functools.partial
偏函数的例子， 二进制转换

注意事项：
partial第一个参数必须是可调用对象
参数传递顺序是从左到右，但不能超过原函数个数
关键字参数会覆盖原函数中定义好的参数


2.include函数
# site-packages/django/urls/conf.py
加载子项目中的urlpattern

3. 请求与响应
HttpRequest 创建与 HttpResponse 返回是一次 HTTP 请求的标准行为

HttpRequest 常用的属性和方法
https://docs.djangoproject.com/zh-hans/2.2/ref/request-response/#django.http.HttpRequest

self.GET = QueryDict(mutable=True)
QueryDict的使用方法

HttpResponse
https://docs.djangoproject.com/zh-hans/3.0/ref/request-response/#django.http.HttpResponse
# 使用HttpResponse的子类
# 使用HttpResponseNotFound

4. Model 要继承 models.Model 
• 不需要显式定义主键
• 自动拥有查询管理器对象
• 可以使用 ORM API 对数据库、表实现 CRUD

5.
model模型的自增主键
元类的应用
 def __new__(cls, name, bases, attrs, **kwargs):
        super_new = super().__new__
 def add_to_class(cls, name, value):
     #添加_meta属性
 new_class._prepare()
6. model模型的查询管理器
# site-packages/django/db/models/manager.py
Manager 继承自 BaseManagerFromQuerySet 类，拥有 QuerySet 的大部分方法， get、create、filter 等方法都来自 QuerySet

7. 模版引擎

8. DjangoWeb相关功能
管理界面
 'django.contrib.admin' 在inatalled app中加载
 # 注册模型
admin.site.register(Type) 
admin.site.register(Name)
官方文档中提供了很多样式

9。表单
<form action="result.html" method="post">
username:<input type="text" name="username" /><br> password:<input type="password" name="password" /> <br> <input type="submit" value="登录">
</form>

表单与内部auth功能结合
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('tom', 'tom@tom.com', 'tompassword') >>> user.save()
>>> from django.contrib.auth import authenticate
>>> user = authenticate(username='tom', password='tompassword’)

10。信号
多个独立程序对某一事件感兴趣
信号:
• 发生事件，通知应用程序
• 支持若干信号发送者通知一组接收者 
• 解耦

应用：
 对请求，migrate,module进行操作，希望操作前后进行处理， 例如日志打印，功能拦截，
 
11. 中间件
django请求和响应中间做一些拦截

12. 生产环境部署
# 安装gunicorn
pip install gunicorn
# 在项目目录执行
gunicorn MyDjango.wsgi

13。定时运行任务

celery 分布式消息队列

14。
 Flask的上下文与信号
上下文:  request上下文与session 上下文 
信号:  Flask 从 0.6 开始，通过 Blinker 提供了信号支持 
pip install blinker

15。
Tornado 的同步 IO 与异步 IO:
• http_client = HTTPClient()
• http_client = AsyncHTTPClient()


