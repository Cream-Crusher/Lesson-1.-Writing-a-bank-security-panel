from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:

        duration = visit.get_duration()
        entered_at = visit.entered_at
        is_strange = visit.check_duration()

        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_strange
            },
        )

    context = {
    'passcard': passcard,
    'this_passcard_visits': this_passcard_visits
        }

    return render(request, 'passcard_info.html', context)
