# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1424806543.489759
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/WardrobeItem.html'
_template_uri = 'WardrobeItem.html'
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
    return runtime._inherit_from(context, 'Managerbase.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        wdbItems = context.get('wdbItems', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        wdbItems = context.get('wdbItems', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<a href="/Store/WardrobeItem.Create">Add Item</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Size</th>\n        <th>Gender</th>\n        <th>Modifier</th>\n        <th>Pattern</th>\n        <th>Start Year</th>\n        <th>End Year</th>\n        <th>Actions</th>\n    </tr>\n\n')
        for WardrobeItem in wdbItems:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.size ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.gender ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.size_modifier ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.pattern ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.start_year ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( WardrobeItem.end_year ))
            __M_writer('</td>\n        <td> <a href="/Store/WardrobeItem.edit/')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('">Edit</a> | <a href="/Store/WardrobeItem.Delete/')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('">Delete</a>  </td>\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/Store/templates/WardrobeItem.html", "line_map": {"64": 30, "65": 30, "66": 31, "67": 31, "68": 32, "69": 32, "70": 33, "71": 33, "72": 34, "73": 34, "74": 34, "75": 34, "76": 38, "82": 76, "27": 0, "35": 1, "40": 39, "46": 9, "53": 9, "54": 24, "55": 25, "56": 26, "57": 26, "58": 27, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29}, "source_encoding": "ascii", "uri": "WardrobeItem.html"}
__M_END_METADATA
"""
