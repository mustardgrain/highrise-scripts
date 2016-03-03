#!/usr/bin/env python

from highriseutils import *

config_highrise(get_config())

for t in Tag.all():
    print(str(t.id) + "-" + t.name)
    
