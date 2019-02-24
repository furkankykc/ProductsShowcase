from django.contrib import admin
# Register your models here.
from django.db.models.base import ModelBase

from product import models

for model_name in dir(models):
    model = getattr(models, model_name)
    if isinstance(model, ModelBase):
        admin.site.register(model)
        # print(model_name)

# admin.site.register(models.Page)
