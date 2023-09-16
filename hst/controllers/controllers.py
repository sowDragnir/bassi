# -*- coding: utf-8 -*-
# from odoo import http


# class Hst(http.Controller):
#     @http.route('/hst/hst', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hst/hst/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hst.listing', {
#             'root': '/hst/hst',
#             'objects': http.request.env['hst.hst'].search([]),
#         })

#     @http.route('/hst/hst/objects/<model("hst.hst"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hst.object', {
#             'object': obj
#         })
