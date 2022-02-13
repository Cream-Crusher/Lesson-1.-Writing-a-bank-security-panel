import datetime
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def check_duration(duration, hour=datetime.timedelta(hours=1)):

    if duration > hour:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    owner_names = Passcard.objects.all()

    for owner_name in owner_names:
        
        passcards_information = Visit.objects.filter(passcard=owner_name)
        this_passcard_visits = []

        for passcard_information in passcards_information:

            duration = passcard_information.get_duration()
            entered_at = passcard_information.entered_at

            this_passcard_visits.append(
                {
                    'entered_at': entered_at,
                    'duration': duration,
                    'is_strange': check_duration(duration)
                },
            )

        context = {
        'passcard': owner_name,
        'this_passcard_visits': this_passcard_visits
            }

    return render(request, 'passcard_info.html', context)
