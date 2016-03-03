#!/usr/bin/env python

from highriseutils import *

config_highrise(get_config())

def strip(name, suffix):
    if name.upper().endswith(suffix.upper()):
        name_len = len(name)
        suffix_len = len(suffix)
        new_len = name_len - suffix_len
        return name[0:new_len].rstrip(',. ')
    else:
        return name

for c in Company.all():
    p = Person.filter(company_id=c.id)

    if len(p) == 0:
        c.delete()
        print(c.name + " has no contacts, deleted")
        continue

    new_name = strip(c.name, "Inc.")
    new_name = strip(new_name, "Inc")
    new_name = strip(new_name, "Systems")
    new_name = strip(new_name, "LLC")

    if len(new_name) > 24:
        print(new_name + " is too long")

    if new_name != c.name:
        old_name = c.name
        c.name = new_name
        c.save()
        print(old_name + " changed to " + new_name)
