from special.models import Enter


def enter(request):
    all_enter = Enter.objects.all()

    return {
        'enter': all_enter,
    }