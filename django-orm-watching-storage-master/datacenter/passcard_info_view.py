import datetime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def get_duration(leaved_at, entered_at, hour=datetime.timedelta(hours=1)):

    duration_visit = (leaved_at - entered_at)

    if duration_visit > hour:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all()
    # Программируем здесь
    context = []
    Visits = Visit.objects.all()
    non_closed_visits = Visits.filter(leaved_at=None)


    for non_closed_visits in non_closed_visits:
        passcard_visits = Visits.filter(passcard=non_closed_visits.passcard)
        this_passcard_visits = []

        for passcard_visit in passcard_visits:
            #entered_at = passcard_visit.passcard.entered_at
            #leaved_at = passcard_visit.passcard.leaved_at

            #if entered_at != None:
            #    duration = get_duration(leaved_at, entered_at)

            this_passcard_visits.append(
                {
                    'entered_at': passcard_visit.passcard.owner_name,
                    'duration': '25:03',
                    'is_strange': 1#duration
                },
            )

        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
        return render(request, 'passcard_info.html', context)
