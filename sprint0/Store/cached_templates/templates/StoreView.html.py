# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428466036.594862
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/StoreView.html'
_template_uri = 'StoreView.html'
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
        blkProducts = context.get('blkProducts', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        def left():
            return render_left(context._locals(__M_locals))
        persProducts = context.get('persProducts', UNDEFINED)
        wdbItems = context.get('wdbItems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n</html>')
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
        settings = context.get('settings', UNDEFINED)
        persProducts = context.get('persProducts', UNDEFINED)
        wdbItems = context.get('wdbItems', UNDEFINED)
        def content():
            return render_content(context)
        blkProducts = context.get('blkProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<body>\r\n<br>\r\n<form id="live-search" action="" class="styled" method="post">\r\n    <fieldset>\r\n        <strong class="search">Search for Items:  </strong><input type="text" class="text-input" id="filter" value="" />\r\n        <span id="filter-count"></span>\r\n    </fieldset>\r\n</form>\r\n\r\n<a id="cart" class="cart btn btn-success" href="/Store/ShoppingCart.view_cart/">View Cart</a>\r\n<br>\r\n<br>\r\n<div><a href="/Store/ShoppingCart.delete_cart" class="delete_cart">Delete the cart</a></div>\r\n<div>\r\n    <h2>Products</h2>\r\n<table class="table">\r\n    <tr>\r\n\r\n')
        for BulkProduct in blkProducts:
            __M_writer('\r\n    <td>\r\n    <div class="item_container">\r\n        <img  class="center=block" src="')
            __M_writer(str( settings.STATIC_URL))
            __M_writer('Store//media/images/Bulk')
            __M_writer(str( BulkProduct.id ))
            __M_writer('.jpg" />\r\n        <div> <strong>')
            __M_writer(str( BulkProduct.name ))
            __M_writer('</strong></div>\r\n        <div>$')
            __M_writer(str( BulkProduct.current_price ))
            __M_writer('</div>\r\n        <a href="/Store/BulkItemDetail/')
            __M_writer(str( BulkProduct.id ))
            __M_writer('">View Details</a>\r\n        <div>\r\n        Quantity:<input class="input_field" type="number" id="qty')
            __M_writer(str( BulkProduct.id ))
            __M_writer('" value="1">\r\n        </div>\r\n        <div>\r\n        <button data-pid="')
            __M_writer(str( BulkProduct.id ))
            __M_writer('" class=\'add_button btn btn-warning\'>Buy Now</button>\r\n        </div>\r\n    </div>\r\n        </td>\r\n')
        __M_writer('    </tr>\r\n    </table>\r\n</div>\r\n<div>\r\n    <h2>Rentable Items</h2>\r\n<table class="table">\r\n    <tr>\r\n\r\n')
        for WardrobeItem in wdbItems:
            __M_writer('\r\n    <td>\r\n    <div class="item_container">\r\n        <img  class="center=block" src="')
            __M_writer(str( settings.STATIC_URL))
            __M_writer('Store//media/images/wdb')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('.jpg" />\r\n        <div> <strong>')
            __M_writer(str( WardrobeItem.name ))
            __M_writer('</strong></div>\r\n        <div>$')
            __M_writer(str( WardrobeItem.standard_rental_value ))
            __M_writer('</div>\r\n        <a href="/Store/RentalItemDetail/')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('">View Details</a>\r\n        <div>\r\n')
            if WardrobeItem.is_available_for_rental:
                __M_writer('            Available\r\n')
            else:
                __M_writer('            <span id="unavailable_rental">Unavailable</span>\r\n')
            __M_writer('        </div>\r\n        <div>\r\n        <button data-pid="')
            __M_writer(str( WardrobeItem.id ))
            __M_writer('" class=\'add_button_rental btn btn-warning\'>Buy Now</button>\r\n        </div>\r\n    </div>\r\n        </td>\r\n')
        __M_writer('    </tr>\r\n    </table>\r\n</div>\r\n<div>\r\n    <h2>Personalized Products</h2>\r\n')
        for PersonalProduct in persProducts:
            __M_writer('    <div class="item_container">\r\n        <img src="')
            __M_writer(str( settings.STATIC_URL))
            __M_writer('/Store/media/images/pers')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('.jpg" />\r\n        <div> ')
            __M_writer(str( PersonalProduct.name ))
            __M_writer('</div>\r\n        <div>$')
            __M_writer(str( PersonalProduct.current_price ))
            __M_writer('</div>\r\n        <a href="/Store/PersonalItemDetail/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">View Details</a> <a class="btn btn-warning" href="/Store/StoreView.add_to_cart/')
            __M_writer(str( PersonalProduct.id ))
            __M_writer('">Buy Now</a>\r\n    </div>\r\n')
        __M_writer('    </div>\r\n\r\n</body>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 92, "129": 92, "130": 95, "136": 130, "27": 0, "40": 1, "45": 15, "50": 98, "56": 4, "62": 4, "68": 17, "78": 17, "79": 36, "80": 37, "81": 40, "82": 40, "83": 40, "84": 40, "85": 41, "86": 41, "87": 42, "88": 42, "89": 43, "90": 43, "91": 45, "92": 45, "93": 48, "94": 48, "95": 53, "96": 61, "97": 62, "98": 65, "99": 65, "100": 65, "101": 65, "102": 66, "103": 66, "104": 67, "105": 67, "106": 68, "107": 68, "108": 70, "109": 71, "110": 72, "111": 73, "112": 75, "113": 77, "114": 77, "115": 82, "116": 87, "117": 88, "118": 89, "119": 89, "120": 89, "121": 89, "122": 90, "123": 90, "124": 91, "125": 91, "126": 92, "127": 92}, "uri": "StoreView.html", "source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\Documents\\GitHub\\CHF_case\\sprint0\\Store\\templates/StoreView.html"}
__M_END_METADATA
"""
