# Introduction

`django-enum-js` is a simple package for sharing a specific implementation of
enums with the client through javascript that I developed for
[Agora](https://joinagora.com).

## Use

When writing Django model classes it's common to use an enum-style class to
store a few choices. E.g.

    class EventState:
        SCHEDULED = u'0'
        LIVE = u'1'
        CANCELLED = u'2'
        CHOICES = [(SCHEDULED, u'Scheduled (but not live yet)'),
                   (LIVE, u'Live'),
                   (CANCELLED, u'Cancelled')]


    class Event(models.Model):
        state = models.CharField(max_length=1, choices=EventState.CHOICES, default=EventState.LIVE)
        ...

Having defined this neat little enum-style class in Django it would be great to
be able to communicate and use this enum when writing the client-side code. To
do this we just add the following two lines:

    from django_enum_js import enum_wrapper
    enum_wrapper.register_enum(EventState)

And add the following line to any template where the enums are needed:

	<script src="{% url "js_enums" %}" type="text/javascript"></script>

as well as the url to a django file for defining urls (e.g. appname/urls.py):

    from django.conf.urls import patterns, include, url
    from django_enum_js.views import enums_js

    urlpatterns = patterns('',
        url(r'^api/jsenums/$', cache_page(3600)(enums_js), name='js_enums'),
        )

I've set a cache here as I expect the enums not to change very often.

You can now access all the enums through a global javascript variable called
*Enums*.

    > Enums.EventState.LIVE
    "1"
    > Enums.EventState.CHOICES[0]
    ["0", "Scheduled (but not live yet)"]

## Installation

Add `django_enum_js` to your **INSTALLED_APPS** in your **settings.py** file.

## Credit

Inspired by [django-js-reverse](https://github.com/ierror/django-js-reverse/).
