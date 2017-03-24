__all__ = ['bwipjs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'BWIPJS'])
@Js
def PyJsHoisted_BWIPJS_(freetype, monochrome, this, arguments, var=var):
    var = Scope({u'this':this, u'monochrome':monochrome, u'freetype':freetype, u'arguments':arguments}, var)
    var.registers([u'monochrome', u'freetype'])
    if PyJsStrictNeq(var.get(u"this").get(u'constructor'),var.get(u'BWIPJS')):
        return var.get(u'BWIPJS').create(var.get(u'freetype'), var.get(u'monochrome'))
    var.get(u"this").put(u'bmap', var.get(u"null"))
    var.get(u"this").put(u'gstk', Js([]))
    var.get(u"this").callprop(u'reset')
    PyJs_Object_0_ = Js({u'monochrome':var.get(u'freetype').callprop(u'cwrap', Js(u'monochrome'), Js(u'number'), Js([Js(u'number')])),u'lookup':var.get(u'freetype').callprop(u'cwrap', Js(u'find_font'), Js(u'number'), Js([Js(u'string')])),u'bitmap':var.get(u'freetype').callprop(u'cwrap', Js(u'get_bitmap'), Js(u'number'), Js([Js(u'number'), Js(u'number'), Js(u'number'), Js(u'number')])),u'width':var.get(u'freetype').callprop(u'cwrap', Js(u'get_width'), Js(u'number'), Js([])),u'height':var.get(u'freetype').callprop(u'cwrap', Js(u'get_height'), Js(u'number'), Js([])),u'left':var.get(u'freetype').callprop(u'cwrap', Js(u'get_left'), Js(u'number'), Js([])),u'top':var.get(u'freetype').callprop(u'cwrap', Js(u'get_top'), Js(u'number'), Js([])),u'advance':var.get(u'freetype').callprop(u'cwrap', Js(u'get_advance'), Js(u'number'), Js([])),u'module':var.get(u'freetype')})
    var.get(u"this").put(u'ft', PyJs_Object_0_)
    var.get(u"this").get(u'ft').callprop(u'monochrome', (Js(1.0) if var.get(u'monochrome') else Js(0.0)))
PyJsHoisted_BWIPJS_.func_name = u'BWIPJS'
var.put(u'BWIPJS', PyJsHoisted_BWIPJS_)
pass
@Js
def PyJs_anonymous_1_(bitmap, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'bitmap':bitmap}, var)
    var.registers([u'bitmap'])
    if var.get(u'bitmap'):
        var.get(u"this").put(u'bmap', var.get(u'bitmap'))
    return var.get(u"this").get(u'bmap')
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'bitmap', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'g_tdx', Js(0.0))
    var.get(u"this").put(u'g_tdy', Js(0.0))
    var.get(u"this").put(u'g_tsx', Js(1.0))
    var.get(u"this").put(u'g_tsy', Js(1.0))
    var.get(u"this").put(u'g_posx', Js(0.0))
    var.get(u"this").put(u'g_posy', Js(0.0))
    var.get(u"this").put(u'g_penw', Js(1.0))
    var.get(u"this").put(u'g_path', Js([]))
    var.get(u"this").put(u'g_font', var.get(u"null"))
    var.get(u"this").put(u'g_rgb', Js([Js(0.0), Js(0.0), Js(0.0)]))
PyJs_anonymous_2_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'reset', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'clone', u'ctx', u'id'])
    @Js
    def PyJsHoisted_clone_(v, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'v':v}, var)
        var.registers([u'i', u'v', u't', u'id'])
        if var.get(u'v').instanceof(var.get(u'Array')):
            var.put(u't', Js([]))
            #for JS loop
            var.put(u'i', Js(0.0))
            while (var.get(u'i')<var.get(u'v').get(u'length')):
                try:
                    var.get(u't').put(var.get(u'i'), var.get(u'clone')(var.get(u'v').get(var.get(u'i'))))
                finally:
                        (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
            return var.get(u't')
        if var.get(u'v').instanceof(var.get(u'Object')):
            PyJs_Object_5_ = Js({})
            var.put(u't', PyJs_Object_5_)
            for PyJsTemp in var.get(u'v'):
                var.put(u'id', PyJsTemp)
                var.get(u't').put(var.get(u'id'), var.get(u'clone')(var.get(u'v').get(var.get(u'id'))))
            return var.get(u't')
        return var.get(u'v')
    PyJsHoisted_clone_.func_name = u'clone'
    var.put(u'clone', PyJsHoisted_clone_)
    PyJs_Object_4_ = Js({})
    var.put(u'ctx', PyJs_Object_4_)
    for PyJsTemp in var.get(u"this"):
        var.put(u'id', PyJsTemp)
        if (var.get(u'id').callprop(u'indexOf', Js(u'g_'))==Js(0.0)):
            var.get(u'ctx').put(var.get(u'id'), var.get(u'clone')(var.get(u"this").get(var.get(u'id'))))
    var.get(u"this").get(u'gstk').callprop(u'push', var.get(u'ctx'))
    pass
PyJs_anonymous_3_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'save', PyJs_anonymous_3_)
@Js
def PyJs_anonymous_6_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'ctx', u'id'])
    if var.get(u"this").get(u'gstk').get(u'length').neg():
        PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'grestore: stack underflow')))
        raise PyJsTempException
    var.put(u'ctx', var.get(u"this").get(u'gstk').callprop(u'pop'))
    for PyJsTemp in var.get(u'ctx'):
        var.put(u'id', PyJsTemp)
        var.get(u"this").put(var.get(u'id'), var.get(u'ctx').get(var.get(u'id')))
    if var.get(u"this").get(u'bmap'):
        var.get(u"this").get(u'bmap').callprop(u'color', var.get(u"this").get(u'g_rgb').get(u'0'), var.get(u"this").get(u'g_rgb').get(u'1'), var.get(u"this").get(u'g_rgb').get(u'2'))
PyJs_anonymous_6_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'restore', PyJs_anonymous_6_)
@Js
def PyJs_anonymous_7_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    PyJs_Object_8_ = Js({u'x':((var.get(u"this").get(u'g_posx')-var.get(u"this").get(u'g_tdx'))/var.get(u"this").get(u'g_tsx')),u'y':((var.get(u"this").get(u'g_posy')-var.get(u"this").get(u'g_tdy'))/var.get(u"this").get(u'g_tsy'))})
    return PyJs_Object_8_
PyJs_anonymous_7_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'currpos', PyJs_anonymous_7_)
@Js
def PyJs_anonymous_9_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'g_font')
PyJs_anonymous_9_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'currfont', PyJs_anonymous_9_)
@Js
def PyJs_anonymous_10_(name, this, arguments, var=var):
    var = Scope({u'this':this, u'name':name, u'arguments':arguments}, var)
    var.registers([u'name'])
    PyJs_Object_11_ = Js({u'FontName':var.get(u'name')})
    return PyJs_Object_11_
PyJs_anonymous_10_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'findfont', PyJs_anonymous_10_)
@Js
def PyJs_anonymous_12_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.get(u"this").put(u'g_tdx', (var.get(u"this").get(u'g_tsx')*var.get(u'x')))
    var.get(u"this").put(u'g_tdy', (var.get(u"this").get(u'g_tsy')*var.get(u'y')))
PyJs_anonymous_12_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'translate', PyJs_anonymous_12_)
@Js
def PyJs_anonymous_13_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.get(u"this").put(u'g_tsx', var.get(u'x'), u'*')
    var.get(u"this").put(u'g_tsy', var.get(u'y'), u'*')
PyJs_anonymous_13_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'scale', PyJs_anonymous_13_)
@Js
def PyJs_anonymous_14_(w, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'w':w}, var)
    var.registers([u'w'])
    var.get(u"this").put(u'g_penw', var.get(u'w'))
PyJs_anonymous_14_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'setlinewidth', PyJs_anonymous_14_)
@Js
def PyJs_anonymous_15_(f, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'f':f}, var)
    var.registers([u'f'])
    var.get(u"this").put(u'g_font', var.get(u'f'))
PyJs_anonymous_15_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'setfont', PyJs_anonymous_15_)
@Js
def PyJs_anonymous_16_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").get(u'ft').callprop(u'lookup', var.get(u"this").get(u'g_font').get(u'FontName').callprop(u'toString'))
PyJs_anonymous_16_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'getfont', PyJs_anonymous_16_)
@Js
def PyJs_anonymous_17_(s, this, arguments, var=var):
    var = Scope({u'this':this, u's':s, u'arguments':arguments}, var)
    var.registers([u'c', u'b', u'g', u'k', u'm', u's', u'r', u'y'])
    if (var.get(u's').get(u'length')==Js(6.0)):
        var.put(u'r', var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(0.0), Js(2.0)), Js(16.0)))
        var.put(u'g', var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(2.0), Js(2.0)), Js(16.0)))
        var.put(u'b', var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(4.0), Js(2.0)), Js(16.0)))
    else:
        if (var.get(u's').get(u'length')==Js(8.0)):
            var.put(u'c', (var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(0.0), Js(2.0)), Js(16.0))/Js(255.0)))
            var.put(u'm', (var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(2.0), Js(2.0)), Js(16.0))/Js(255.0)))
            var.put(u'y', (var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(4.0), Js(2.0)), Js(16.0))/Js(255.0)))
            var.put(u'k', (var.get(u'parseInt')(var.get(u's').callprop(u'substr', Js(6.0), Js(2.0)), Js(16.0))/Js(255.0)))
            var.put(u'r', var.get(u'Math').callprop(u'round', (((Js(1.0)-var.get(u'c'))*(Js(1.0)-var.get(u'k')))*Js(255.0))))
            var.put(u'g', var.get(u'Math').callprop(u'round', (((Js(1.0)-var.get(u'm'))*(Js(1.0)-var.get(u'k')))*Js(255.0))))
            var.put(u'b', var.get(u'Math').callprop(u'round', (((Js(1.0)-var.get(u'y'))*(Js(1.0)-var.get(u'k')))*Js(255.0))))
        else:
            PyJsTempException = JsToPyException(((Js(u'bwipp.setcolor: invalid string length (')+var.get(u's'))+Js(u')')))
            raise PyJsTempException
    var.get(u"this").get(u'bmap').callprop(u'color', var.get(u'r'), var.get(u'g'), var.get(u'b'))
    var.get(u"this").put(u'g_rgb', Js([var.get(u'r'), var.get(u'g'), var.get(u'b')]))
PyJs_anonymous_17_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'setcolor', PyJs_anonymous_17_)
@Js
def PyJs_anonymous_18_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'g_path', Js([]))
PyJs_anonymous_18_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'newpath', PyJs_anonymous_18_)
@Js
def PyJs_anonymous_19_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'c1', u'c0'])
    if var.get(u"this").get(u'g_path').get(u'length'):
        var.put(u'c0', var.get(u"this").get(u'g_path').get(u'0'))
        var.put(u'c1', var.get(u"this").get(u'g_path').get((var.get(u"this").get(u'g_path').get(u'length')-Js(1.0))))
        var.get(u"this").get(u'g_path').callprop(u'push', Js([var.get(u'c1').get(u'0'), var.get(u'c1').get(u'1')]))
        var.get(u"this").get(u'g_path').callprop(u'push', Js([Js(u'c')]))
        var.get(u"this").get(u'g_path').callprop(u'push', Js([var.get(u'c0').get(u'0'), var.get(u'c0').get(u'1')]))
PyJs_anonymous_19_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'closepath', PyJs_anonymous_19_)
@Js
def PyJs_anonymous_20_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.get(u"this").put(u'g_posx', (var.get(u"this").get(u'g_tdx')+(var.get(u"this").get(u'g_tsx')*var.get(u'x'))))
    var.get(u"this").put(u'g_posy', (var.get(u"this").get(u'g_tdy')+(var.get(u"this").get(u'g_tsy')*var.get(u'y'))))
PyJs_anonymous_20_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'moveto', PyJs_anonymous_20_)
@Js
def PyJs_anonymous_21_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.get(u"this").put(u'g_posx', (var.get(u"this").get(u'g_tsx')*var.get(u'x')), u'+')
    var.get(u"this").put(u'g_posy', (var.get(u"this").get(u'g_tsy')*var.get(u'y')), u'+')
PyJs_anonymous_21_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'rmoveto', PyJs_anonymous_21_)
@Js
def PyJs_anonymous_22_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.get(u"this").get(u'g_path').callprop(u'push', Js([var.get(u"this").get(u'g_posx'), var.get(u"this").get(u'g_posy')]))
    var.get(u"this").get(u'g_path').callprop(u'push', Js([Js(u'l')]))
    var.get(u"this").put(u'g_posx', (var.get(u"this").get(u'g_tdx')+(var.get(u"this").get(u'g_tsx')*var.get(u'x'))))
    var.get(u"this").put(u'g_posy', (var.get(u"this").get(u'g_tdy')+(var.get(u"this").get(u'g_tsy')*var.get(u'y'))))
    var.get(u"this").get(u'g_path').callprop(u'push', Js([var.get(u"this").get(u'g_posx'), var.get(u"this").get(u'g_posy')]))
PyJs_anonymous_22_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'lineto', PyJs_anonymous_22_)
@Js
def PyJs_anonymous_23_(x, y, this, arguments, var=var):
    var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
    var.registers([u'y', u'x'])
    var.get(u"this").get(u'g_path').callprop(u'push', Js([var.get(u"this").get(u'g_posx'), var.get(u"this").get(u'g_posy')]))
    var.get(u"this").get(u'g_path').callprop(u'push', Js([Js(u'l')]))
    var.get(u"this").put(u'g_posx', (var.get(u"this").get(u'g_tsx')*var.get(u'x')), u'+')
    var.get(u"this").put(u'g_posy', (var.get(u"this").get(u'g_tsy')*var.get(u'y')), u'+')
    var.get(u"this").get(u'g_path').callprop(u'push', Js([var.get(u"this").get(u'g_posx'), var.get(u"this").get(u'g_posy')]))
PyJs_anonymous_23_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'rlineto', PyJs_anonymous_23_)
@Js
def PyJs_anonymous_24_(str, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'str':str}, var)
    var.registers([u'a', u'd', u'str', u'i', u'h', u'cd', u't', u'w', u'offset', u'font', u'cca', u'size'])
    var.put(u'font', var.get(u"this").callprop(u'getfont'))
    var.put(u'size', ((+var.get(u"this").get(u'g_font').get(u'FontSize')) or Js(10.0)))
    var.put(u'cca', PyJsStrictEq(var.get(u'str',throw=False).typeof(),Js(u'string')))
    var.put(u'w', Js(0.0))
    var.put(u'a', Js(0.0))
    var.put(u'd', Js(0.0))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<var.get(u'str').get(u'length')):
        try:
            var.put(u'cd', (var.get(u'str').callprop(u'charCodeAt', var.get(u'i')) if var.get(u'cca') else var.get(u'str').get(var.get(u'i'))))
            var.put(u'offset', var.get(u"this").get(u'ft').callprop(u'bitmap', var.get(u'font'), var.get(u'cd'), (var.get(u'size')*var.get(u"this").get(u'g_tsx')), (var.get(u'size')*var.get(u"this").get(u'g_tsy'))))
            var.put(u'w', var.get(u"this").get(u'ft').callprop(u'advance'), u'+')
            if var.get(u'offset').neg():
                continue
            var.put(u'h', var.get(u"this").get(u'ft').callprop(u'height'))
            var.put(u't', var.get(u"this").get(u'ft').callprop(u'top'))
            var.put(u'a', var.get(u'Math').callprop(u'max', var.get(u'a'), var.get(u't')))
            var.put(u'd', var.get(u'Math').callprop(u'max', var.get(u'd'), (var.get(u'h')-var.get(u't'))))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    PyJs_Object_25_ = Js({u'w':(var.get(u'w')/var.get(u"this").get(u'g_tsx')),u'h':((var.get(u'a')+var.get(u'd'))/var.get(u"this").get(u'g_tsy')),u'a':(var.get(u'a')/var.get(u"this").get(u'g_tsy')),u'd':(var.get(u'd')/var.get(u"this").get(u'g_tsy'))})
    return PyJs_Object_25_
PyJs_anonymous_24_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'stringwidth', PyJs_anonymous_24_)
@Js
def PyJs_anonymous_26_(str, b, this, arguments, var=var):
    var = Scope({u'this':this, u'b':b, u'arguments':arguments, u'str':str}, var)
    var.registers([u'b', u'sw', u'str'])
    var.put(u'sw', var.get(u"this").callprop(u'stringwidth', var.get(u'str')))
    var.get(u"this").callprop(u'rlineto', Js(0.0), var.get(u'sw').get(u'a'))
    var.get(u"this").callprop(u'rlineto', var.get(u'sw').get(u'w'), Js(0.0))
    var.get(u"this").callprop(u'rlineto', Js(0.0), (-var.get(u'sw').get(u'h')))
PyJs_anonymous_26_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'charpath', PyJs_anonymous_26_)
@Js
def PyJs_anonymous_27_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'lly', u'llx', u'pth', u'i', u'rv', u'urx', u'ury', u'inc'])
    if var.get(u"this").get(u'g_path').get(u'length').neg():
        PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'pathbbox: --nocurrentpoint--')))
        raise PyJsTempException
    var.put(u'pth', var.get(u"this").get(u'g_path'))
    var.put(u'llx', var.get(u'pth').get(u'0').get(u'0'))
    var.put(u'lly', var.get(u'pth').get(u'0').get(u'1'))
    var.put(u'urx', Js(0.0))
    var.put(u'ury', Js(0.0))
    #for JS loop
    var.put(u'i', Js(2.0))
    var.put(u'inc', Js(2.0))
    while (var.get(u'i')<var.get(u'pth').get(u'length')):
        try:
            if (var.get(u'llx')>var.get(u'pth').get(var.get(u'i')).get(u'0')):
                var.put(u'llx', var.get(u'pth').get(var.get(u'i')).get(u'0'))
            if (var.get(u'urx')<var.get(u'pth').get(var.get(u'i')).get(u'0')):
                var.put(u'urx', var.get(u'pth').get(var.get(u'i')).get(u'0'))
            if (var.get(u'lly')>var.get(u'pth').get(var.get(u'i')).get(u'1')):
                var.put(u'lly', var.get(u'pth').get(var.get(u'i')).get(u'1'))
            if (var.get(u'ury')<var.get(u'pth').get(var.get(u'i')).get(u'1')):
                var.put(u'ury', var.get(u'pth').get(var.get(u'i')).get(u'1'))
            var.put(u'inc', (Js(1.0) if (var.get(u'inc')==Js(2.0)) else Js(2.0)))
        finally:
                var.put(u'i', var.get(u'inc'), u'+')
    PyJs_Object_28_ = Js({u'llx':((var.get(u'llx')-var.get(u"this").get(u'g_tdx'))/var.get(u"this").get(u'g_tsx')),u'lly':((var.get(u'lly')-var.get(u"this").get(u'g_tdy'))/var.get(u"this").get(u'g_tsy')),u'urx':((var.get(u'urx')-var.get(u"this").get(u'g_tdx'))/var.get(u"this").get(u'g_tsx')),u'ury':((var.get(u'ury')-var.get(u"this").get(u'g_tdy'))/var.get(u"this").get(u'g_tsy'))})
    var.put(u'rv', PyJs_Object_28_)
    return var.get(u'rv')
PyJs_anonymous_27_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'pathbbox', PyJs_anonymous_27_)
@Js
def PyJs_anonymous_29_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'a', u'e', u'i', u'segs', u'penx', u's', u'peny'])
    if PyJsStrictEq(var.get(u"this").get(u'__miny'),var.get(u'undefined')):
        var.get(u"this").put(u'__miny', var.get(u'Infinity'))
    var.put(u'penx', (var.get(u"this").get(u'g_penw')*var.get(u"this").get(u'g_tsx')))
    var.put(u'peny', (var.get(u"this").get(u'g_penw')*var.get(u"this").get(u'g_tsy')))
    var.put(u'segs', (var.get(u"this").get(u'g_path').get(u'length')/Js(3.0)))
    if (var.get(u"this").get(u'g_path').get((var.get(u"this").get(u'g_path').get(u'length')-Js(2.0))).get(u'0')==Js(u'c')):
        (var.put(u'segs',Js(var.get(u'segs').to_number())-Js(1))+Js(1))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<var.get(u"this").get(u'g_path').get(u'length')):
        var.put(u's', var.get(u"this").get(u'g_path').get((var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'a', var.get(u"this").get(u'g_path').get((var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        var.put(u'e', var.get(u"this").get(u'g_path').get((var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))))
        if (var.get(u"this").get(u'__miny')>var.get(u's').get(u'1')):
            var.get(u"this").put(u'__miny', var.get(u's').get(u'1'))
        if (var.get(u"this").get(u'__miny')>var.get(u'e').get(u'1')):
            var.get(u"this").put(u'__miny', var.get(u'e').get(u'1'))
        while 1:
            SWITCHED = False
            CONDITION = (var.get(u'a').get(u'0'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'l')):
                SWITCHED = True
                var.get(u"this").callprop(u'drawline', var.get(u'true'), var.get(u's').get(u'0'), var.get(u's').get(u'1'), var.get(u'e').get(u'0'), var.get(u'e').get(u'1'), var.get(u'penx'), var.get(u'peny'), (var.get(u'segs')>Js(1.0)))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(u'c')):
                SWITCHED = True
                break
            if True:
                SWITCHED = True
                PyJsTempException = JsToPyException(var.get(u'Error').create((Js(u'stroke: undefined opcode: ')+var.get(u'a').get(u'0'))))
                raise PyJsTempException
            SWITCHED = True
            break
    
    var.get(u"this").put(u'g_path', Js([]))
PyJs_anonymous_29_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'stroke', PyJs_anonymous_29_)
@Js
def PyJs_anonymous_30_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'g_tsx', (var.get(u'Math').callprop(u'floor', var.get(u"this").get(u'g_tsx')) or Js(1.0)))
    var.get(u"this").put(u'g_tsy', (var.get(u'Math').callprop(u'floor', var.get(u"this").get(u'g_tsy')) or Js(1.0)))
PyJs_anonymous_30_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'floorscale', PyJs_anonymous_30_)
@Js
def PyJs_anonymous_31_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'g_tsx', (var.get(u'Math').callprop(u'ceil', var.get(u"this").get(u'g_tsx')) or Js(1.0)))
    var.get(u"this").put(u'g_tsy', (var.get(u'Math').callprop(u'ceil', var.get(u"this").get(u'g_tsy')) or Js(1.0)))
PyJs_anonymous_31_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'ceilscale', PyJs_anonymous_31_)
@Js
def PyJs_anonymous_32_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put(u'g_tsx', (var.get(u'Math').callprop(u'round', var.get(u"this").get(u'g_tsx')) or Js(1.0)))
    var.get(u"this").put(u'g_tsy', (var.get(u'Math').callprop(u'round', var.get(u"this").get(u'g_tsy')) or Js(1.0)))
PyJs_anonymous_32_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'roundscale', PyJs_anonymous_32_)
@Js
def PyJs_anonymous_33_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'lly', u'llx', u'pth', u'i', u'urx', u'ury', u'inc'])
    if var.get(u"this").get(u'g_path').get(u'length').neg():
        return var.get('undefined')
    var.put(u'pth', var.get(u"this").get(u'g_path'))
    var.put(u'llx', var.get(u'pth').get(u'0').get(u'0'))
    var.put(u'lly', var.get(u'pth').get(u'0').get(u'1'))
    var.put(u'urx', Js(0.0))
    var.put(u'ury', Js(0.0))
    #for JS loop
    var.put(u'i', Js(2.0))
    var.put(u'inc', Js(2.0))
    while (var.get(u'i')<var.get(u'pth').get(u'length')):
        try:
            if (var.get(u'llx')>var.get(u'pth').get(var.get(u'i')).get(u'0')):
                var.put(u'llx', var.get(u'pth').get(var.get(u'i')).get(u'0'))
            if (var.get(u'urx')<var.get(u'pth').get(var.get(u'i')).get(u'0')):
                var.put(u'urx', var.get(u'pth').get(var.get(u'i')).get(u'0'))
            if (var.get(u'lly')>var.get(u'pth').get(var.get(u'i')).get(u'1')):
                var.put(u'lly', var.get(u'pth').get(var.get(u'i')).get(u'1'))
            if (var.get(u'ury')<var.get(u'pth').get(var.get(u'i')).get(u'1')):
                var.put(u'ury', var.get(u'pth').get(var.get(u'i')).get(u'1'))
            var.put(u'inc', (Js(1.0) if (var.get(u'inc')==Js(2.0)) else Js(2.0)))
        finally:
                var.put(u'i', var.get(u'inc'), u'+')
    var.get(u"this").get(u'bmap').callprop(u'extent', var.get(u'llx'), var.get(u'lly'), var.get(u'urx'), var.get(u'ury'))
PyJs_anonymous_33_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'setextent', PyJs_anonymous_33_)
@Js
def PyJs_anonymous_34_(width, height, source, this, arguments, var=var):
    var = Scope({u'this':this, u'width':width, u'source':source, u'arguments':arguments, u'height':height}, var)
    var.registers([u'x', u'sy', u'sx', u'y1', u'width', u'k', u'j', u'height', u'bt', u'y', u'source', u'dx', u'dy', u'rl', u'y0', u'x0', u'x1', u'by'])
    var.put(u'sx', var.get(u'Math').callprop(u'round', var.get(u"this").get(u'g_tsx')))
    var.put(u'sy', var.get(u'Math').callprop(u'round', var.get(u"this").get(u'g_tsy')))
    var.put(u'dx', var.get(u'Math').callprop(u'floor', (var.get(u'sx')/var.get(u'width'))))
    var.put(u'dy', var.get(u'Math').callprop(u'floor', (var.get(u'sy')/var.get(u'height'))))
    var.put(u'rl', var.get(u'Math').callprop(u'ceil', (var.get(u'width')/Js(8.0))))
    var.put(u'y0', (var.get(u'Math').callprop(u'floor', var.get(u"this").get(u'g_tdy'))+(var.get(u'height')*var.get(u'dy'))))
    pass
    if (var.get(u'dx').neg() or var.get(u'dy').neg()):
        PyJsTempException = JsToPyException(var.get(u'Error').create(Js(u'Image scaled to zero size.')))
        raise PyJsTempException
    #for JS loop
    var.put(u'y', Js(0.0))
    while (var.get(u'y')<var.get(u'height')):
        try:
            var.put(u'x0', var.get(u'Math').callprop(u'floor', var.get(u"this").get(u'g_tdx')))
            var.put(u'y0', var.get(u'dy'), u'-')
            #for JS loop
            var.put(u'x', Js(0.0))
            while (var.get(u'x')<var.get(u'width')):
                try:
                    var.put(u'by', var.get(u'source').get(((var.get(u'y')*var.get(u'rl'))+PyJsBshift(var.get(u'x'),Js(3.0)))))
                    var.put(u'bt', (var.get(u'by')&(Js(1.0)<<(Js(7.0)-(var.get(u'x')&Js(7.0))))))
                    if var.get(u'bt'):
                        var.put(u'x1', (var.get(u'x0')+var.get(u'dx')))
                        var.put(u'y1', (var.get(u'y0')+var.get(u'dy')))
                        #for JS loop
                        var.put(u'j', var.get(u'y0'))
                        while (var.get(u'j')<var.get(u'y1')):
                            try:
                                #for JS loop
                                var.put(u'k', var.get(u'x0'))
                                while (var.get(u'k')<var.get(u'x1')):
                                    try:
                                        var.get(u"this").get(u'bmap').callprop(u'set', var.get(u'k'), var.get(u'j'), Js(255.0))
                                    finally:
                                            (var.put(u'k',Js(var.get(u'k').to_number())+Js(1))-Js(1))
                            finally:
                                    (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
                    var.put(u'x0', var.get(u'dx'), u'+')
                finally:
                        (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
        finally:
                (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
PyJs_anonymous_34_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'imagemask', PyJs_anonymous_34_)
@Js
def PyJs_anonymous_35_(str, dx, dy, this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments, u'dx':dx, u'str':str, u'dy':dy}, var)
    var.registers([u'a', u'ch', u'dx', u'str', u'i', u'h', u'dy', u'l', u'b', u't', u'w', u'offset', u'y', u'x', u'font', u'cca', u'size'])
    var.put(u'font', var.get(u"this").callprop(u'getfont'))
    var.put(u'size', ((+var.get(u"this").get(u'g_font').get(u'FontSize')) or Js(10.0)))
    var.put(u'cca', PyJsStrictEq(var.get(u'str',throw=False).typeof(),Js(u'string')))
    var.put(u'dx', (var.get(u"this").get(u'g_tsx')*var.get(u'dx')))
    var.put(u'dy', (var.get(u"this").get(u'g_tsy')*var.get(u'dy')))
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<var.get(u'str').get(u'length')):
        try:
            var.put(u'ch', (var.get(u'str').callprop(u'charCodeAt', var.get(u'i')) if var.get(u'cca') else var.get(u'str').get(var.get(u'i'))))
            var.put(u'offset', var.get(u"this").get(u'ft').callprop(u'bitmap', var.get(u'font'), var.get(u'ch'), (var.get(u'size')*var.get(u"this").get(u'g_tsx')), (var.get(u'size')*var.get(u"this").get(u'g_tsy'))))
            if var.get(u'offset').neg():
                var.get(u"this").put(u'g_posx', (var.get(u"this").get(u'ft').callprop(u'advance')+var.get(u'dx')), u'+')
                continue
            var.put(u'l', (var.get(u"this").get(u'g_posx')+var.get(u"this").get(u'ft').callprop(u'left')))
            if (((var.get(u'font')<=Js(1.0)) and (var.get(u'ch')>=Js(48.0))) and (var.get(u'ch')<=Js(57.0))):
                var.put(u'l', (Js(0.5)*var.get(u"this").get(u'g_tsx')), u'-')
            var.put(u't', ((var.get(u"this").get(u'g_posy')+var.get(u"this").get(u'ft').callprop(u'top'))+var.get(u'dy')))
            var.put(u'w', var.get(u"this").get(u'ft').callprop(u'width'))
            var.put(u'h', var.get(u"this").get(u'ft').callprop(u'height'))
            var.put(u'b', var.get(u"this").get(u'ft').get(u'module').get(u'HEAPU8').callprop(u'subarray', var.get(u'offset'), (var.get(u'offset')+(var.get(u'w')*var.get(u'h')))))
            pass
            #for JS loop
            var.put(u'x', Js(0.0))
            while (var.get(u'x')<var.get(u'w')):
                try:
                    #for JS loop
                    var.put(u'y', Js(0.0))
                    while (var.get(u'y')<var.get(u'h')):
                        try:
                            var.put(u'a', var.get(u'b').get(((var.get(u'y')*var.get(u'w'))+var.get(u'x'))))
                            if var.get(u'a'):
                                var.get(u"this").get(u'bmap').callprop(u'set', (var.get(u'l')+var.get(u'x')), (var.get(u't')-var.get(u'y')), var.get(u'a'))
                        finally:
                                (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
                finally:
                        (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            var.get(u"this").put(u'g_posx', (var.get(u"this").get(u'ft').callprop(u'advance')+var.get(u'dx')), u'+')
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
PyJs_anonymous_35_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'show', PyJs_anonymous_35_)
@Js
def PyJs_anonymous_36_(optmz, x1, y1, x2, y2, penx, peny, merge, this, arguments, var=var):
    var = Scope({u'y2':y2, u'merge':merge, u'this':this, u'peny':peny, u'penx':penx, u'x2':x2, u'optmz':optmz, u'arguments':arguments, u'y1':y1, u'x1':x1}, var)
    var.registers([u'pixw', u'dv', u'pixh', u'y1', u'y2', u'penw', u'x1', u'peny', u'penx', u'lx', u'ly', u'optmz', u'x2', u'du', u'd', u'j', u'merge', u't', u'y', u'x', u'ky', u'kx'])
    if (var.get(u'optmz') and ((var.get(u'x1')==var.get(u'x2')) or (var.get(u'y1')==var.get(u'y2')))):
        var.put(u'lx', var.get(u'Math').callprop(u'round', var.get(u'penx')))
        var.put(u'ly', var.get(u'Math').callprop(u'round', var.get(u'peny')))
        if (var.get(u'y2')<var.get(u'y1')):
            var.put(u't', var.get(u'y1'))
            var.put(u'y1', var.get(u'y2'))
            var.put(u'y2', var.get(u't'))
        if (var.get(u'x2')<var.get(u'x1')):
            var.put(u't', var.get(u'x1'))
            var.put(u'x1', var.get(u'x2'))
            var.put(u'x2', var.get(u't'))
        if (var.get(u'x1')==var.get(u'x2')):
            var.put(u'x1', var.get(u'Math').callprop(u'floor', (var.get(u'x1')-(var.get(u'lx')/Js(2.0)))))
            var.put(u'x2', var.get(u'Math').callprop(u'floor', (var.get(u'x2')+(var.get(u'lx')/Js(2.0)))))
            var.put(u'y1', var.get(u'Math').callprop(u'floor', (var.get(u'y1')-((var.get(u'ly')/Js(2.0)) if var.get(u'merge') else Js(0.0)))))
            var.put(u'y2', var.get(u'Math').callprop(u'floor', (var.get(u'y2')+((var.get(u'ly')/Js(2.0)) if var.get(u'merge') else Js(0.0)))))
        else:
            var.put(u'y1', var.get(u'Math').callprop(u'floor', (var.get(u'y1')-(var.get(u'ly')/Js(2.0)))))
            var.put(u'y2', var.get(u'Math').callprop(u'floor', (var.get(u'y2')+(var.get(u'ly')/Js(2.0)))))
            var.put(u'x1', var.get(u'Math').callprop(u'floor', (var.get(u'x1')-((var.get(u'lx')/Js(2.0)) if var.get(u'merge') else Js(0.0)))))
            var.put(u'x2', var.get(u'Math').callprop(u'floor', (var.get(u'x2')+((var.get(u'lx')/Js(2.0)) if var.get(u'merge') else Js(0.0)))))
        #for JS loop
        var.put(u'y', var.get(u'y1'))
        while (var.get(u'y')<var.get(u'y2')):
            try:
                #for JS loop
                var.put(u'x', var.get(u'x1'))
                while (var.get(u'x')<var.get(u'x2')):
                    try:
                        var.get(u"this").get(u'bmap').callprop(u'set', var.get(u'x'), var.get(u'y'), Js(255.0))
                    finally:
                            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        return var.get('undefined')
    var.put(u'x1', var.get(u'Math').callprop(u'floor', var.get(u'x1')))
    var.put(u'x2', var.get(u'Math').callprop(u'floor', var.get(u'x2')))
    var.put(u'y1', var.get(u'Math').callprop(u'floor', var.get(u'y1')))
    var.put(u'y2', var.get(u'Math').callprop(u'floor', var.get(u'y2')))
    var.put(u'du', var.get(u'Math').callprop(u'abs', (var.get(u'x2')-var.get(u'x1'))))
    var.put(u'dv', var.get(u'Math').callprop(u'abs', (var.get(u'y2')-var.get(u'y1'))))
    var.put(u'kx', ((-Js(1.0)) if (var.get(u'x2')<var.get(u'x1')) else Js(1.0)))
    var.put(u'ky', ((-Js(1.0)) if (var.get(u'y2')<var.get(u'y1')) else Js(1.0)))
    var.put(u'x', var.get(u'x1'))
    var.put(u'y', var.get(u'y1'))
    var.put(u'd', Js(0.0))
    var.put(u'penw', var.get(u'Math').callprop(u'floor', var.get(u'Math').callprop(u'sqrt', ((var.get(u'penx')*var.get(u'penx'))+(var.get(u'peny')*var.get(u'peny'))))))
    var.put(u'pixh', (var.get(u'Math').callprop(u'round', var.get(u'Math').callprop(u'sqrt', ((var.get(u'penw')*var.get(u'penw'))/(((var.get(u'dv')*var.get(u'dv'))/(var.get(u'du')*var.get(u'du')))+Js(1.0))))) or Js(1.0)))
    var.put(u'pixw', (var.get(u'Math').callprop(u'round', var.get(u'Math').callprop(u'sqrt', ((var.get(u'penw')*var.get(u'penw'))-(var.get(u'pixh')*var.get(u'pixh'))))) or Js(1.0)))
    if (var.get(u'du')>=var.get(u'dv')):
        while (var.get(u'x')!=var.get(u'x2')):
            #for JS loop
            var.put(u'j', Js(0.0))
            while (var.get(u'j')<var.get(u'pixh')):
                try:
                    var.get(u"this").get(u'bmap').callprop(u'set', var.get(u'x'), (var.get(u'y')+var.get(u'j')), Js(255.0))
                finally:
                        (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
            var.put(u'd', var.get(u'dv'), u'+')
            if (var.get(u'd')>=var.get(u'du')):
                var.put(u'd', var.get(u'du'), u'-')
                var.put(u'y', var.get(u'ky'), u'+')
            var.put(u'x', var.get(u'kx'), u'+')
        #for JS loop
        var.put(u'j', Js(0.0))
        while (var.get(u'j')<var.get(u'pixh')):
            try:
                var.get(u"this").get(u'bmap').callprop(u'set', var.get(u'x'), (var.get(u'y')+var.get(u'j')), Js(255.0))
            finally:
                    (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
    else:
        while (var.get(u'y')!=var.get(u'y2')):
            #for JS loop
            var.put(u'j', Js(0.0))
            while (var.get(u'j')<var.get(u'pixw')):
                try:
                    var.get(u"this").get(u'bmap').callprop(u'set', (var.get(u'x')+var.get(u'j')), var.get(u'y'), Js(255.0))
                finally:
                        (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
            var.put(u'd', var.get(u'du'), u'+')
            if (var.get(u'd')>=var.get(u'dv')):
                var.put(u'd', var.get(u'dv'), u'-')
                var.put(u'x', var.get(u'kx'), u'+')
            var.put(u'y', var.get(u'ky'), u'+')
        #for JS loop
        var.put(u'j', Js(0.0))
        while (var.get(u'j')<var.get(u'pixw')):
            try:
                var.get(u"this").get(u'bmap').callprop(u'set', (var.get(u'x')+var.get(u'j')), var.get(u'y'), Js(255.0))
            finally:
                    (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
PyJs_anonymous_36_._set_name(u'anonymous')
var.get(u'BWIPJS').get(u'prototype').put(u'drawline', PyJs_anonymous_36_)
if (PyJsStrictEq(var.get(u'module',throw=False).typeof(),Js(u'object')) and var.get(u'module').get(u'exports')):
    var.get(u'module').put(u'exports', var.get(u'BWIPJS'))
pass


# Add lib to the module scope
bwipjs = var.to_python()