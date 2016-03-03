#!/usr/bin/env python

from highriseutils import *
import sys
import signal

def signal_handler(signal, frame):
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

match_tags = []

if len(sys.argv) > 1:
    match_tags = list(set(sys.argv[1:len(sys.argv)]))

config = get_config()
config_highrise(config)

remind_tag_id = -1

for t in Tag.all():
    if t.name == "remind":
        remind_tag_id = t.id
        break

def set_tag(p, check_datetime):
    tags = [tag.name for tag in p.tags]

    if not "remind" in tags:
        print p.first_name + " " + p.last_name + " has had no activity since " + str(check_datetime)
        p.add_tag("remind")

def clear_tag(p, check_datetime):
    tags = [tag.name for tag in p.tags]
    if "remind" in tags:
        if remind_tag_id != -1:
            print p.first_name + " " + p.last_name + " has activity since " + str(check_datetime)
            p.remove_tag(remind_tag_id)

def check_comments(messages, check_datetime):
    for m in messages: 
        if m.comments:
            comments = sorted(m.comments, key=lambda x: x.created_at)

            if contains(comments, lambda x: x.created_at > check_datetime):
                return True

    return False

for p in Person.all():
    tags = [tag.name for tag in p.tags]

    # If we're matching tags, make sure we match all of them
    if len(match_tags) > 0:
        matches = list(set(match_tags) & set(tags))

        if len(matches) != len(match_tags):
            continue

    num_days = 365

    for tag in tags:
        if not config.has_option('reminderdays', tag):
            continue
           
        n = config.getint('reminderdays', tag)
        num_days = min(n, num_days)

    # If num_days is less than zero, skip intentionally
    if num_days < 0:
        continue

    check_datetime = datetime.now() - timedelta(days=num_days)

    emails = sorted(Email.filter(person=p.id), key=lambda x: x.created_at)

    if contains(emails, lambda x: x.created_at > check_datetime):
        clear_tag(p, check_datetime)
        continue

    if check_comments(emails, check_datetime):
        clear_tag(p, check_datetime)
        continue

    notes = sorted(Note.filter(person=p.id), key=lambda x: x.created_at)

    if contains(notes, lambda x: x.created_at > check_datetime):
        clear_tag(p, check_datetime)
        continue

    set_tag(p, check_datetime)
