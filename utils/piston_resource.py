'''
Created on 2012-7-9

@author: sea
'''
import piston
from piston.utils import FormValidationError
from django.http import HttpResponse
from piston.resource import Resource
from piston.emitters import Emitter

class PistonResource(Resource):
    '''
    classdocs
    '''
    def error_handler(self, e, request, meth, em_format):
        if isinstance(e, FormValidationError):
            return self.form_validation_response(e,request,em_format)
        else:
            return super(PistonResource,self).error_handler(e,request,meth,em_format)


    def form_validation_response(self, e, request,em_format):
        print 'in form_validation_response 1'
        try:
            emitter, ct = Emitter.get(em_format)
            fields = self.handler.fields
        except ValueError:
            result = piston.utils.rc.BAD_REQUEST
            result.content = "Invalid output format specified '%s'." % em_format
            return result
        serialized_errors = dict((key, [unicode(v) for v in values])
                                for key,values in e.form.errors.items())
        srl = emitter(serialized_errors, piston.handler.typemapper, self.handler, fields, False)
        stream = srl.render(request)
        resp = HttpResponse(stream, mimetype=ct, status=400)
        return resp
