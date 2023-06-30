from django.shortcuts import render

# Create your views here.


def blog(request):
    print('blog')

    context = {
        'text': 'Estamos no blog..'
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Estamos no exemplo.',
        'title': 'Essa é uma página de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
