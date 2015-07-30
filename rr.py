import commands
import re
(s, o) = commands.getstatusoutput("lsof -i:8000")
path = "/Users/xdy/demo/jango_test/d1.3/xdyutils"
if s == 0:
    i = o.index("python")
    e = o.index("xdy")
    o = o[i+6:e]
    (ss, oo) = commands.getstatusoutput("kill %s"%(o,))
    if ss == 0:
        print("kill %s success"%(o,))
        # (sss,ooo) = commands.getstatusoutput("cd "+path+";python manage.py runserver")
        # print("restart uwsgi")
