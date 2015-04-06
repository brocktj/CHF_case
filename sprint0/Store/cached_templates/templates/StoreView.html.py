# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427235855.235872
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/StoreView.html'
_template_uri = 'StoreView.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        wdbItems = context.get('wdbItems', UNDEFINED)
        persProducts = context.get('persProducts', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        blkProducts = context.get('blkProducts', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        wdbItems = context.get('wdbItems', UNDEFINED)
        persProducts = context.get('persProducts', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        blkProducts = context.get('blkProducts', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<body>\n<form id="live-search" action="" class="styled" method="post">\n    <fieldset>\n        Search:<input type="text" class="text-input" id="filter" value="" />\n        <span id="filter-count"></span>\n    </fieldset>\n</form>\n<a href="/Store/ShoppingCart.delete_cart">Delete the cart</a>\n<div>\n    <h2>Products</h2>\n<table class="table">\n    <tr>\n\n')
        for BulkProduct in blkProducts:
            __M_writer('\n    <td>\n    <div class="item_container">\n        <img  class="center=block" src="')
            __M_writer(str( settings.STATIC_URL))
            __M_writer('Store//media/images/Bulk')
            __M_writer(str( BulkProduct.id ))
            __M_writer('.jpg" />\n        <div> <strong>')
            __M_writer(str( BulkProduct.name ))
            __M_writer('</strong></div>\n        <div>$')
            __M_writer(str( BulkProduct.current_price ))
            __M_writer('</div>\n        <a href="/Store/BulkItemDetail/')
            __M_writer(str( BulkProduct.id ))
            __M_writer('">View Details</a>\n        <div>\n        Quantity:<input class="input_field" type="number" id="qty')
            __M_writer(str( BulkProduct.id ))
            __M_writer('" value="1">\n        </div>\n        <div>\n        <button data-pid="')
            __M_writer(str( BulkProduct.id ))
            __M_writer('" class=\'add_button btn btn-warning\'>Buy Now</button>\n        </div>\n    </div>\n        </td>\n')
        __M_writer('    </tr>\n    </table>\n</div>\n<div>\n    <h2>Rentable Items</h2>\n<table class="table">\n    <tr>\n\n')
        for WardrobeItem in wdbItems:
            __M_writer('\n    <td>\n    <div class="item_container">\n        <img  class="center=block" src="')
            __M_writer(str( settings.STATIC_URL))
            __M_writer('Store//media/images/wdb')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('.jpg" />\n        <div> <strong>')
            __M_writer(str( WardrobeItem.name ))
            __M_writer('</strong></div>\n        <div>$')
            __M_writer(str( WardrobeItem.standard_rental_value ))
            __M_writer('</div>\n        <a href="/Store/RentalItemDetail/')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('">View Details</a>\n        <div>\n')
            if WardrobeItem.is_available_for_rental:
                __M_writer('            Available\n')
            else:
                __M_writer('            <span id="unavailable_rental">Unavailable</span>\n')
            __M_writer('        </div>\n        <div>\n        <button data-pid="')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('" class=\'add_button_rental btn btn-warning\'>Buy Now</button>\n        </div>\n    </div>\n        </td>\n')
        __M_writer('    </tr>\n    </table>\n</div>\n<div>\n    <h2>Personalized Products</h2>\n')
        for PersonalProduct in persProducts:
            __M_writer('    <div class="item_container">\n        <img src="')
            __M_writer(str( settings.STATIC_URL))
            __M_writer('/Store/media/images/pers')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('.jpg" />\n        <div> ')
            __M_writer(str( PersonalProduct.name ))
            __M_writer('</div>\n        <div>$')
            __M_writer(str( PersonalProduct.current_price ))
            __M_writer('</div>\n        <a href="/Store/PersonalItemDetail/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">View Details</a> <a class="btn btn-warning" href="/Store/StoreView.add_to_cart/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">Buy Now</a>\n    </div>\n')
        __M_writer('    </div>\n\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "38": 1, "43": 84, "49": 8, "59": 8, "60": 22, "61": 23, "62": 26, "63": 26, "64": 26, "65": 26, "66": 27, "67": 27, "68": 28, "69": 28, "70": 29, "71": 29, "72": 31, "73": 31, "74": 34, "75": 34, "76": 39, "77": 47, "78": 48, "79": 51, "80": 51, "81": 51, "82": 51, "83": 52, "84": 52, "85": 53, "86": 53, "87": 54, "88": 54, "89": 56, "90": 57, "91": 58, "92": 59, "93": 61, "94": 63, "95": 63, "96": 68, "97": 73, "98": 74, "99": 75, "100": 75, "101": 75, "102": 75, "103": 76, "104": 76, "105": 77, "106": 77, "107": 78, "108": 78, "109": 78, "110": 78, "111": 81, "117": 111}, "uri": "StoreView.html", "source_encoding": "ascii", "filename": "/Users/brock/sprint0/Store/templates/StoreView.html"}
__M_END_METADATA
"""
