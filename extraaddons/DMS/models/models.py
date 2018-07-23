# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class DMS(models.Model):
#     _name = 'DMS.DMS'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

from odoo import models, fields, api
class MyModel(models.Model):
    _inherit = 'sale.order'

    vehicale_id = fields.Char('vehicale number')
