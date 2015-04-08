# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428430045.635852
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/IndividualProduct.html'
_template_uri = 'IndividualProduct.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        indProducts = context.get('indProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n    <div id="left side" class="col-md-2">\r\n        <nav>\r\n            <ul class="nav nav-pills nav-stacked">\r\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\r\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\r\n                <li><a href="/Store/IndividualProduct/">Individual Products</a></li>\r\n            </ul>\r\n        </nav>\r\n    </div>\r\n')
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
        __M_writer('\r\n<a href="/Store/IndividualProduct.Create">Add item</a>\r\n<table class="table table-striped">\r\n    <tr>\r\n        <th>ID</th>\r\n        <th>Name</th>\r\n        <th>Description</th>\r\n        <th>Date Made</th>\r\n        <th>Current Price</th>\r\n        <th>Action</th>\r\n    </tr>\r\n')
        for IndividualProduct in indProducts:
            __M_writer('    <tr>\r\n        <td>')
            __M_writer(str( IndividualProduct.id ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( IndividualProduct.name ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( IndividualProduct.description ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( IndividualProduct.date_made ))
            __M_writer('</td>\r\n        <td>')
            __M_writer(str( IndividualProduct.current_price ))
            __M_writer('</td>\r\n        <td> <a href="/Store/IndividualProduct.edit/')
            __M_writer(str( IndividualProduct.id ))
            __M_writer('">Edit</a> | <a href="/Store/IndividualProduct.Delete/')
            __M_writer(str( IndividualProduct.id ))
            __M_writer('">Delete</a> </td>\r\n\r\n    </tr>\r\n')
        __M_writer('</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "IndividualProduct.html", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/IndividualProduct.html", "line_map": {"65": 17, "72": 17, "73": 28, "74": 29, "75": 30, "76": 30, "77": 31, "78": 31, "79": 32, "80": 32, "81": 33, "82": 33, "83": 34, "84": 34, "85": 35, "86": 35, "87": 35, "88": 35, "89": 39, "27": 0, "95": 89, "37": 1, "42": 15, "47": 40, "53": 4, "59": 4}, "source_encoding": "ascii"}
__M_END_METADATA
"""
