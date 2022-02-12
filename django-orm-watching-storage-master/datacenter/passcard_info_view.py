import datetime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def get_duration(duration, hour=datetime.timedelta(hours=1)):

    if duration > hour:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()
    '''    
    visits = Visit.objects.all()

    for owner_name in passcard:

        passcard_visits = visits.filter(passcard=owner_name)

        duration = Visit().get_duration()
        this_passcard_visits = []

        for passcard_visit in passcard_visits:'''

    
    visits = Visit.objects.all()
    this_passcard_visits = []

    for owner_name in passcard:

        passcard_visits = visits.filter(passcard=owner_name)

    for visit in passcard_visits:
        duration = visit.get_duration()
        entered_at = visit.entered_at
        owner_name = visits.filter(passcard=passcard[1])

        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': get_duration(duration)
            },
        )

    context = {
    'passcard': owner_name,
    'this_passcard_visits': this_passcard_visits
        }

    return render(request, 'passcard_info.html', context)
