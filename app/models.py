from django.db import models


class Requests(models.Model):
    endpoint_name = models.CharField(max_length=50)
    call_params = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True, auto_created=True, primary_key=True,)
