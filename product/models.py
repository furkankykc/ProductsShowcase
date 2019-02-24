from django.db import models


# Create your models here.


def getTemplates():
    from django.conf import settings
    import os

    template_path = settings.TEMPLATES[0]['DIRS'][0]

    templates = os.listdir(template_path)

    return zip(templates, templates)


#
# def getUrls():
#     from product import urls
#
#     name = [o.name for o in urls.urlpatterns]
#     url= [o.pattern._route for o in urls.urlpatterns]
#     return zip(name,url)


class Product(models.Model):
    name = models.CharField(max_length=15)
    about = models.CharField(max_length=20)


class PricingPlan(models.Model):
    type = models.CharField(max_length=15)
    price = models.IntegerField()
    time = models.CharField(max_length=15)
    COLORS = (
        ('green', 'Green'),
        ('red', 'Red'),
        ('yel', 'Yellow'),
        ('blue', 'Blue'),
        ('white', 'White')

    )
    color = models.CharField(max_length=10, choices=COLORS, default='white')

    def __str__(self):
        return self.type

    @property
    def predictedPrice(self):
        # 10% taxes
        return int(self.time) * 500


class DropDown(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=20, default='/')
    items = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class NavItem(models.Model):
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=20, default='/')
    desc = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Navbar(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20, default='default')
    template = models.CharField(max_length=20, choices=getTemplates(), default='default.html')
    item = models.ManyToManyField(NavItem, null=True)
    dropdown = models.ManyToManyField(DropDown, null=True)

    def __str__(self):
        return self.name


class SliderItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200, default='/')
    short_desc = models.CharField(max_length=50)
    button_text = models.CharField(max_length=50, default='default')
    desc = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.name

    @property
    def url(self):
        return self.image.url


class Slider(models.Model):
    name = models.CharField(max_length=15)
    template = models.CharField(max_length=20, choices=getTemplates(), default='default.html')
    images = models.ManyToManyField(Image)
    mainImage = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='img')
    item = models.ManyToManyField(SliderItem)

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name


class Footer(models.Model):
    name = models.CharField(max_length=15)
    template = models.CharField(max_length=20, choices=getTemplates(), default='default.html')
    links = models.ManyToManyField(Link)

    def __str__(self):
        return self.name


# def getModels():
#     model_List=[]
#     for model_name in dir():
#         model = getattr(models, model_name)
#         if isinstance(model, ModelBase):
#             model_List.append(model_name)
#     return model_List
#


class Contact(models.Model):
    name = models.CharField(max_length=15)
    skype = models.CharField(max_length=15)
    facebook = models.CharField(max_length=15)
    instagram = models.CharField(max_length=15)
    website = models.CharField(max_length=15)
    about = models.CharField(max_length=500)
    picture = models.ImageField()

    def __str__(self):
        return self.name

    @property
    def instagramURL(self):
        # 10% taxes
        return "http://www.instagram.com/{}".format(self.instagram)


class Components(models.Model):
    template = models.CharField(max_length=20, choices=getTemplates(), default='default.html')
    name = models.CharField(max_length=15)

    model = models.CharField(max_length=20, null=True)

    class Meta:
        abstract = False  # <--- denotes our model as abstract

    def __str__(self):
        return self.name


class Seo(models.Model):
    name = models.CharField(max_length=50)
    locale = models.CharField(max_length=10, default='')
    description = models.TextField(max_length=170, default='')

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=70, default='')
    seo = models.ForeignKey(Seo, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=70, default='')
    publisher = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
    template = models.CharField(max_length=20, choices=getTemplates(), default='default.html')
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True)
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, null=True)
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, null=True)
    components = models.ManyToManyField(Components)

    @property
    def url(self):
        # 10% taxes
        return "127.0.0.0.0:8000/page/{}".format(self.name)

    def __str__(self):
        return self.name
