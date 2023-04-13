from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        abstract = True

class form(TimeStamp):
    name = models.CharField(_("name of the user"), max_length= 50)
    phn_num = models.CharField(_("phone_number of the user"), max_length= 10)
    adr = models.CharField(_("address of the user"), max_length= 200)
    mem_count = models.CharField(_("number of family members"), max_length= 5)
    count = models.IntegerField(_("how many times the user has dumped garbage"), default=0)

    def __str__(self):
        return f"{self.name} | {self.phn_num} | {self.count}"
    
class form_check(TimeStamp):
    phn_check = models.CharField(_("login_phone_number"), max_length= 10)

