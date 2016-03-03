#!/usr/bin/env python

from highriseutils import *
import sys

if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " <old tag> <new tag>"
    sys.exit(1)

config_highrise(get_config())

old_tag = sys.argv[1]
new_tag = sys.argv[2]
old_tag_id = -1

for t in Tag.all():
    if t.name == old_tag:
        old_tag_id = t.id

if old_tag_id == -1:
    print "Could not find ID for " + old_tag
    sys.exit(1)

for p in Person.all():
    tags = [tag.name for tag in p.tags]

    if old_tag in tags and new_tag in tags:
        p.remove_tag(old_tag_id)
        p.save()
        print(p.first_name + " " + p.last_name + " had both, removed " + old_tag)
    
