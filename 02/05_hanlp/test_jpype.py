# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 11:38 PM
# @Author  : alpface
# @Email   : xiaoyuan1314@me.com
# @File    : test_jpype.py
# @Software: PyCharm

import jpype

if __name__=='__main__':

    print('测试java环境和jpype的环境')

    # 获取系统的jvm路径
    jvm_path = jpype.getDefaultJVMPath()
    # 设置jvm路径，以启动java虚拟机
    jpype.startJVM(jvm=jvm_path)
    # 执行java代码
    jpype.java.lang.System.out.println('hello world')
    # 关闭jvm虚拟机，当使用完 JVM 后，可以通过 jpype.shutdownJVM() 来关闭 JVM，该函数没有输入参数。当 python 程序退出时，JVM 会自动关闭。
    jpype.shutdownJVM()
