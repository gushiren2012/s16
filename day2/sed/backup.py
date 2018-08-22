#!/usr/bin/env python
#auto backup system files
#by authors rain 2017
import os,time,sys
d_dir='/data/backup/'
d_file='system_back.tar.gz'
s_dir=['/etc/','/boot/','/var/www/html/']
date=time.strftime('%Y%m%d')
r_dir = d_dir + date + '/'
r_name = r_dir + d_file

def all_bak():
        print 'backup scripts start,please wait....'
        print '\033[32m--------------------------------------\033[0m'
        time.sleep(3)
        if os.path.exists(d_dir) == False:
                os.makedirs(r_dir)
                print 'The DIR %s is create success!' % r_dir
        else:
                print 'The DIR %s is exists!' % r_dir
        tar_cmd = 'tar -zcvf %s %s ' % (r_name,' '.join(s_dir))
        if os.system(tar_cmd) == 0:
                print '\033[32mthe backup files %s exec successful!\033[0m' % r_name
        else:

                print 'the backup files is  failed!'
try:
        if len(sys.argv[1]) == 0:
                pass
except IndexError:
                print '\033[32m--------------------------------------\033[0m'
                print
                print '\033[34mUsage: {Please Exec %s help|all_bak}\033[0m' % sys.argv[0]
try:
        if sys.argv[1] == 'all_bak':
                all_bak()
        else:
                print 'rain'
except IndexError:
                pass