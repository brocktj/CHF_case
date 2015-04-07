# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428375033.570766
_enable_loop = True
_template_filename = 'C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/StoreView.html'
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
        def left():
            return render_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        blkProducts = context.get('blkProducts', UNDEFINED)
        wdbItems = context.get('wdbItems', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        persProducts = context.get('persProducts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/Store/BulkProduct/">Bulk Products</a></li>\n                <li><a href="/Store/PersonalProduct/">Personal Products</a></li>\n                <li><a href="/Store/IndividualProduct/">Individual Products</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        persProducts = context.get('persProducts', UNDEFINED)
        blkProducts = context.get('blkProducts', UNDEFINED)
        def content():
            return render_content(context)
        wdbItems = context.get('wdbItems', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<body>\n<form id="live-search" action="" class="styled" method="post">\n    <fieldset>\n        Search:<input type="text" class="text-input" id="filter" value="" />\n        <span id="filter-count"></span>\n    </fieldset>\n</form>\n<a href="/Store/ShoppingCart.delete_cart">Delete the cart</a>\n<a class="btn btn-success" href="/Store/ShoppingCart.view_cart/">View Cart</a>\n<div>\n    <h2>Products</h2>\n<table class="table">\n    <tr>\n\n')
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
{"source_encoding": "ascii", "filename": "C:\\Users\\Tanner\\PycharmProjects\\CHF_case-master\\sprint0\\Store\\templates/StoreView.html", "uri": "StoreView.html", "line_map": {"128": 88, "129": 88, "130": 91, "136": 130, "27": 0, "40": 1, "45": 15, "50": 94, "56": 4, "62": 4, "68": 17, "78": 17, "79": 32, "80": 33, "81": 36, "82": 36, "83": 36, "84": 36, "85": 37, "86": 37, "87": 38, "88": 38, "89": 39, "90": 39, "91": 41, "92": 41, "93": 44, "94": 44, "95": 49, "96": 57, "97": 58, "98": 61, "99": 61, "100": 61, "101": 61, "102": 62, "103": 62, "104": 63, "105": 63, "106": 64, "107": 64, "108": 66, "109": 67, "110": 68, "111": 69, "112": 71, "113": 73, "114": 73, "115": 78, "116": 83, "117": 84, "118": 85, "119": 85, "120": 85, "121": 85, "122": 86, "123": 86, "124": 87, "125": 87, "126": 88, "127": 88}}
__M_END_METADATA
"""
