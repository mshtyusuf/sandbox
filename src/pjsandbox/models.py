from django.db import models

class query(models.Model):
    # file name to be saved and tab name
    # name = models.CharField(max_length=50)
    query_script = models.CharField(max_length=900)
    execution_time = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.query_script
    