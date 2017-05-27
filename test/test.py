# -*- coding: utf-8 -*-
from pprint import pprint
import sys

myPath = "D:/jfpstorage/Publish/team_dennis/assets/Pipeline"
if myPath not in sys.path:
    sys.path.append(myPath)

import sanity_checks.geom_checks
print sys.path[-1]
pprint (sys.path)
pprint (sys.modules)

t = sanity_checks.geom_checks.TestCheck()
print dir(t)
print t.__module__
print "sys.modules[",t.__module__,"].__file__:", sys.modules[t.__module__].__file__
# pprint (dir(sys.modules[t.__module__]))

# pprint (dir(sys.modules))