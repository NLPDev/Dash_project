import vobject
import ics
import datetime

data = open("calendar.ics").read()

result_list = []

a = 1

# <class 'vobject.icalendar.RecurringComponent'>

for cal in vobject.readComponents(data):
    for component in cal.components():
        result_val = {}
        if component.name:
            result_val['name'] = component.name
            if hasattr(component, 'dtstart'):
                result_val['start'] = component.dtstart.valueRepr()

            if hasattr(component, 'dtend'):
                result_val['end'] = component.dtend.valueRepr()
                if hasattr(component, 'dtstart'):
                    duration = result_val['end'] - result_val['start']
                    result_val['duration'] = duration.seconds

            if hasattr(component, 'attendee'):
                result_val['attendees'] = component.attendee.valueRepr()

                a = 0

                print(component.get('attendee'))

            if hasattr(component, 'description'):
                result_val['description'] = component.description.valueRepr()

            if hasattr(component, 'location'):
                result_val['location'] = component.location.valueRepr()

            result_list.append(result_val)
            # print(component.__dict__)

            if a == 0:
                # print(result_val)
                break

    if a == 0:
        break

# print(result_list)