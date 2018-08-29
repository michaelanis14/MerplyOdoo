# -*- coding: utf-8 -*-
from odoo import http

# class ProjectTemplate(http.Controller):
#     @http.route('/project_template/project_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_template/project_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_template.listing', {
#             'root': '/project_template/project_template',
#             'objects': http.request.env['project_template.project_template'].search([]),
#         })

#     @http.route('/project_template/project_template/objects/<model("project_template.project_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_template.object', {
#             'object': obj
#         })