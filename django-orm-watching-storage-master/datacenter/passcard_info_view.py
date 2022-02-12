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

    for owner_name in passcard:

        passcard_visits = Visit.objects.filter(passcard=owner_name)
        this_passcard_visits = []

        for visit in passcard_visits:

            duration = visit.get_duration()
            entered_at = visit.entered_at

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
