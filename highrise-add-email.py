#!/usr/bin/env python

from highriseutils import *
import sys

if len(sys.argv) < 3:
    print "Usage: " + sys.argv[0] + " <email address> <subject>"
    sys.exit(1)

config_highrise(get_config())

email_address = sys.argv[1]
subject = sys.argv[2]
body = "".join(sys.stdin.readlines())

for person in Person.filter(email=email_address):
    email = Email()
    email.title = subject
    email.body = body
    email.subject_type = 'Party'
    email.subject_id = person.id
    email.save()

