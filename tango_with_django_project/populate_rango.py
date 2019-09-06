import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')


import django
django.setup()


from rango.models import Category, Page


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/2/tutorial/'},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokitthakis.net/tutorials/python/'}
    ]

    django_pages = [
        {'title': 'Official django Tutorial', 'url': 'https://docs.djangoproject.com/en/1.9/intro/tutorial01/'},
        {'title': 'Django Rocks','url': 'http://www.diangorocks.com/'},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/'}
    ]

    others_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org'}
    ]

    cats = {
        {'Python': {'pages': python_pages}, 'views': 128, 'likes': 64},
        {'Django': {'pages': django_pages}, 'views': 64, 'likes': 32},
        {'Others': {'pages': others_pages}, 'views': 32, 'likes': 16},
    }

    for cat, views, likes, cat_data in cats.items():
        c = add_cat(cat, views, likes)

        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

        for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print('- {0} - {1}'.format(str(c), str(p)))


def add_page(cat, title, url, views=0, likes=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views

    p.save()


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c = Category.objects.get_or_create(views=views)[0]
    c = Category.objects.get_or_create(likes=likes)[0]

    c.save()

    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()