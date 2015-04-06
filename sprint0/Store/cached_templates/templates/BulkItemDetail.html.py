# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425723583.264465
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/BulkItemDetail.html'
_template_uri = 'BulkItemDetail.html'
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
        settings = context.get('settings', UNDEFINED)
        blkProduct = context.get('blkProduct', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\n                <li><a href="/Store/IndividualProduct/">Custom Products</a></li>\n                <li><a href="/Store/WardrobeItem">Wardrobe Items</a></li>\n                <li><a href="">Other Rental Items</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        blkProduct = context.get('blkProduct', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div>\n     <img src="')
        __M_writer(str( settings.STATIC_URL))
        __M_writer('/Store/media/images/Bulk')
        __M_writer(str( blkProduct.id ))
        __M_writer('.jpg"/>\n        <div>\n     <h1>')
        __M_writer(str( blkProduct.name ))
        __M_writer('</h1>\n            </div>\n        <div>\n     <p>')
        __M_writer(str( blkProduct.description))
        __M_writer('</p>\n            </div>\n        <div> $')
        __M_writer(str( blkProduct.current_price ))
        __M_writer('</div>\n        <div>\n        Quantity:<input type="number" id="qty')
        __M_writer(str( blkProduct.id ))
        __M_writer('" value="1">\n        </div>\n        <a class=\'add_button\' pid_data="')
        __M_writer(str( blkProduct.id ))
        __M_writer('" href="/Store/ShoppingCart.add_bulk_to_cart/')
        __M_writer(str( blkProduct.id ))
        __M_writer('">Buy Now</a>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "BulkItemDetail.html", "filename": "/Users/brock/sprint0/Store/templates/BulkItemDetail.html", "line_map": {"66": 12, "74": 12, "75": 14, "76": 14, "77": 14, "78": 14, "79": 16, "80": 16, "81": 19, "82": 19, "83": 21, "84": 21, "85": 23, "86": 23, "87": 25, "88": 25, "89": 25, "90": 25, "27": 0, "96": 90, "38": 1, "43": 28, "48": 42, "54": 29, "60": 29}, "source_encoding": "ascii"}
__M_END_METADATA
"""
