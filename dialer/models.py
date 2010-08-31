from datetime import datetime
from django.db import models

class Call(models.Model):
    name1 = models.CharField(max_length=30, blank=True, null=True)
    number1 = models.CharField(max_length=19)
    sid1 = models.CharField(max_length=35, default='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    name2 = models.CharField(max_length=30, blank=True, null=True)
    number2 = models.CharField(max_length=19)
    sid2 = models.CharField(max_length=35, default='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    creation_date = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        """
        Returns the numbers dialed
        """
        return '{0}[{1}] <-> {2}[{3}]'.format(self.name1,
                                              self.number1,
                                              self.name2,
                                              self.number2)
