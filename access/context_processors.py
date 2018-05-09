from access.models import Item


def item(request):
    all_item = Item.objects.all()

    return {
        'item': all_item,
    }





