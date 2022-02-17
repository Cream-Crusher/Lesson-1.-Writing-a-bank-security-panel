import datetime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def check_duration(duration, hour=datetime.timedelta(hours=1)):

    return duration > hour


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:

        duration = visit.get_duration()
        entered_at = visit.entered_at

        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': check_duration(duration)
            },
        )

    context = {
    'passcard': passcard,
    'this_passcard_visits': this_passcard_visits
        }

    return render(request, 'passcard_info.html', context)
