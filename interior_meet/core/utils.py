from django.db.models import Count

from interior_meet.designs.models import Design


def get_designs():
    return Design.objects.annotate(likes_count=Count('like')).order_by('-likes_count', 'title')