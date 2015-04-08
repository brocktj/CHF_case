# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1428376342.975955
=======
_modified_time = 1428467643.231205
>>>>>>> Style-Changes
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\homepage\\templates/EventDetails.html'
_template_uri = 'EventDetails.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['left', 'content']


import homepage.models as hmod 

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
        def left():
            return render_left(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
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
        areas = context.get('areas', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
<<<<<<< HEAD
        __M_writer('\n<table>\n    <tr>\n        <td>\n<img src="http://provo-canyon-parks.weebly.com/uploads/8/4/9/4/8494501/6284450.jpg?400" />\n\n        </td>\n        <td>\n            <div>\n                <h2>')
        __M_writer(str( event.name ))
        __M_writer('</h2>\n\n                <div>')
        __M_writer(str( event.description ))
        __M_writer('</div>\n                <div>')
=======
        __M_writer('\r\n<table>\r\n    <tr>\r\n        <td>\r\n<img src="http://provo-canyon-parks.weebly.com/uploads/8/4/9/4/8494501/6284450.jpg?400" />\r\n\r\n        </td>\r\n        <td>\r\n            <div>\r\n                <h2 class="event_detail">')
        __M_writer(str( event.name ))
        __M_writer('</h2>\r\n\r\n                <div class="event_detail">')
        __M_writer(str( event.description ))
        __M_writer('</div>\r\n                <div class="event_detail">')
>>>>>>> Style-Changes
        __M_writer(str( event.start_date ))
        __M_writer(' through ')
        __M_writer(str( event.end_date ))
        __M_writer('</div>\n            </div>\n        </td>\n    </tr>\n</table>\n<table class="table table-striped">\n')
        for area in areas:
            __M_writer('    ')
            saleItems = hmod.SaleItem.objects.filter(area_ID=area) 
            
            __M_writer('\n    <tr>\n        <td>\n            <h3>')
            __M_writer(str( area.name ))
            __M_writer('</h3>\n        </td>\n        <td>\n\n        </td>\n        <td>\n\n        </td>\n    </tr>\n\n    </tr>\n    <tr>\n        <td><div>')
            __M_writer(str( area.description ))
            __M_writer('</div></td>\n        <td><div>')
            __M_writer(str( area.coordinator_ID.first_name ))
            __M_writer(' ')
            __M_writer(str( area.coordinator_ID.last_name ))
            __M_writer('</div></td>\n        <td><div>')
            __M_writer(str( area.description ))
            __M_writer('</div></td>\n    </tr>\n    <tr>\n        <td>\n            <h3>Items for Sale</h3>\n        </td>\n        <td>\n\n        </td>\n        <td>\n\n        </td>\n\n')
            for SaleItem in saleItems:
                __M_writer('        <tr>\n    <td><div>')
                __M_writer(str( SaleItem.name ))
                __M_writer('</div></td>\n    <td><div>')
                __M_writer(str( SaleItem.description ))
                __M_writer('</div></td>\n    <td>$')
                __M_writer(str( SaleItem.low_price ))
                __M_writer('</td>\n    </tr>\n')
        __M_writer('\n\n</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\homepage\\templates/EventDetails.html", "uri": "EventDetails.html", "line_map": {"115": 109, "69": 10, "97": 45, "77": 10, "78": 19, "79": 19, "80": 21, "81": 21, "82": 22, "83": 22, "84": 22, "85": 22, "86": 28, "87": 29, "88": 29, "90": 29, "91": 32, "92": 32, "29": 0, "94": 44, "95": 45, "96": 45, "16": 2, "98": 45, "99": 46, "100": 46, "101": 59, "102": 60, "103": 61, "40": 1, "41": 2, "106": 62, "107": 63, "108": 63, "109": 67, "46": 71, "93": 44, "104": 61, "51": 82, "105": 62, "57": 72, "63": 72}}
=======
{"line_map": {"115": 109, "69": 10, "97": 45, "77": 10, "78": 19, "79": 19, "80": 21, "81": 21, "82": 22, "83": 22, "84": 22, "85": 22, "86": 28, "87": 29, "88": 29, "90": 29, "91": 32, "92": 32, "29": 0, "94": 44, "95": 45, "96": 45, "16": 2, "98": 45, "99": 46, "100": 46, "101": 59, "102": 60, "103": 61, "40": 1, "41": 2, "106": 62, "107": 63, "108": 63, "109": 67, "46": 71, "93": 44, "104": 61, "51": 82, "105": 62, "57": 72, "63": 72}, "uri": "EventDetails.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\homepage\\templates/EventDetails.html"}
>>>>>>> Style-Changes
__M_END_METADATA
"""
