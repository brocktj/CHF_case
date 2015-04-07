# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423255995.607985
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/IndividualProduct.html'
_template_uri = 'IndividualProduct.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        indProducts = context.get('indProducts', UNDEFINED)
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
        indProducts = context.get('indProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<a href="/homepage/IndividualProduct.Create">Add item</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Date Made</th>\n        <th>Current Price</th>\n        <th>Action</th>\n    </tr>\n')
        for IndividualProduct in indProducts:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( IndividualProduct.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( IndividualProduct.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( IndividualProduct.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( IndividualProduct.date_made ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( IndividualProduct.current_price ))
            __M_writer('</td>\n        <td> <a href="/homepage/IndividualProduct.edit/')
            __M_writer(str( IndividualProduct.id ))
            __M_writer('">Edit</a> | <a href="/homepage/IndividualProduct.Delete/')
            __M_writer(str( IndividualProduct.id ))
            __M_writer('">Delete</a> </td>\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 26, "65": 26, "66": 27, "67": 27, "68": 27, "69": 27, "70": 31, "76": 70, "27": 0, "35": 1, "40": 32, "46": 9, "53": 9, "54": 20, "55": 21, "56": 22, "57": 22, "58": 23, "59": 23, "60": 24, "61": 24, "62": 25, "63": 25}, "source_encoding": "ascii", "uri": "IndividualProduct.html", "filename": "/Users/brock/sprint0/homepage/templates/IndividualProduct.html"}
__M_END_METADATA
"""
