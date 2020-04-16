from icalendar import Calendar, Event, vDDDTypes, vCalAddress
g = open('calendar.ics','rb')
gcal = Calendar.from_ical(g.read())

result_list = []

for event in gcal.walk('vevent'):
    each_val = {}
    if event.get('name'):
        each_val['name'] = event.get('name')

    each_val['start'] = event.get('dtstart').dt

    if event.get('dtend'):
        each_val['end'] = event.get('dtend').dt

    if event.get('dtend'):
        duration = each_val['end'] - each_val['start']
        each_val['duration'] = duration.seconds

    if event.get('status'):
        each_val['status'] = event.get('status')


    if event.get('description'):
        each_val['description'] = event.get('description')

    if event.get('location'):
        each_val['location'] = event.get('location')

    each_val['attendees'] = []
    attendees = event.get('attendee')

    if attendees:
        for each_attendee in attendees:
            each_val['attendees'].append(each_attendee)

    result_list.append(each_val)

print(result_list)