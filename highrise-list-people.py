#!/usr/bin/env python

from highriseutils import *

config_highrise(get_config())

print_contact_header()

for p in Person.all():
    title = p.title
    company_name = get_company_name(p.company_id)
    email = get_email(p)
    tags = [tag.name for tag in p.tags]
    c = Contact(p.first_name + " " + p.last_name, title, company_name, email, tags)
    print_contact(c)

