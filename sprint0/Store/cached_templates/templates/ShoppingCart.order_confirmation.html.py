# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428012780.128613
_enable_loop = True
_template_filename = '/Users/brock/sprint0/Store/templates/ShoppingCart.order_confirmation.html'
_template_uri = 'ShoppingCart.order_confirmation.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


import homepage.models as hmod 

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
        int = context.get('int', UNDEFINED)
        x = context.get('x', UNDEFINED)
        y = context.get('y', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        int = context.get('int', UNDEFINED)
        x = context.get('x', UNDEFINED)
        y = context.get('y', UNDEFINED)
        def content():
            return render_content(context)
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
{"filename": "/Users/brock/sprint0/Store/templates/ShoppingCart.order_confirmation.html", "source_encoding": "ascii", "line_map": {"64": 25, "65": 26, "66": 28, "68": 28, "69": 29, "71": 29, "72": 32, "73": 32, "74": 35, "75": 35, "76": 38, "77": 38, "78": 41, "16": 2, "81": 45, "82": 46, "83": 48, "85": 48, "86": 51, "87": 51, "88": 56, "89": 56, "90": 59, "92": 59, "29": 0, "94": 67, "95": 67, "96": 74, "80": 41, "98": 77, "99": 77, "39": 1, "40": 2, "105": 99, "97": 74, "45": 78, "93": 63, "51": 11, "60": 11, "61": 24, "63": 24}, "uri": "ShoppingCart.order_confirmation.html"}
__M_END_METADATA
"""
