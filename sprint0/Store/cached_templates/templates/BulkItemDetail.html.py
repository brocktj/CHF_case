# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428450401.81135
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/BulkItemDetail.html'
_template_uri = 'BulkItemDetail.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left']


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
        def content():
            return render_content(context._locals(__M_locals))
        blkProduct = context.get('blkProduct', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        blkProduct = context.get('blkProduct', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div>\r\n     <img src="')
        __M_writer(str( settings.STATIC_URL))
        __M_writer('/Store/media/images/Bulk')
        __M_writer(str( blkProduct.id ))
        __M_writer('.jpg"/>\r\n        <div>\r\n     <h1>')
        __M_writer(str( blkProduct.name ))
        __M_writer('</h1>\r\n            </div>\r\n        <div>\r\n     <p>')
        __M_writer(str( blkProduct.description))
        __M_writer('</p>\r\n            </div>\r\n        <div> $')
        __M_writer(str( blkProduct.current_price ))
        __M_writer('</div>\r\n        <div>\r\n        Quantity:<input type="number" id="qty')
        __M_writer(str( blkProduct.id ))
        __M_writer('" value="1">\r\n        </div>\r\n        <a class=\'add_button\' pid_data="')
        __M_writer(str( blkProduct.id ))
        __M_writer('" href="/Store/ShoppingCart.add_bulk_to_cart/')
        __M_writer(str( blkProduct.id ))
        __M_writer('">Buy Now</a>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n    <div id="left side" class="col-md-2">\r\n        <nav>\r\n            <ul class="nav nav-pills nav-stacked">\r\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\r\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\r\n                <li><a href="/Store/IndividualProduct/">Individual Products</a></li>\r\n                <li><a href="/Store/WardrobeItem/">Wardrobe Item</a></li>\r\n            </ul>\r\n        </nav>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/BulkItemDetail.html", "source_encoding": "ascii", "line_map": {"64": 20, "65": 20, "66": 20, "67": 22, "68": 22, "69": 25, "70": 25, "71": 27, "72": 27, "73": 29, "74": 29, "75": 31, "76": 31, "77": 31, "78": 31, "84": 4, "90": 4, "27": 0, "96": 90, "38": 1, "43": 16, "48": 34, "54": 18, "62": 18, "63": 20}, "uri": "BulkItemDetail.html"}
__M_END_METADATA
"""
