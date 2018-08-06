# -*- coding: utf-8 -*-

from odoo import models, fields

class invoices(models.Model):
     _name = 'account_invoicing'


     Chipper = fields.Text()
     Consignee = fields.Text()
     Intermideate_consignee = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100