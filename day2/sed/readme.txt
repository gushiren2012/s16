可以替换文件中的字段

[root@shell_python sed]# python sed.py backup.py /var/www/html/ zhangxiaoyu

[root@shell_python sed]# cat backup.py 
s_dir=['/etc/','/boot/','zhangxiaoyu']

[root@shell_python sed]# python sed.py backup.py zhangxiaoyu  test

[root@shell_python sed]# cat backup.py 
s_dir=['/etc/','/boot/','test']
