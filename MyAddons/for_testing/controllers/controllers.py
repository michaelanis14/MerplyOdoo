# -*- coding: utf-8 -*-
from odoo import http

# class ForTesting(http.Controller):
#     @http.route('/for_testing/for_testing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/for_testing/for_testing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('for_testing.listing', {
#             'root': '/for_testing/for_testing',
#             'objects': http.request.env['for_testing.for_testing'].search([]),
#         })

#     @http.route('/for_testing/for_testing/objects/<model("for_testing.for_testing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('for_testing.object', {
#             'object': obj
#         })