def create_slug(sender, instance, created, **kwargs):
    from .base64 import inttob64
    if instance.slug_address is None:
        slug = instance.slug_address
        slug = inttob64(instance.id)
        instance.slug_address = slug
        instance.save()


