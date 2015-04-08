# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428467170.447271
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\homepage\\templates/Events.html'
_template_uri = 'Events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        events = context.get('events', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n<head lang="en">\r\n    <meta charset="UTF-8">\r\n    <title></title>\r\n</head>\r\n<body>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n    <div id="left side" class="col-md-2">\r\n        <nav>\r\n            <ul class="nav nav-pills nav-stacked">\r\n                <li><a href="/homepage/Events/">Events</a></li>\r\n\r\n            </ul>\r\n        </nav>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<br>\r\n<br>\r\n<a href="/homepage/Events.Create" class="btn btn-warning">New Event</a>\r\n<br>\r\n<br>\r\n\r\n<table class="table table-striped">\r\n    <tr>\r\n        <th>ID</th>\r\n        <th>Name</th>\r\n        <th>Description</th>\r\n        <th>Start Date</th>\r\n        <th>End Date</th>\r\n        <th>Actions</th>\r\n    </tr>\r\n\r\n')
        for Event in events:
            __M_writer('    <tr>\r\n        <td>')
            __M_writer(str( Event.id ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( Event.name ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( Event.description ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( Event.start_date ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( Event.end_date ))
            __M_writer('</td>\r\n        <td><a href="/homepage/Events.edit/')
            __M_writer(str( Event.id ))
            __M_writer('">Edit</a> | <a href="/homepage/Events.Delete/')
            __M_writer(str( Event.id ))
            __M_writer('">Delete</a> | <a href="/homepage/Events.view_details/')
            __M_writer(str( Event.id ))
            __M_writer('">Details</a>\r\n        </td>\r\n\r\n    </tr>\r\n')
        __M_writer('</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 9, "72": 9, "73": 27, "74": 28, "75": 29, "76": 29, "77": 30, "78": 30, "79": 31, "80": 31, "81": 32, "82": 32, "83": 33, "84": 33, "85": 34, "86": 34, "87": 34, "88": 34, "89": 34, "90": 34, "27": 0, "97": 91, "91": 39, "37": 1, "42": 40, "47": 51, "53": 41, "59": 41}, "uri": "Events.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\homepage\\templates/Events.html"}
__M_END_METADATA
"""
