from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def new_show_validator(self, postData):
        errors = {}
        if len(postData['title']) > 2:
            for show in Show.objects.all():
                if show.title == postData['title']:
                    errors["uniqueTitle"] = "Show title must be unique"
        else:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if datetime.strptime(postData['release_date'], "%Y-%m-%d" ) > datetime.now():
            errors['release_date'] = "Release date should be in the past"
        if postData['release_date'] == '':
            errors['blankDate'] = "Release date should not be blank" 
        if len(postData['desc']) > 1:
            if len(postData['desc']) < 10:
                errors["desc"] = "Show description is optional but should be at least 10 characters if present"
        return errors

    def update_show_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if postData['release_date'] != '':
            if datetime.strptime(postData['release_date'], "%Y-%m-%d" ) > datetime.now():
                errors['release_date'] = "Release date should be in the past"
        else:
            errors['blankDate'] = "Release date should not be blank"

        if len(postData['desc']) > 1:
            if len(postData['desc']) < 10:
                errors["desc"] = "Show description is optional but should be at least 10 characters if present"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
