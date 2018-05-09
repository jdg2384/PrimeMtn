from womens.models import Wost


def wost(request):
    all_wost = Wost.objects.all()

    return {
        'wost': all_wost,
    }





