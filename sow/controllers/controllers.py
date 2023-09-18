# -*- coding: utf-8 -*-
# from odoo import http


# class Sow(http.Controller):
#     @http.route('/sow/sow', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sow/sow/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sow.listing', {
#             'root': '/sow/sow',
#             'objects': http.request.env['sow.sow'].search([]),
#         })

#     @http.route('/sow/sow/objects/<model("sow.sow"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sow.object', {
#             'object': obj
#         })
