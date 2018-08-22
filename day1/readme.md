登录程序
1.输入用户名密码
2.认证成功后显示欢迎信息
3.输错三次后锁定


1.[输入正确的用户名和密码]
[root@shell_python ~]# python welcome.py
请输入用户名:zhangxiaoyu
请输入密码:
登录成功！欢迎zhangxiaoyu登录系统!
######当输入正确的用户名和密码打印登录成功和欢迎信息！


2.[输入错误的用户名]
[root@shell_python ~]# python welcome.py
请输入用户名:nouser
请输入密码:
用户nouser不存在,请重新输入:
请输入用户名:
#######当输入错误的用户名和密码(正确或者不正确或为空)提示用户不存在请重新输入！


3.[输入正确的用户名和错误的密码]
[root@shell_python ~]# python welcome.py
请输入用户名:zhangxiaoyu
请输入密码:
密码错误,还剩2次机会,超出次数账号将被锁定！
请输入用户名:zhangxiaoyu
请输入密码:
密码错误,还剩1次机会,超出次数账号将被锁定！
请输入用户名:zhangxiaoyu
请输入密码:
密码错误次数达到三次，该用户已被锁定！请联系系统管理员解锁!
#######当输入正确的用户名和错误的密码提示密码错误，并提示输入密码错误三次此账户将被锁定！


4.[输入被锁定的用户]
[root@shell_python ~]# python welcome.py
请输入用户名:zhangxiaoyu
请输入密码:
用户zhangxiaoyu已被锁定，请联系系统管理员解锁!
#######当输入已经被锁定的用户时，提示该用户已被锁定，请联系系统管理员解锁!


5.[查看被锁定的用户]
[root@shell_python ~]# cat locked.txt 
zhangxiaoyu
#######凡是加入到此锁定文件的用户均不能登录系统！



