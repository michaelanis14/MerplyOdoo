# -*- coding: utf-8 -*-

from odoo import models, fields, api

class course(models.Model):
     _name = 'open_academy.course'

     name = fields.Char(string='Title', requierd='true')
     description = fields.Text(string='Course Decription')
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100