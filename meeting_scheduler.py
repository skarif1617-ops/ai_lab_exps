busy_schedules = {                         # known busy slots for each person
    'Person A': [('Monday', '10AM'), ('Wednesday', '2PM')],
    'Person B': [('Monday', '10AM'), ('Friday', '3PM')],
    'Person C': [('Thursday', '2PM')],
    'Person D': [('Monday', '10AM'), ('Wednesday', '2PM')],
    'Person E': [('Friday', '3PM'), ('Thursday', '2PM')],
}

default_slots = [                          # candidate (day, time, place) options
    ('Monday', '10AM', 'Conference Room A'),
    ('Tuesday', '11AM', 'Conference Room B'),
    ('Wednesday', '2PM', 'Conference Room C'),
    ('Thursday', '2PM', 'Conference Room D'),
    ('Friday', '3PM', 'Conference Room E'),
]

def find_meeting_slot():
    for day, time, place in default_slots:         # try slots in order
        conflict = False
        for schedule in busy_schedules.values():   # check every person
            if (day, time) in schedule:            # known to be busy then
                conflict = True
                break                              # no need to check others
        if not conflict:                           # default: free unless proven busy
            return day, time, place
    return None                                    # no slot works for everyone

meeting = find_meeting_slot()
if meeting:
    day, time, place = meeting
    print("Meeting Scheduled Successfully!")
    print(f"Day:   {day}")
    print(f"Time:  {time}")
    print(f"Place: {place}")
else:
    print("No common time slot available.")