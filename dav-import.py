from datetime import datetime
import caldav
import json
import re
from caldav.elements import dav, cdav


def get_caldav_url(filename):
    with open(filename) as credit_file:
        credits = json.loads(credit_file.read())
        username = credits['username']
        password = credits['password']
        # for sure there is something better than regex to split the url, but for the sake of fun :D
        url = re.search('(http[s]?:\/\/)(.*)', credits['url'])
    return "{}{}:{}@{}".format(url.group(1), username, password, url.group(2))


url = get_caldav_url('res/credits')

client = caldav.DAVClient(url)
principal = client.principal()
calendars = principal.calendars()

if len(calendars) > 0:
    events = calendars[0].events()
    print(calendars[0].name)

    if len(events) > 0:
        for event in events:
            print(event.data)

print("\n\nDone")
