from pet.models import Woof


def woof(request):
    all_woof = Woof.objects.all()

    return {
        'woof': all_woof,
    }





