# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428016267.855501
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/RentedWardrobeItem.html'
_template_uri = 'RentedWardrobeItem.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, '/homepage/templates/Managerbase.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        wdbItems = context.get('wdbItems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        wdbItems = context.get('wdbItems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="/Store/RentedLineItem.Create">Add Item</a>\n<table class="table table-striped">\n    <tr>\n        <th>Item</th>\n        <th>Date Out</th>\n        <th>Date Due</th>\n        <th>Renter</th>\n        <th>Modifier</th>\n\n    </tr>\n\n')
        for RentedLineItem in wdbItems:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( RentedLineItem.wardrobe_item_ID.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_out ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( RentedLineItem.date_due ))
            __M_writer('</td>\n')
            if RentedLineItem.transaction_ID is not None:
                __M_writer('        <td>')
                __M_writer(str( RentedLineItem.transaction_ID.customer.first_name ))
                __M_writer('</td>\n')
            else:
                __M_writer('        <td></td>\n')
            __M_writer('        <td> <a href="/Store/WardrobeItem.check_in/')
            __M_writer(str( RentedLineItem.id ))
            __M_writer('">Edit</a> | <a href="/Store/RentedLineItem.Delete/')
            __M_writer(str( RentedLineItem.id ))
            __M_writer('">Delete</a>  </td>\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "RentedWardrobeItem.html", "filename": "/Users/brock/sprint0/Store/templates/RentedWardrobeItem.html", "line_map": {"64": 27, "65": 27, "66": 28, "67": 29, "68": 31, "69": 31, "70": 31, "71": 31, "72": 31, "73": 35, "79": 73, "27": 0, "35": 1, "40": 36, "46": 9, "53": 9, "54": 21, "55": 22, "56": 23, "57": 23, "58": 24, "59": 24, "60": 25, "61": 25, "62": 26, "63": 27}, "source_encoding": "ascii"}
__M_END_METADATA
"""
