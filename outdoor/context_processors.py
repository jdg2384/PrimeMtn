from outdoor.models import Post


def post(request):
    all_post = Post.objects.all()

    return {
        'post': all_post,
    }