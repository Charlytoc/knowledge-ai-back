from django.db import models
from django.contrib.auth.models import User
import uuid


class Community(models.Model):
        name = models.CharField(max_length=255)
        owner = models.ForeignKey(User, on_delete=models.CASCADE)
        description = models.TextField()
        is_public = models.BooleanField(default=True)
        invitation_token = models.UUIDField(default=uuid.uuid4, editable=False)
        tags = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
        TYPE_CHOICES = (
                ('HUMAN', 'Human'),
                ('AI', 'AI'),
        )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        username = models.CharField(max_length=255)
        communities = models.ManyToManyField(Community, blank=True)
        is_public = models.BooleanField(default=True)
        biography = models.TextField(null=True, blank=True)
        profile_type = models.CharField(max_length=25, choices=TYPE_CHOICES)
        character = models.TextField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class StudyPlan(models.Model):
        created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
        title = models.CharField(max_length=255)
        suggested_title = models.CharField(max_length=255, null=True, blank=True)
        description = models.TextField()
        ai_description = models.TextField(null=True, blank=True)
        communities = models.ManyToManyField(Community,blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Section(models.Model):
        title = models.CharField(max_length=255)
        objective = models.TextField()
        study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
        created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Topic(models.Model):
        title = models.CharField(max_length=255)
        explanation = models.TextField()
        section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
        
        objective = models.TextField(null=True, blank=True)
        created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Discussion(models.Model):
        created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
        topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
        profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
        discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
        text = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)