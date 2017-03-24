__all__ = ['node-zlibPNG']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'zlib', u'crcCalc'])
var.put(u'zlib', var.get(u'require')(Js(u'zlib')))
var.put(u'crcCalc', Js([]))
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([u'i', u'c', u'j'])
    #for JS loop
    var.put(u'i', Js(0.0))
    while (var.get(u'i')<Js(256.0)):
        try:
            var.put(u'c', var.get(u'i'))
            #for JS loop
            var.put(u'j', Js(0.0))
            while (var.get(u'j')<Js(8.0)):
                try:
                    if (var.get(u'c')&Js(1.0)):
                        var.put(u'c', (Js(3988292384)^PyJsBshift(var.get(u'c'),Js(1.0))))
                    else:
                        var.put(u'c', PyJsBshift(var.get(u'c'),Js(1.0)))
                finally:
                        (var.put(u'j',Js(var.get(u'j').to_number())+Js(1))-Js(1))
            var.get(u'crcCalc').put(var.get(u'i'), var.get(u'c'))
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
PyJs_anonymous_0_._set_name(u'anonymous')
PyJs_anonymous_0_()
@Js
def PyJs_anonymous_1_(width, height, bgcolor, this, arguments, var=var):
    var = Scope({u'this':this, u'width':width, u'bgcolor':bgcolor, u'arguments':arguments, u'height':height}, var)
    var.registers([u'_palette', u'_nset', u'_gray', u'toGrayScale', u'toTrueAlpha', u'_ncolors', u'i', u'TEXT', u'_pixels', u'bgcolor', u'height', u'toGrayAlpha', u'_trans', u'toTrueColor', u'_cmap', u'width', u'toPalette'])
    @Js
    def PyJsHoisted_toGrayAlpha_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'c', u'pos', u'y', u'x', u'buf', u'row'])
        var.put(u'buf', var.get(u'Buffer').create((((var.get(u'width')*Js(2.0))+Js(1.0))*var.get(u'height'))))
        var.put(u'pos', Js(0.0))
        #for JS loop
        var.put(u'y', Js(0.0))
        while (var.get(u'y')<var.get(u'height')):
            try:
                var.put(u'row', (var.get(u'y')*var.get(u'width')))
                var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), Js(0.0))
                #for JS loop
                var.put(u'x', Js(0.0))
                while (var.get(u'x')<var.get(u'width')):
                    try:
                        var.put(u'c', (var.get(u'_pixels').get((var.get(u'row')+var.get(u'x'))) or Js(0.0)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (var.get(u'c')&Js(255)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (PyJsBshift(var.get(u'c'),Js(24.0))&Js(255)))
                    finally:
                            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        return var.get(u'buf')
    PyJsHoisted_toGrayAlpha_.func_name = u'toGrayAlpha'
    var.put(u'toGrayAlpha', PyJsHoisted_toGrayAlpha_)
    @Js
    def PyJsHoisted_toTrueColor_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'c', u'pos', u'y', u'x', u'buf', u'row'])
        var.put(u'buf', var.get(u'Buffer').create((((var.get(u'width')*Js(3.0))+Js(1.0))*var.get(u'height'))))
        var.put(u'pos', Js(0.0))
        #for JS loop
        var.put(u'y', Js(0.0))
        while (var.get(u'y')<var.get(u'height')):
            try:
                var.put(u'row', (var.get(u'y')*var.get(u'width')))
                var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), Js(0.0))
                #for JS loop
                var.put(u'x', Js(0.0))
                while (var.get(u'x')<var.get(u'width')):
                    try:
                        var.put(u'c', (var.get(u'_pixels').get((var.get(u'row')+var.get(u'x'))) or Js(0.0)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (PyJsBshift(var.get(u'c'),Js(16.0))&Js(255)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (PyJsBshift(var.get(u'c'),Js(8.0))&Js(255)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (var.get(u'c')&Js(255)))
                    finally:
                            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        return var.get(u'buf')
    PyJsHoisted_toTrueColor_.func_name = u'toTrueColor'
    var.put(u'toTrueColor', PyJsHoisted_toTrueColor_)
    @Js
    def PyJsHoisted_toPalette_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'color', u'pos', u'y', u'x', u'buf', u'row'])
        for PyJsTemp in var.get(u'_palette'):
            var.put(u'color', PyJsTemp)
            var.get(u'_cmap').put(var.get(u'_palette').get(var.get(u'color')), var.get(u'color'))
        var.put(u'buf', var.get(u'Buffer').create(((var.get(u'width')+Js(1.0))*var.get(u'height'))))
        var.put(u'pos', Js(0.0))
        #for JS loop
        var.put(u'y', Js(0.0))
        while (var.get(u'y')<var.get(u'height')):
            try:
                var.put(u'row', (var.get(u'y')*var.get(u'width')))
                var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), Js(0.0))
                #for JS loop
                var.put(u'x', Js(0.0))
                while (var.get(u'x')<var.get(u'width')):
                    try:
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), var.get(u'_palette').get((var.get(u'_pixels').get((var.get(u'row')+var.get(u'x'))) or Js(0.0))))
                    finally:
                            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        return var.get(u'buf')
    PyJsHoisted_toPalette_.func_name = u'toPalette'
    var.put(u'toPalette', PyJsHoisted_toPalette_)
    @Js
    def PyJsHoisted_toTrueAlpha_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'c', u'pos', u'y', u'x', u'buf', u'row'])
        var.put(u'buf', var.get(u'Buffer').create((((var.get(u'width')*Js(4.0))+Js(1.0))*var.get(u'height'))))
        var.put(u'pos', Js(0.0))
        #for JS loop
        var.put(u'y', Js(0.0))
        while (var.get(u'y')<var.get(u'height')):
            try:
                var.put(u'row', (var.get(u'y')*var.get(u'width')))
                var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), Js(0.0))
                #for JS loop
                var.put(u'x', Js(0.0))
                while (var.get(u'x')<var.get(u'width')):
                    try:
                        var.put(u'c', (var.get(u'_pixels').get((var.get(u'row')+var.get(u'x'))) or Js(0.0)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (PyJsBshift(var.get(u'c'),Js(16.0))&Js(255)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (PyJsBshift(var.get(u'c'),Js(8.0))&Js(255)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (var.get(u'c')&Js(255)))
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), (PyJsBshift(var.get(u'c'),Js(24.0))&Js(255)))
                    finally:
                            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        return var.get(u'buf')
    PyJsHoisted_toTrueAlpha_.func_name = u'toTrueAlpha'
    var.put(u'toTrueAlpha', PyJsHoisted_toTrueAlpha_)
    @Js
    def PyJsHoisted_toGrayScale_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'y', u'x', u'buf', u'pos', u'row'])
        var.put(u'buf', var.get(u'Buffer').create(((var.get(u'width')+Js(1.0))*var.get(u'height'))))
        var.put(u'pos', Js(0.0))
        #for JS loop
        var.put(u'y', Js(0.0))
        while (var.get(u'y')<var.get(u'height')):
            try:
                var.put(u'row', (var.get(u'y')*var.get(u'width')))
                var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), Js(0.0))
                #for JS loop
                var.put(u'x', Js(0.0))
                while (var.get(u'x')<var.get(u'width')):
                    try:
                        var.get(u'buf').put((var.put(u'pos',Js(var.get(u'pos').to_number())+Js(1))-Js(1)), ((var.get(u'_pixels').get((var.get(u'row')+var.get(u'x'))) or Js(0.0))&Js(255)))
                    finally:
                            (var.put(u'x',Js(var.get(u'x').to_number())+Js(1))-Js(1))
            finally:
                    (var.put(u'y',Js(var.get(u'y').to_number())+Js(1))-Js(1))
        return var.get(u'buf')
    PyJsHoisted_toGrayScale_.func_name = u'toGrayScale'
    var.put(u'toGrayScale', PyJsHoisted_toGrayScale_)
    var.put(u'width', (var.get(u'width')|Js(0.0)))
    var.put(u'height', (var.get(u'height')|Js(0.0)))
    var.put(u'TEXT', Js(u'Software\x00bwip-js.metafloor.com'))
    var.put(u'_pixels', Js([]))
    PyJs_Object_2_ = Js({u'0':Js(0.0)})
    var.put(u'_palette', PyJs_Object_2_)
    var.put(u'_ncolors', Js(1.0))
    var.put(u'_cmap', Js([]))
    var.put(u'_trans', Js(False))
    var.put(u'_gray', Js(False))
    var.put(u'_nset', Js(0.0))
    if PyJsStrictNeq(var.get(u'bgcolor'),var.get(u'undefined')):
        var.put(u'bgcolor', PyJsBshift((Js(4278190080)|var.get(u'bgcolor')),Js(0.0)))
        var.put(u'_gray', (((PyJsBshift(var.get(u'bgcolor'),Js(16.0))&Js(255))==(var.get(u'bgcolor')&Js(255))) and ((PyJsBshift(var.get(u'bgcolor'),Js(8.0))&Js(255))==(var.get(u'bgcolor')&Js(255)))))
        var.put(u'_nset', (var.get(u'width')*var.get(u'height')))
        PyJs_Object_3_ = Js({})
        var.put(u'_palette', PyJs_Object_3_)
        var.get(u'_palette').put(var.get(u'bgcolor'), Js(0.0))
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<var.get(u'_nset')):
            try:
                var.get(u'_pixels').put(var.get(u'i'), var.get(u'bgcolor'))
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    @Js
    def PyJs_anonymous_4_(x, y, c, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'c':c, u'this':this, u'arguments':arguments}, var)
        var.registers([u'y', u'x', u'c'])
        var.get(u"this").callprop(u'set', var.get(u'x'), var.get(u'y'), PyJsBshift((Js(4278190080)|var.get(u'c')),Js(0.0)))
    PyJs_anonymous_4_._set_name(u'anonymous')
    var.get(u"this").put(u'setRGB', PyJs_anonymous_4_)
    @Js
    def PyJs_anonymous_5_(x, y, clr, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments, u'clr':clr}, var)
        var.registers([u'clrr', u'curr', u'cur', u'clrb', u'newb', u'newa', u'newg', u'y', u'curg', u'clra', u'curb', u'x', u'cura', u'newr', u'clrg', u'clr'])
        var.put(u'cur', var.get(u'_pixels').get(((var.get(u'y')*var.get(u'width'))+var.get(u'x'))))
        if PyJsStrictEq(var.get(u'cur'),var.get(u'undefined')):
            (var.put(u'_nset',Js(var.get(u'_nset').to_number())+Js(1))-Js(1))
        else:
            var.put(u'cura', (PyJsBshift(var.get(u'cur'),Js(24.0))/Js(255.0)))
            var.put(u'curr', (PyJsBshift(var.get(u'cur'),Js(16.0))&Js(255)))
            var.put(u'curg', (PyJsBshift(var.get(u'cur'),Js(8.0))&Js(255)))
            var.put(u'curb', (var.get(u'cur')&Js(255)))
            var.put(u'clra', (PyJsBshift(var.get(u'clr'),Js(24.0))/Js(255.0)))
            var.put(u'clrr', (PyJsBshift(var.get(u'clr'),Js(16.0))&Js(255)))
            var.put(u'clrg', (PyJsBshift(var.get(u'clr'),Js(8.0))&Js(255)))
            var.put(u'clrb', (var.get(u'clr')&Js(255)))
            var.put(u'newa', (var.get(u'clra')+(var.get(u'cura')*(Js(1.0)-var.get(u'clra')))))
            if var.get(u'newa').neg():
                var.put(u'clr', Js(0.0))
            else:
                var.put(u'newr', ((((var.get(u'clrr')*var.get(u'clra'))+((var.get(u'curr')*var.get(u'cura'))*(Js(1.0)-var.get(u'clra'))))/var.get(u'newa'))|Js(0.0)))
                var.put(u'newg', ((((var.get(u'clrg')*var.get(u'clra'))+((var.get(u'curg')*var.get(u'cura'))*(Js(1.0)-var.get(u'clra'))))/var.get(u'newa'))|Js(0.0)))
                var.put(u'newb', ((((var.get(u'clrb')*var.get(u'clra'))+((var.get(u'curb')*var.get(u'cura'))*(Js(1.0)-var.get(u'clra'))))/var.get(u'newa'))|Js(0.0)))
                var.put(u'clr', PyJsBshift(((((((var.get(u'newa')*Js(255.0))|Js(0.0))<<Js(24.0))|(var.get(u'newr')<<Js(16.0)))|(var.get(u'newg')<<Js(8.0)))|var.get(u'newb')),Js(0.0)))
        var.put(u'_gray', ((var.get(u'_gray') and ((PyJsBshift(var.get(u'clr'),Js(16.0))&Js(255))==(var.get(u'clr')&Js(255)))) and ((PyJsBshift(var.get(u'clr'),Js(8.0))&Js(255))==(var.get(u'clr')&Js(255)))))
        var.put(u'_trans', (var.get(u'_trans') or (PyJsBshift(var.get(u'clr'),Js(24.0))<Js(255.0))))
        if ((var.get(u'_ncolors')<=Js(256.0)) and PyJsStrictEq(var.get(u'_palette').get(var.get(u'clr')),var.get(u'undefined'))):
            var.get(u'_palette').put(var.get(u'clr'), (var.put(u'_ncolors',Js(var.get(u'_ncolors').to_number())+Js(1))-Js(1)))
        var.get(u'_pixels').put(((var.get(u'y')*var.get(u'width'))+var.get(u'x')), var.get(u'clr'))
    PyJs_anonymous_5_._set_name(u'anonymous')
    var.get(u"this").put(u'set', PyJs_anonymous_5_)
    @Js
    def PyJs_anonymous_6_(x, y, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'this':this, u'arguments':arguments}, var)
        var.registers([u'y', u'x'])
        return (var.get(u'_pixels').get(((var.get(u'y')*var.get(u'width'))+var.get(u'x'))) or Js(0.0))
    PyJs_anonymous_6_._set_name(u'anonymous')
    var.get(u"this").put(u'get', PyJs_anonymous_6_)
    @Js
    def PyJs_anonymous_7_(callback, this, arguments, var=var):
        var = Scope({u'this':this, u'callback':callback, u'arguments':arguments}, var)
        var.registers([u'returnPNG', u'bufs', u'callback', u'deflator', u'blen', u'image'])
        @Js
        def PyJsHoisted_returnPNG_(data, this, arguments, var=var):
            var = Scope({u'this':this, u'data':data, u'arguments':arguments}, var)
            var.registers([u'writeTEXT', u'writeIDAT', u'write8', u'writePLTE', u'pngoff', u'data', u'write', u'write32', u'length', u'writeIHDR', u'writeCRC', u'write16', u'writeIEND', u'png', u'writeTRNS'])
            @Js
            def PyJsHoisted_writeTEXT_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u'crcoff'])
                var.get(u'write32')(var.get(u'TEXT').get(u'length'))
                var.put(u'crcoff', var.get(u'pngoff'))
                var.get(u'write')(Js(u'tEXt'))
                var.get(u'write')(var.get(u'TEXT'))
                var.get(u'writeCRC')(var.get(u'crcoff'))
            PyJsHoisted_writeTEXT_.func_name = u'writeTEXT'
            var.put(u'writeTEXT', PyJsHoisted_writeTEXT_)
            @Js
            def PyJsHoisted_writeIDAT_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u'crcoff'])
                var.get(u'write32')(var.get(u'data').get(u'length'))
                var.put(u'crcoff', var.get(u'pngoff'))
                var.get(u'write')(Js(u'IDAT'))
                var.get(u'data').callprop(u'copy', var.get(u'png'), var.get(u'pngoff'))
                var.put(u'pngoff', var.get(u'data').get(u'length'), u'+')
                var.get(u'writeCRC')(var.get(u'crcoff'))
            PyJsHoisted_writeIDAT_.func_name = u'writeIDAT'
            var.put(u'writeIDAT', PyJsHoisted_writeIDAT_)
            @Js
            def PyJsHoisted_write8_(v, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'v':v}, var)
                var.registers([u'v'])
                var.get(u'png').put((var.put(u'pngoff',Js(var.get(u'pngoff').to_number())+Js(1))-Js(1)), var.get(u'v'))
            PyJsHoisted_write8_.func_name = u'write8'
            var.put(u'write8', PyJsHoisted_write8_)
            @Js
            def PyJsHoisted_writePLTE_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u'i', u'c', u'crcoff'])
                var.get(u'write32')((var.get(u'_ncolors')*Js(3.0)))
                var.put(u'crcoff', var.get(u'pngoff'))
                var.get(u'write')(Js(u'PLTE'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'_cmap').get(u'length')):
                    try:
                        var.put(u'c', var.get(u'_cmap').get(var.get(u'i')))
                        var.get(u'write8')((PyJsBshift(var.get(u'c'),Js(16.0))&Js(255)))
                        var.get(u'write8')((PyJsBshift(var.get(u'c'),Js(8.0))&Js(255)))
                        var.get(u'write8')((var.get(u'c')&Js(255)))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                var.get(u'writeCRC')(var.get(u'crcoff'))
            PyJsHoisted_writePLTE_.func_name = u'writePLTE'
            var.put(u'writePLTE', PyJsHoisted_writePLTE_)
            @Js
            def PyJsHoisted_write_(s, this, arguments, var=var):
                var = Scope({u'this':this, u's':s, u'arguments':arguments}, var)
                var.registers([u's'])
                var.get(u'png').callprop(u'write', var.get(u's'), var.get(u'pngoff'), Js(u'binary'))
                var.put(u'pngoff', var.get(u's').get(u'length'), u'+')
            PyJsHoisted_write_.func_name = u'write'
            var.put(u'write', PyJsHoisted_write_)
            @Js
            def PyJsHoisted_write32_(v, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'v':v}, var)
                var.registers([u'v'])
                var.get(u'png').callprop(u'writeUInt32BE', var.get(u'v'), var.get(u'pngoff'))
                var.put(u'pngoff', Js(4.0), u'+')
            PyJsHoisted_write32_.func_name = u'write32'
            var.put(u'write32', PyJsHoisted_write32_)
            @Js
            def PyJsHoisted_writeIHDR_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u'crcoff'])
                var.get(u'write32')(Js(13.0))
                var.put(u'crcoff', var.get(u'pngoff'))
                var.get(u'write')(Js(u'IHDR'))
                var.get(u'write32')(var.get(u'width'))
                var.get(u'write32')(var.get(u'height'))
                var.get(u'write8')(Js(8.0))
                if (var.get(u'_gray') and var.get(u'_trans').neg()):
                    var.get(u'write8')(Js(0.0))
                else:
                    if (var.get(u'_ncolors')<=Js(256.0)):
                        var.get(u'write8')(Js(3.0))
                    else:
                        if var.get(u'_gray'):
                            var.get(u'write8')(Js(4.0))
                        else:
                            if var.get(u'_trans'):
                                var.get(u'write8')(Js(6.0))
                            else:
                                var.get(u'write8')(Js(2.0))
                var.get(u'write8')(Js(0.0))
                var.get(u'write8')(Js(0.0))
                var.get(u'write8')(Js(0.0))
                var.get(u'writeCRC')(var.get(u'crcoff'))
            PyJsHoisted_writeIHDR_.func_name = u'writeIHDR'
            var.put(u'writeIHDR', PyJsHoisted_writeIHDR_)
            @Js
            def PyJsHoisted_writeCRC_(off, this, arguments, var=var):
                var = Scope({u'this':this, u'off':off, u'arguments':arguments}, var)
                var.registers([u'crc', u'off'])
                var.put(u'crc', (-Js(1.0)))
                while (var.get(u'off')<var.get(u'pngoff')):
                    var.put(u'crc', (var.get(u'crcCalc').get(((var.get(u'crc')^var.get(u'png').get((var.put(u'off',Js(var.get(u'off').to_number())+Js(1))-Js(1))))&Js(255)))^PyJsBshift(var.get(u'crc'),Js(8.0))))
                var.get(u'write32')(PyJsBshift((var.get(u'crc')^(-Js(1.0))),Js(0.0)))
            PyJsHoisted_writeCRC_.func_name = u'writeCRC'
            var.put(u'writeCRC', PyJsHoisted_writeCRC_)
            @Js
            def PyJsHoisted_write16_(v, this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments, u'v':v}, var)
                var.registers([u'v'])
                var.get(u'png').callprop(u'writeUInt16BE', var.get(u'v'), var.get(u'pngoff'))
                var.put(u'pngoff', Js(2.0), u'+')
            PyJsHoisted_write16_.func_name = u'write16'
            var.put(u'write16', PyJsHoisted_write16_)
            @Js
            def PyJsHoisted_writeIEND_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u'crcoff'])
                var.get(u'write32')(Js(0.0))
                var.put(u'crcoff', var.get(u'pngoff'))
                var.get(u'write')(Js(u'IEND'))
                var.get(u'writeCRC')(var.get(u'crcoff'))
            PyJsHoisted_writeIEND_.func_name = u'writeIEND'
            var.put(u'writeIEND', PyJsHoisted_writeIEND_)
            @Js
            def PyJsHoisted_writeTRNS_(this, arguments, var=var):
                var = Scope({u'this':this, u'arguments':arguments}, var)
                var.registers([u'i', u'crcoff'])
                var.get(u'write32')(var.get(u'_ncolors'))
                var.put(u'crcoff', var.get(u'pngoff'))
                var.get(u'write')(Js(u'tRNS'))
                #for JS loop
                var.put(u'i', Js(0.0))
                while (var.get(u'i')<var.get(u'_cmap').get(u'length')):
                    try:
                        var.get(u'write8')((PyJsBshift(var.get(u'_cmap').get(var.get(u'i')),Js(24.0))&Js(255)))
                    finally:
                            (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
                var.get(u'writeCRC')(var.get(u'crcoff'))
            PyJsHoisted_writeTRNS_.func_name = u'writeTRNS'
            var.put(u'writeTRNS', PyJsHoisted_writeTRNS_)
            var.put(u'length', (((((((Js(8.0)+Js(12.0))+Js(13.0))+Js(12.0))+var.get(u'TEXT').get(u'length'))+Js(12.0))+var.get(u'data').get(u'length'))+Js(12.0)))
            if (var.get(u'_gray') and var.get(u'_trans').neg()):
                pass
            else:
                if (var.get(u'_ncolors')<=Js(256.0)):
                    var.put(u'length', (Js(12.0)+(Js(3.0)*var.get(u'_ncolors'))), u'+')
                    if var.get(u'_trans'):
                        var.put(u'length', (Js(12.0)+var.get(u'_ncolors')), u'+')
            var.put(u'png', var.get(u'Buffer').create(var.get(u'length')))
            var.put(u'pngoff', Js(0.0))
            var.get(u'write')(Js(u'\x89PNG\r\n\x1a\n'))
            var.get(u'writeIHDR')()
            var.get(u'writeTEXT')()
            if (var.get(u'_gray') and var.get(u'_trans').neg()):
                pass
            else:
                if (var.get(u'_ncolors')<=Js(256.0)):
                    var.get(u'writePLTE')()
                    if var.get(u'_trans'):
                        var.get(u'writeTRNS')()
            var.get(u'writeIDAT')()
            var.get(u'writeIEND')()
            var.get(u'callback')(var.get(u"null"), var.get(u'png'))
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
            pass
        PyJsHoisted_returnPNG_.func_name = u'returnPNG'
        var.put(u'returnPNG', PyJsHoisted_returnPNG_)
        var.put(u'_trans', (var.get(u'_trans') or (var.get(u'_nset')<(var.get(u'width')*var.get(u'height')))))
        pass
        if (var.get(u'_gray') and var.get(u'_trans').neg()):
            var.put(u'image', var.get(u'toGrayScale')())
        else:
            if (var.get(u'_ncolors')<=Js(256.0)):
                var.put(u'image', var.get(u'toPalette')())
            else:
                if var.get(u'_gray'):
                    var.put(u'image', var.get(u'toGrayAlpha')())
                else:
                    var.put(u'image', (var.get(u'toTrueAlpha')() if var.get(u'_trans') else var.get(u'toTrueColor')()))
        var.put(u'bufs', Js([]))
        var.put(u'blen', Js(0.0))
        PyJs_Object_8_ = Js({u'chunkSize':(Js(32.0)*Js(1024.0)),u'level':var.get(u'zlib').get(u'Z_DEFAULT_COMPRESSION'),u'strategy':var.get(u'zlib').get(u'Z_DEFAULT_STRATEGY')})
        var.put(u'deflator', var.get(u'zlib').callprop(u'createDeflate', PyJs_Object_8_))
        var.get(u'deflator').callprop(u'on', Js(u'error'), var.get(u'callback'))
        @Js
        def PyJs_anonymous_9_(data, this, arguments, var=var):
            var = Scope({u'this':this, u'data':data, u'arguments':arguments}, var)
            var.registers([u'data'])
            var.get(u'bufs').callprop(u'push', var.get(u'data'))
            var.put(u'blen', var.get(u'data').get(u'length'), u'+')
        PyJs_anonymous_9_._set_name(u'anonymous')
        var.get(u'deflator').callprop(u'on', Js(u'data'), PyJs_anonymous_9_)
        @Js
        def PyJs_anonymous_10_(this, arguments, var=var):
            var = Scope({u'this':this, u'arguments':arguments}, var)
            var.registers([])
            var.get(u'returnPNG')(var.get(u'Buffer').callprop(u'concat', var.get(u'bufs'), var.get(u'blen')))
        PyJs_anonymous_10_._set_name(u'anonymous')
        var.get(u'deflator').callprop(u'on', Js(u'end'), PyJs_anonymous_10_)
        var.get(u'deflator').callprop(u'end', var.get(u'image'))
        pass
    PyJs_anonymous_7_._set_name(u'anonymous')
    var.get(u"this").put(u'render', PyJs_anonymous_7_)
    pass
    pass
    pass
    pass
    pass
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'module').put(u'exports', PyJs_anonymous_1_)


# Add lib to the module scope
node-zlibPNG = var.to_python()