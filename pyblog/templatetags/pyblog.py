from django import template
from ..models import Category, Tag
from ..settings import AVATAR_DOMAIN
import hashlib

register = template.Library()


# 返回所以分类
@register.simple_tag()
def categories():
    return Category.objects.all()


@register.simple_tag()
def tags():
    return Tag.objects.all()


# 根据Email生成头像地址
@register.filter(name='gravatar')
def gravatar(email, size=32):
    return "%s/avatar/%s?s=%s&d=retro" % (AVATAR_DOMAIN,
                                          hashlib.md5(email.lower().encode()).hexdigest(), str(size))
