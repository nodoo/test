__all__ = ['node-bwipjs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'freetype', u'bwipjs', u'url', u'zlibPNG', u'Bitmap', u'bwipp'])
@Js
def PyJsHoisted_Bitmap_(bgcolor, this, arguments, var=var):
    var = Scope({u'this':this, u'bgcolor':bgcolor, u'arguments':arguments}, var)
    var.registers([u'_pixs', u'_sizelim', u'_clrr', u'_minx', u'bgcolor', u'_clrg', u'_miny', u'_clrb', u'_maxx', u'_maxy', u'_pady', u'_padx'])
    var.put(u'_clrr', Js(0.0))
    var.put(u'_clrg', Js(0.0))
    var.put(u'_clrb', Js(0.0))
    PyJs_Object_9_ = Js({})
    var.put(u'_pixs', PyJs_Object_9_)
    var.put(u'_minx', var.get(u'Infinity'))
    var.put(u'_miny', var.get(u'Infinity'))
    var.put(u'_maxx', Js(0.0))
    var.put(u'_maxy', Js(0.0))
    var.put(u'_padx', Js(0.0))
    var.put(u'_pady', Js(0.0))
    var.put(u'_sizelim', Js(0.0))
    if PyJsStrictEq(var.get(u'bgcolor',throw=False).typeof(),Js(u'string')):
        var.put(u'bgcolor', PyJsBshift((Js(4278190080)|var.get(u'parseInt')(var.get(u'bgcolor'), Js(16.0))),Js(0.0)))
    else:
        if PyJsStrictNeq(var.get(u'bgcolor'),var.get(u'undefined')):
            var.put(u'bgcolor', PyJsBshift((Js(4278190080)|var.get(u'bgcolor')),Js(0.0)))
    @Js
    def PyJs_anonymous_10_(width, height, this, arguments, var=var):
        var = Scope({u'this':this, u'width':width, u'arguments':arguments, u'height':height}, var)
        var.registers([u'width', u'height'])
        var.put(u'_padx', (var.get(u'width')|Js(0.0)))
        var.put(u'_pady', (var.get(u'height')|Js(0.0)))
    PyJs_anonymous_10_._set_name(u'anonymous')
    var.get(u"this").put(u'pad', PyJs_anonymous_10_)
    @Js
    def PyJs_anonymous_11_(size, this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments, u'size':size}, var)
        var.registers([u'size'])
        var.put(u'_sizelim', var.get(u'size'))
    PyJs_anonymous_11_._set_name(u'anonymous')
    var.get(u"this").put(u'limit', PyJs_anonymous_11_)
    @Js
    def PyJs_anonymous_12_(llx, lly, urx, ury, this, arguments, var=var):
        var = Scope({u'lly':lly, u'llx':llx, u'arguments':arguments, u'this':this, u'urx':urx, u'ury':ury}, var)
        var.registers([u'lly', u'llx', u'urx', u'ury'])
        var.put(u'llx', var.get(u'Math').callprop(u'floor', var.get(u'llx')))
        var.put(u'lly', var.get(u'Math').callprop(u'floor', var.get(u'lly')))
        var.put(u'urx', var.get(u'Math').callprop(u'floor', var.get(u'urx')))
        var.put(u'ury', var.get(u'Math').callprop(u'floor', var.get(u'ury')))
        if (var.get(u'_minx')>var.get(u'llx')):
            var.put(u'_minx', var.get(u'llx'))
        if (var.get(u'_miny')>var.get(u'lly')):
            var.put(u'_miny', var.get(u'lly'))
        if (var.get(u'_maxx')<var.get(u'urx')):
            var.put(u'_maxx', var.get(u'urx'))
        if (var.get(u'_maxy')<var.get(u'ury')):
            var.put(u'_maxy', var.get(u'ury'))
        if (var.get(u'_sizelim') and ((var.get(u'_maxx')*var.get(u'_maxy'))>var.get(u'_sizelim'))):
            PyJsTempException = JsToPyException(Js(u'BWIPJS: image exceeded size limit'))
            raise PyJsTempException
    PyJs_anonymous_12_._set_name(u'anonymous')
    var.get(u"this").put(u'extent', PyJs_anonymous_12_)
    @Js
    def PyJs_anonymous_13_(r, g, b, this, arguments, var=var):
        var = Scope({u'this':this, u'r':r, u'b':b, u'arguments':arguments, u'g':g}, var)
        var.registers([u'r', u'b', u'g'])
        var.put(u'_clrr', var.get(u'r'))
        var.put(u'_clrg', var.get(u'g'))
        var.put(u'_clrb', var.get(u'b'))
    PyJs_anonymous_13_._set_name(u'anonymous')
    var.get(u"this").put(u'color', PyJs_anonymous_13_)
    @Js
    def PyJs_anonymous_14_(x, y, a, this, arguments, var=var):
        var = Scope({u'y':y, u'x':x, u'this':this, u'a':a, u'arguments':arguments}, var)
        var.registers([u'a', u'b', u'y', u'g', u'srca', u'newa', u'dstr', u'dstg', u'cx', u'xy', u'x', u'r', u'dstb', u'dsta'])
        var.put(u'x', var.get(u'Math').callprop(u'floor', var.get(u'x')))
        var.put(u'y', var.get(u'Math').callprop(u'floor', var.get(u'y')))
        if (var.get(u'_minx')>var.get(u'x')):
            var.put(u'_minx', var.get(u'x'))
        if (var.get(u'_maxx')<var.get(u'x')):
            var.put(u'_maxx', var.get(u'x'))
        if (var.get(u'_miny')>var.get(u'y')):
            var.put(u'_miny', var.get(u'y'))
        if (var.get(u'_maxy')<var.get(u'y')):
            var.put(u'_maxy', var.get(u'y'))
        var.put(u'xy', ((var.get(u'x')+Js(u','))+var.get(u'y')))
        var.put(u'cx', var.get(u'_pixs').get(var.get(u'xy')))
        pass
        if PyJsStrictEq(var.get(u'cx'),var.get(u'undefined')):
            var.put(u'cx', var.get(u'bgcolor'))
        if PyJsStrictEq(var.get(u'cx'),var.get(u'undefined')):
            var.put(u'r', var.get(u'_clrr'))
            var.put(u'g', var.get(u'_clrg'))
            var.put(u'b', var.get(u'_clrb'))
        else:
            var.put(u'dsta', (PyJsBshift(var.get(u'cx'),Js(24.0))/Js(255.0)))
            var.put(u'dstr', (PyJsBshift(var.get(u'cx'),Js(16.0))&Js(255)))
            var.put(u'dstg', (PyJsBshift(var.get(u'cx'),Js(8.0))&Js(255)))
            var.put(u'dstb', (var.get(u'cx')&Js(255)))
            var.put(u'srca', (var.get(u'a')/Js(255.0)))
            var.put(u'newa', (var.get(u'srca')+(var.get(u'dsta')*(Js(1.0)-var.get(u'srca')))))
            if var.get(u'newa').neg():
                var.put(u'r', var.put(u'g', var.put(u'b', var.put(u'a', Js(0.0)))))
            else:
                var.put(u'r', ((((var.get(u'_clrr')*var.get(u'srca'))+((var.get(u'dstr')*var.get(u'dsta'))*(Js(1.0)-var.get(u'srca'))))/var.get(u'newa'))|Js(0.0)))
                var.put(u'g', ((((var.get(u'_clrg')*var.get(u'srca'))+((var.get(u'dstg')*var.get(u'dsta'))*(Js(1.0)-var.get(u'srca'))))/var.get(u'newa'))|Js(0.0)))
                var.put(u'b', ((((var.get(u'_clrb')*var.get(u'srca'))+((var.get(u'dstb')*var.get(u'dsta'))*(Js(1.0)-var.get(u'srca'))))/var.get(u'newa'))|Js(0.0)))
                var.put(u'a', ((var.get(u'newa')*Js(255.0))|Js(0.0)))
        var.get(u'_pixs').put(var.get(u'xy'), PyJsBshift(((((var.get(u'a')<<Js(24.0))|(var.get(u'r')<<Js(16.0)))|(var.get(u'g')<<Js(8.0)))|var.get(u'b')),Js(0.0)))
    PyJs_anonymous_14_._set_name(u'anonymous')
    var.get(u"this").put(u'set', PyJs_anonymous_14_)
    @Js
    def PyJs_anonymous_15_(rot, callback, this, arguments, var=var):
        var = Scope({u'this':this, u'callback':callback, u'rot':rot, u'arguments':arguments}, var)
        var.registers([u'h', u'rot', u'callback', u'xy', u't', u'w', u'y', u'x', u'pts', u'png'])
        if ((var.get(u'rot')==Js(u'R')) or (var.get(u'rot')==Js(u'L'))):
            var.put(u'h', ((var.get(u'_maxx')-var.get(u'_minx'))+Js(1.0)))
            var.put(u'w', ((var.get(u'_maxy')-var.get(u'_miny'))+Js(1.0)))
            var.put(u't', var.get(u'_pady'))
            var.put(u'_pady', var.get(u'_padx'))
            var.put(u'_padx', var.get(u't'))
        else:
            var.put(u'w', ((var.get(u'_maxx')-var.get(u'_minx'))+Js(1.0)))
            var.put(u'h', ((var.get(u'_maxy')-var.get(u'_miny'))+Js(1.0)))
        var.put(u'png', var.get(u'zlibPNG').create((var.get(u'w')+(Js(2.0)*var.get(u'_padx'))), (var.get(u'h')+(Js(2.0)*var.get(u'_pady'))), var.get(u'bgcolor')))
        for PyJsTemp in var.get(u'_pixs'):
            var.put(u'xy', PyJsTemp)
            var.put(u'pts', var.get(u'xy').callprop(u'split', Js(u',')))
            var.put(u'x', ((+var.get(u'pts').get(u'0'))-var.get(u'_minx')))
            var.put(u'y', ((+var.get(u'pts').get(u'1'))-var.get(u'_miny')))
            if (var.get(u'rot')==Js(u'N')):
                var.put(u'y', ((var.get(u'h')-var.get(u'y'))-Js(1.0)))
            else:
                if (var.get(u'rot')==Js(u'I')):
                    var.put(u'x', ((var.get(u'w')-var.get(u'x'))-Js(1.0)))
                else:
                    var.put(u'y', (var.get(u'w')-var.get(u'y')))
                    if (var.get(u'rot')==Js(u'L')):
                        var.put(u't', var.get(u'y'))
                        var.put(u'y', ((var.get(u'h')-var.get(u'x'))-Js(1.0)))
                        var.put(u'x', (var.get(u't')-Js(1.0)))
                    else:
                        var.put(u't', var.get(u'x'))
                        var.put(u'x', (var.get(u'w')-var.get(u'y')))
                        var.put(u'y', var.get(u't'))
            var.get(u'png').callprop(u'set', (var.get(u'x')+var.get(u'_padx')), (var.get(u'y')+var.get(u'_pady')), var.get(u'_pixs').get(var.get(u'xy')))
        return var.get(u'png').callprop(u'render', var.get(u'callback'))
    PyJs_anonymous_15_._set_name(u'anonymous')
    var.get(u"this").put(u'getPNG', PyJs_anonymous_15_)
PyJsHoisted_Bitmap_.func_name = u'Bitmap'
var.put(u'Bitmap', PyJsHoisted_Bitmap_)
var.put(u'url', var.get(u'require')(Js(u'url')))
var.put(u'bwipp', var.get(u'require')((var.get(u'__dirname')+Js(u'/bwipp'))))
var.put(u'bwipjs', var.get(u'require')((var.get(u'__dirname')+Js(u'/bwipjs'))))
var.put(u'zlibPNG', var.get(u'require')((var.get(u'__dirname')+Js(u'/node-zlibPNG'))))
var.put(u'freetype', var.get(u'require')((var.get(u'__dirname')+Js(u'/freetype'))))
@Js
def PyJs_anonymous_0_(req, res, opts, this, arguments, var=var):
    var = Scope({u'this':this, u'res':res, u'req':req, u'arguments':arguments, u'opts':opts}, var)
    var.registers([u'req', u'res', u'args', u'id', u'opts'])
    var.put(u'args', var.get(u'url').callprop(u'parse', var.get(u'req').get(u'url'), var.get(u'true')).get(u'query'))
    for PyJsTemp in var.get(u'args'):
        var.put(u'id', PyJsTemp)
        if PyJsStrictEq(var.get(u'args').get(var.get(u'id')),Js(u'')):
            var.get(u'args').put(var.get(u'id'), var.get(u'true'))
    PyJs_Object_1_ = Js({})
    var.put(u'opts', (var.get(u'opts') or PyJs_Object_1_))
    for PyJsTemp in var.get(u'opts'):
        var.put(u'id', PyJsTemp)
        var.get(u'args').put(var.get(u'id'), var.get(u'opts').get(var.get(u'id')))
    @Js
    def PyJs_anonymous_2_(err, png, this, arguments, var=var):
        var = Scope({u'this':this, u'png':png, u'err':err, u'arguments':arguments}, var)
        var.registers([u'png', u'err'])
        if var.get(u'err'):
            PyJs_Object_3_ = Js({u'Content-Type':Js(u'text/plain')})
            var.get(u'res').callprop(u'writeHead', Js(400.0), PyJs_Object_3_)
            var.get(u'res').callprop(u'end', var.get(u'err'), Js(u'ascii'))
        else:
            PyJs_Object_4_ = Js({u'Content-Type':Js(u'image/png')})
            var.get(u'res').callprop(u'writeHead', Js(200.0), PyJs_Object_4_)
            var.get(u'res').callprop(u'end', var.get(u'png'), Js(u'binary'))
    PyJs_anonymous_2_._set_name(u'anonymous')
    var.get(u'module').get(u'exports').callprop(u'toBuffer', var.get(u'args'), PyJs_anonymous_2_)
PyJs_anonymous_0_._set_name(u'anonymous')
var.get(u'module').put(u'exports', PyJs_anonymous_0_)
@Js
def PyJs_anonymous_5_(args, callback, this, arguments, var=var):
    var = Scope({u'this':this, u'callback':callback, u'args':args, u'arguments':arguments}, var)
    var.registers([u'scale', u'mono', u'args', u'scaleX', u'scaleY', u'callback', u'bcid', u'bw', u'text', u'sizelimit', u'rot', u'id', u'opts'])
    var.put(u'scale', (var.get(u'args').get(u'scale') or Js(2.0)))
    var.put(u'scaleX', ((+var.get(u'args').get(u'scaleX')) or var.get(u'scale')))
    var.put(u'scaleY', ((+var.get(u'args').get(u'scaleY')) or var.get(u'scaleX')))
    var.put(u'rot', (var.get(u'args').get(u'rotate') or Js(u'N')))
    var.put(u'mono', (var.get(u'args').get(u'monochrome') or Js(False)))
    var.put(u'sizelimit', ((+var.get(u'args').get(u'sizelimit')) or Js(0.0)))
    var.put(u'bcid', var.get(u'args').get(u'bcid'))
    var.put(u'text', var.get(u'args').get(u'text'))
    if var.get(u'text').neg():
        return var.get(u'callback')(Js(u'Bar code text not specified.'))
    if var.get(u'bcid').neg():
        return var.get(u'callback')(Js(u'Bar code type not specified.'))
    var.get(u'args').delete(u'scale')
    var.get(u'args').delete(u'scaleX')
    var.get(u'args').delete(u'scaleY')
    var.get(u'args').delete(u'rotate')
    var.get(u'args').delete(u'text')
    var.get(u'args').delete(u'bcid')
    var.get(u'args').delete(u'monochrome')
    var.get(u'args').delete(u'sizelimit')
    var.put(u'bw', var.get(u'bwipjs').create(var.get(u'freetype'), var.get(u'mono')))
    PyJs_Object_6_ = Js({})
    var.put(u'opts', PyJs_Object_6_)
    for PyJsTemp in var.get(u'args'):
        var.put(u'id', PyJsTemp)
        var.get(u'opts').put(var.get(u'id'), var.get(u'args').get(var.get(u'id')))
    if var.get(u'opts').get(u'alttext'):
        var.get(u'opts').put(u'includetext', var.get(u'true'))
    if ((+var.get(u'opts').get(u'height')) and (var.get(u'bcid')!=Js(u'pharmacode2'))):
        var.get(u'opts').put(u'height', ((var.get(u'opts').get(u'height')/Js(25.4)) or Js(0.5)))
    if (+var.get(u'opts').get(u'width')):
        var.get(u'opts').put(u'width', ((var.get(u'opts').get(u'width')/Js(25.4)) or Js(0.0)))
    if var.get(u'opts').get(u'backgroundcolor'):
        var.get(u'bw').callprop(u'bitmap', var.get(u'Bitmap').create(var.get(u'parseInt')((Js(u'')+var.get(u'opts').get(u'backgroundcolor')), Js(16.0))))
        var.get(u'opts').delete(u'backgroundcolor')
    else:
        var.get(u'bw').callprop(u'bitmap', var.get(u'Bitmap').create())
    var.get(u'bw').callprop(u'bitmap').callprop(u'limit', var.get(u'sizelimit'))
    var.get(u'bw').callprop(u'bitmap').callprop(u'pad', (((+var.get(u'opts').get(u'paddingwidth'))*var.get(u'scaleX')) or Js(0.0)), (((+var.get(u'opts').get(u'paddingheight'))*var.get(u'scaleY')) or Js(0.0)))
    var.get(u'bw').callprop(u'scale', var.get(u'scaleX'), var.get(u'scaleY'))
    try:
        var.get(u'bwipp')()(var.get(u'bw'), var.get(u'bcid'), var.get(u'text'), var.get(u'opts'))
        var.get(u'bw').callprop(u'bitmap').callprop(u'getPNG', var.get(u'rot'), var.get(u'callback'))
    except PyJsException as PyJsTempException:
        PyJsHolder_65_47606238 = var.own.get(u'e')
        var.force_own_put(u'e', PyExceptionToJs(PyJsTempException))
        try:
            var.get(u'callback')((Js(u'')+var.get(u'e')))
        finally:
            if PyJsHolder_65_47606238 is not None:
                var.own[u'e'] = PyJsHolder_65_47606238
            else:
                del var.own[u'e']
            del PyJsHolder_65_47606238
PyJs_anonymous_5_._set_name(u'anonymous')
var.get(u'module').get(u'exports').put(u'toBuffer', PyJs_anonymous_5_)
@Js
def PyJs_anonymous_7_(fontname, sizemult, fontfile, this, arguments, var=var):
    var = Scope({u'this':this, u'sizemult':sizemult, u'fontname':fontname, u'arguments':arguments, u'fontfile':fontfile}, var)
    var.registers([u'sizemult', u'rv', u'fontname', u'load_font', u'fontfile'])
    var.get(u'freetype').callprop(u'FS_createDataFile', Js(u'/'), var.get(u'fontname'), var.get(u'fontfile'), var.get(u'true'), Js(False))
    var.put(u'load_font', var.get(u'freetype').callprop(u'cwrap', Js(u'load_font'), Js(u'number'), Js([Js(u'string'), Js(u'string'), Js(u'number')])))
    var.put(u'rv', var.get(u'load_font')((Js(u'/')+var.get(u'fontname')), var.get(u'fontname'), var.get(u'sizemult')))
    if (var.get(u'rv')!=Js(0.0)):
        var.get(u'freetype').callprop(u'unlink', (Js(u'/')+var.get(u'fontname')))
        PyJsTempException = JsToPyException(((Js(u'Error: font load failed [')+var.get(u'rv'))+Js(u']')))
        raise PyJsTempException
PyJs_anonymous_7_._set_name(u'anonymous')
var.get(u'module').get(u'exports').put(u'loadFont', PyJs_anonymous_7_)
@Js
def PyJs_anonymous_8_(fontname, this, arguments, var=var):
    var = Scope({u'this':this, u'fontname':fontname, u'arguments':arguments}, var)
    var.registers([u'fontname', u'close_font'])
    var.put(u'close_font', var.get(u'freetype').callprop(u'cwrap', Js(u'close_font'), Js(u'number'), Js([Js(u'string')])))
    var.get(u'close_font')(var.get(u'fontname'))
    var.get(u'freetype').callprop(u'unlink', (Js(u'/')+var.get(u'fontname')))
PyJs_anonymous_8_._set_name(u'anonymous')
var.get(u'module').get(u'exports').put(u'unloadFont', PyJs_anonymous_8_)
var.get(u'module').get(u'exports').put(u'bwipjs_version', Js(u'1.2.3 (2017-01-16)'))
var.get(u'module').get(u'exports').put(u'bwipp_version', Js(u'2016-12-16'))
pass
pass


# Add lib to the module scope
node-bwipjs = var.to_python()