from django.db import models
from django.utils.translation import ugettext_lazy as _

class Person(models.Model):
    first_name = models.CharField(max_length=50,
                                  verbose_name=_('give the first name: '),

                                  )
    last_name = models.CharField(max_length=50)



    # birth_date = models.DateField()

    # def baby_boomer_status(self):
    #     "Returns the person's baby-boomer status."
    #     import datetime
    #     if self.birth_date < datetime.date(1945, 8, 1):
    #         return "Pre-boomer"
    #     elif self.birth_date < datetime.date(1965, 1, 1):
    #         return "Baby boomer"
    #     else:
    #         return "Post-boomer"
    #
    # def _get_full_name(self):
    #     "Returns the person's full name."
    #     return '%s %s' % (self.first_name, self.last_name)
    # full_name = property(_get_full_name)