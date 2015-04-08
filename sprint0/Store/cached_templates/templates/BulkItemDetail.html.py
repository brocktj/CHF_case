# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428372878.968259
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/BulkItemDetail.html'
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
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        blkProduct = context.get('blkProduct', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\n                <li><a href="/Store/IndividualProduct/">Individual Products</a></li>\n                <li><a href="/Store/WardrobeItem/">Wardrobe Item</a></li>\n            </ul>\n        </nav>\n    </div>\n')
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
{"source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/BulkItemDetail.html", "uri": "BulkItemDetail.html", "line_map": {"66": 18, "74": 18, "75": 20, "76": 20, "77": 20, "78": 20, "79": 22, "80": 22, "81": 25, "82": 25, "83": 27, "84": 27, "85": 29, "86": 29, "87": 31, "88": 31, "89": 31, "90": 31, "27": 0, "96": 90, "38": 1, "43": 16, "48": 34, "54": 4, "60": 4}}
__M_END_METADATA
"""
