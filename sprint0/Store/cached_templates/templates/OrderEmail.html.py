# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428020786.827449
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/OrderEmail.html'
_template_uri = 'OrderEmail.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import homepage.models as hmod 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        x = context.get('x', UNDEFINED)
        y = context.get('y', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n<!DOCTYPE html>\n<html>\n<head lang="en">\n    <meta charset="UTF-8">\n    <title></title>\n</head>\n<body>\n\n')
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
        int = context.get('int', UNDEFINED)
        x = context.get('x', UNDEFINED)
        y = context.get('y', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div>\n    Thank you for your order of:\n</div>\n<table class="table table-striped">\n    <tr>\n        <td>item</td>\n        <td></td>\n        <td>price</td>\n        <td>quantity</td>\n\n\n    </tr>\n    ')
        total = 0 
        
        __M_writer('\n')
        for k in x:
            __M_writer('    <tr>\n\n        ')
            item = hmod.BulkProduct.objects.get(id=k) 
            
            __M_writer('\n        ')
            qty = x.get(k) 
            
            __M_writer('\n\n        <td>\n            ')
            __M_writer(str( item.name ))
            __M_writer('\n        </td>\n        <td>\n            ')
            __M_writer(str( qty ))
            __M_writer('\n        </td>\n        <td>\n            $')
            __M_writer(str( item.current_price ))
            __M_writer('\n\n        </td>\n        ')
            total += (int(qty) * item.current_price) 
            
            __M_writer('\n    </tr>\n\n')
        for i in y:
            __M_writer('    <tr>\n\n        ')
            item = hmod.WardrobeItem.objects.get(id=k) 
            
            __M_writer('\n\n        <td>\n            ')
            __M_writer(str( item.name ))
            __M_writer('\n        </td>\n        <td>\n        </td>\n        <td>\n            $')
            __M_writer(str( item.standard_rental_value ))
            __M_writer('\n\n        </td>\n        ')
            total += item.standard_rental_value 
            
            __M_writer('\n    </tr>\n\n')
        __M_writer('    <tr>\n        <td></td>\n        <td></td>\n        <td>Total:</td>\n        <td>$')
        __M_writer(str( total ))
        __M_writer('</td>\n\n\n    </tr>\n\n</table>\n\n<div>Your card has been charged $')
        __M_writer(str( total ))
        __M_writer('</div>\n<div>Your items will ship to the following address:</div>\n<div></div>\n<div><a class="btn btn-success" href="/Store/ShoppingCart.check_out/')
        __M_writer(str( total ))
        __M_writer('">Checkout</a> </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 35, "65": 38, "66": 38, "67": 41, "69": 41, "70": 45, "71": 46, "72": 48, "74": 48, "75": 51, "76": 51, "77": 56, "78": 56, "79": 59, "16": 2, "81": 59, "18": 0, "83": 67, "84": 67, "85": 74, "86": 74, "87": 77, "88": 77, "28": 1, "29": 2, "94": 88, "34": 78, "40": 11, "82": 63, "49": 11, "50": 24, "52": 24, "53": 25, "54": 26, "55": 28, "57": 28, "58": 29, "60": 29, "61": 32, "62": 32, "63": 35}, "filename": "/Users/brock/sprint0/Store/templates/OrderEmail.html", "source_encoding": "ascii", "uri": "OrderEmail.html"}
__M_END_METADATA
"""
