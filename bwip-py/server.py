__all__ = ['server']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([u'fs', u'http', u'bwipjs', u'hostname', u'path', u'port'])
var.put(u'http', var.get(u'require')(Js(u'http')))
var.put(u'bwipjs', var.get(u'require')(Js(u'./node-bwipjs')))
var.put(u'fs', var.get(u'require')(Js(u'fs')))
var.put(u'path', var.get(u'require')(Js(u'path')))
var.put(u'hostname', Js(u'127.0.0.1'))
var.put(u'port', Js(3030.0))
var.get(u'bwipjs').callprop(u'loadFont', Js(u'Inconsolata'), Js(108.0), var.get(u'fs').callprop(u'readFileSync', var.get(u'path').callprop(u'resolve', var.get(u'__dirname'), Js(u'fonts/Inconsolata.otf')), Js(u'binary')))
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({u'this':this, u'arguments':arguments}, var)
    var.registers([])
    var.get(u'console').callprop(u'log', Js(u'BWIP-JS listening on http://%s:%s/'), var.get(u'hostname'), var.get(u'port'))
PyJs_anonymous_0_._set_name(u'anonymous')
@Js
def PyJs_anonymous_1_(req, res, this, arguments, var=var):
    var = Scope({u'this':this, u'res':res, u'req':req, u'arguments':arguments}, var)
    var.registers([u'res', u'req'])
    if PyJsStrictNeq(var.get(u'req').get(u'url').callprop(u'indexOf', Js(u'/?bcid=')),Js(0.0)):
        PyJs_Object_2_ = Js({u'Content-Type':Js(u'text/plain')})
        var.get(u'res').callprop(u'writeHead', Js(404.0), PyJs_Object_2_)
        var.get(u'res').callprop(u'end', Js(u'BWIP-JS: Unknown request format.'), Js(u'utf8'))
    else:
        PyJs_Object_3_ = Js({u'sizelimit':(Js(1024.0)*Js(1024.0))})
        var.get(u'bwipjs')(var.get(u'req'), var.get(u'res'), PyJs_Object_3_)
PyJs_anonymous_1_._set_name(u'anonymous')
var.get(u'http').callprop(u'createServer', PyJs_anonymous_1_).callprop(u'listen', var.get(u'port'), var.get(u'hostname'), PyJs_anonymous_0_)
pass


# Add lib to the module scope
server = var.to_python()