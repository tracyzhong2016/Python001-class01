学习笔记

1. 显示 Object 类的所有子类 print( ().class.bases[0].subclasses() ) () # tuple ().class # <class 'tuple'> ().class.bases # <class 'object'> # 父类 ().class.bases[0].subclasses() # 父类下所有子类
2.  可以用class.__dict__   dir(class) 来查看类所带的属性。
    实例占不用的内存，对一个实例的属性进行修改 不会影响另一个。
3.作为构造函数使用，classmethod的两大应用场景： 1）函数需要调用类并返回类的时候   2）父类中定义classmethod，子类需要根据自己的变量名去发生变化的时候
4.staticmethod：定义和类或实例相关的功能，又不需要使用到类或实例的属性；常用于类型转换、条件判断等
5. 实例获取属性，__getattribute__() 对所有属性的访问都会调用该方法， 拦截变量的赋值
6. 实例获取属性，__getattr__() 适用于未定义的属性
7. @property 可以把方法封装成属性
8.继承机制 MRO
MRO 采用 C3 算法
Subclass.mro() 查看继承链顺序
于有向无环图类似：
DAG（Directed Acyclic Graph）
DAG 原本是一种数据结构，因为 DAG 的拓扑结构带来的优异特性，经常被用于处理动态规划、寻求最短路径的场景。
9.SOLID 设计原则
单一责任原则 The Single Responsibility Principle ： 职责越多，复杂度越高，职责过多时，大类拆小类
开放封闭原则 The Open Closed Principle：如果有新的功能，应该新增而不是修改，比如引入 @classmethod
里氏替换原则 The Liskov Substitution Principle：要求子类必须完整覆盖父类的所有方法
依赖倒置原则 The Dependency Inversion Principle：高层模块不应该依赖低层模块，如果有依赖必须建立两者之间的抽象，进行解耦
接口分离原则 The Interface Segregation Principle：接口是模块之间相互交流的抽象协议，一个接口的方法应该是模块刚好需要的
10.工厂模式
静态工厂模式创建方法
动态工厂模式创建方法
11.元类：
元类是创建类的类，是类的模板
元类是用来控制如何创建类的，正如类是创建对象的模板一样
元类的实例为类，正如类的实例为对象
创建元类的两种方法 1.class 2.type
type：类名，父类的元祖，包含属性的字典
12.Mixin 模式：
在程序运行过程中，重定义类的继承，即动态继承。好处：
可以在不修改任何源代码的情况下，对已有类进行扩展
进行组件的划分
