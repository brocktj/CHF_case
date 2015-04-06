# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1424806210.090709
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/PersonalProduct.html'
_template_uri = 'PersonalProduct.html'
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
        persProducts = context.get('persProducts', UNDEFINED)
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
        persProducts = context.get('persProducts', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<a href="/Store/PersonalProduct.Create">Add item</a>\n<table class="table table-striped">\n    <tr>\n        <th>ID</th>\n        <th>Name</th>\n        <th>Description</th>\n        <th>Current Price</th>\n        <th>Instruction Form</th>\n        <th>Production time in days</th>\n        <th>Action</th>\n    </tr>\n')
        for PersonalProduct in persProducts:
            __M_writer('    <tr>\n        <td>')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.description ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.current_price ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.order_form_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( PersonalProduct.production_time ))
            __M_writer('</td>\n        <td> <a href="/Store/PersonalProduct.edit/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">Edit</a> | <a href="/Store/PersonalProduct.Delete/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">Delete</a>  </td>\n\n    </tr>\n')
        __M_writer('</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "PersonalProduct.html", "filename": "/Users/brock/sprint0/Store/templates/PersonalProduct.html", "line_map": {"64": 27, "65": 27, "66": 28, "67": 28, "68": 29, "69": 29, "70": 29, "71": 29, "72": 33, "78": 72, "27": 0, "35": 1, "40": 34, "46": 9, "53": 9, "54": 21, "55": 22, "56": 23, "57": 23, "58": 24, "59": 24, "60": 25, "61": 25, "62": 26, "63": 26}, "source_encoding": "ascii"}
__M_END_METADATA
"""
