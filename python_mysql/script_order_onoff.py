import sys
sys.path.append("..")
import _python_email
import _python_redis


alist = _python_redis.getOnOff()
_python_email.sendmail(alist[0], alist[1], alist[2])
