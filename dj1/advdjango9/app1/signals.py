from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Blog


@receiver(post_save, sender=Blog)
def blog_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"New blog created: {instance.title}")
    else:
        print(f"Blog updated: {instance.title}") 

@receiver(pre_save, sender=Blog)
def blog_pre_save(sender, instance, **kwargs):
    print(f"About to save blog: {instance.title}")
