# -*- coding: utf-8 -*-

from odoo import models, fields

class master_Invoices(models.Model):

     _inherit ='account.invoice.line'

     #package = fields.Integer('Package')
     #account = fields.Char('Account')






#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100