import sys
import os
import ConfigParser
from pyrise import *

def contains(list, filter):
    for x in list:
        if filter(x):
            return True

    return False

def get_config():
    config_file_name = os.getenv("HOME") + "/.highrise.conf"

    if not os.path.isfile(config_file_name):
        print "Please create " + config_file_name
        sys.exit(1)

    config = ConfigParser.ConfigParser()
    config.read(config_file_name)
    return config

def config_highrise(config):
    server = config.get('server', 'company_id')
    auth_token = config.get('server', 'auth_token')

    Highrise.set_server(server)
    Highrise.auth(auth_token)

def print_contact_header():
    max_name = 32
    max_title = 48
    max_company = 24
    max_email = 48

    print "Name".ljust(max_name) + "    " + "Title".ljust(max_title) + "    " + "Company".ljust(max_company) + "    " + "Email".ljust(max_email) + "    " + "Tags"

def print_contact(c):
    max_name = 32
    max_title = 48
    max_company = 24
    max_email = 48

    print c.name.ljust(max_name) + "    " + c.title.ljust(max_title) + "    " + c.company.ljust(max_company) + "    " + c.email.ljust(max_email) + "    " + ", ".join(c.tags)

def get_email(p):
    if len(p.contact_data.email_addresses) == 0:
        return ""
    else:
        return p.contact_data.email_addresses[0].address

def get_company_name(company_id):
    company_name = ""

    if company_id:
        company = Company.get(company_id)

        if company:
            company_name = company.name

    return company_name

class Contact:

    def __init__(self, name, title, company, email, tags):
        self.name = name
        self.title = title
        self.company = company
        self.email = email
        self.tags = tags
