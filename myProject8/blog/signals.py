from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Blog


# Triggered before saving a Blog
@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print(f"About to save blog [pre-save]: {instance.title}")


# Triggered after saving a Blog
@receiver(post_save, sender=Blog)
def after_blog_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New blog created [post-save]: {instance.title}")
    else:
        print(f"Blog updated [post-save]: {instance.title}")