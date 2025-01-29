import os
# 设置Django项目的设置模块环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
# 导入Django并进行初始化
django.setup()

from rango.models import Category, Page


def populate():
    # 首先，我们将创建包含要添加到每个类别的页面的字典列表。
    # 然后，我们将创建类别的字典列表。
    # 这虽然有点复杂，但它允许我们通过每条数据记录迭代并将数据添加到模型中。
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views':100},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views':80},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views':60}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views':60},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views':110},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views':10}
    ]

    other_pages = [
        {'title': 'bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views':30},
        {'title': 'flask',
         'url': 'http://flask.pocoo.org/',
         'views':80}
    ]

    cats = {
        'Python': {'pages': python_pages,'views':64,'likes':128},
        'Django': {'pages': django_pages,'views':32,'likes':64},
        'Other Frameworks': {'pages': other_pages,'views':32,'likes':16}
    }
    #  #If youwanttoaddmorecategories orpages,
    # #addthem tothe dictionariesabove.

    # 遍历类别字典，对于每个类别名称，调用add_cat函数创建或获取类别对象c
    # 接着遍历该类别对应的页面列表，对于每个页面信息，调用add_page函数将页面添加到对应的类别下
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])#!!!***不确定***!!!
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'],p['views'])#把页面浏览量传入add_page函数

    # 遍历所有的类别对象
    for c in Category.objects.all():
        # 对于每个类别，遍历其对应的页面对象
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    # 尝试获取或创建一个Page对象，[0]是因为get_or_create返回一个元组，第一个元素是对象
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name,views=0,likes=0):
    # 尝试获取或创建一个Category对象，[0]是因为get_or_create返回一个元组，第一个元素是对象
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    c.save()
    return c


# 开始执行的地方！
# 如果模块作为主程序运行（即不是被其他模块导入），__name__会被赋值为'__main__'，此时执行下面代码块
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()