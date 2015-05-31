from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe

from django_enum_js import enum_wrapper

def enums_js(request):
    enums = enum_wrapper.get_json_formatted_enums()
    return render_to_response('django_enum_js/enums_js.tpl', { 'enums': mark_safe(enums), }, context_instance=RequestContext(request), content_type='application/javascript')
