from django import template

register = template.Library()

@register.filter
def youtube_embed(value):
    """Konwertuje URL YouTube na format embed."""
    if 'youtube.com/watch?v=' in value:
        return value.replace('youtube.com/watch?v=', 'youtube.com/embed/')
    elif 'youtu.be/' in value:
        return value.replace('youtu.be/', 'youtube.com/embed/')
    return value 