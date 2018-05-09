from mens.models import Most


def most(request):
    all_most = Most.objects.all()

    return {
        'most': all_most,
    }





