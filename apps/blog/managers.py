from django.db import models


class CategoryManager(models.Manager):
    """ manager category """

    def list_category(self):
        return self.all()