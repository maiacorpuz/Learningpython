#!/usr/bin/python
import re
phone = "602-343-8747 "
num = re.sub(r'#.*s', "", phone)
print "Phone Num : ", num
num = re.sub(r'D', "", phone)
match = re.search(r'602', phone)
if match:
    print ' The area code is:', match.group ()
else:
    print 'did not find'
