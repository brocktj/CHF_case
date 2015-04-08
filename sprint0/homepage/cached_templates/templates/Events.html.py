# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1428375845.788387
=======
_modified_time = 1428467170.447271
>>>>>>> Style-Changes
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\homepage\\templates/Events.html'
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
    return runtime._inherit_from(context, 'Managerbase.htm', _template_uri)
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
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/homepage/Events/">Events</a></li>\n\n            </ul>\n        </nav>\n    </div>\n')
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
<<<<<<< HEAD
        __M_writer('\n<a href="/homepage/Events.Create">New Event</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Start Date</th>\n        <th>End Date</th>\n        <th>Actions</th>\n    </tr>\n\n')
=======
        __M_writer('\r\n\r\n<br>\r\n<br>\r\n<a href="/homepage/Events.Create" class="btn btn-warning">New Event</a>\r\n<br>\r\n<br>\r\n\r\n<table class="table table-striped">\r\n    <tr>\r\n        <th>ID</th>\r\n        <th>Name</th>\r\n        <th>Description</th>\r\n        <th>Start Date</th>\r\n        <th>End Date</th>\r\n        <th>Actions</th>\r\n    </tr>\r\n\r\n')
>>>>>>> Style-Changes
        for Event in events:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( Event.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( Event.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( Event.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( Event.start_date ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( Event.end_date ))
            __M_writer('</td>\n        <td><a href="/homepage/Events.edit/')
            __M_writer(str( Event.id ))
            __M_writer('">Edit</a> | <a href="/homepage/Events.Delete/')
            __M_writer(str( Event.id ))
            __M_writer('">Delete</a> | <a href="/homepage/Events.view_details/')
            __M_writer(str( Event.id ))
            __M_writer('">Details</a>\n        </td>\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\homepage\\templates/Events.html", "uri": "Events.html", "line_map": {"65": 9, "72": 9, "73": 21, "74": 22, "75": 23, "76": 23, "77": 24, "78": 24, "79": 25, "80": 25, "81": 26, "82": 26, "83": 27, "84": 27, "85": 28, "86": 28, "87": 28, "88": 28, "89": 28, "90": 28, "27": 0, "97": 91, "91": 33, "37": 1, "42": 34, "47": 45, "53": 35, "59": 35}}
=======
{"line_map": {"65": 9, "72": 9, "73": 27, "74": 28, "75": 29, "76": 29, "77": 30, "78": 30, "79": 31, "80": 31, "81": 32, "82": 32, "83": 33, "84": 33, "85": 34, "86": 34, "87": 34, "88": 34, "89": 34, "90": 34, "27": 0, "97": 91, "91": 39, "37": 1, "42": 40, "47": 51, "53": 41, "59": 41}, "uri": "Events.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\homepage\\templates/Events.html"}
>>>>>>> Style-Changes
__M_END_METADATA
"""
