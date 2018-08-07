# -*- coding: utf-8 -*-

from odoo import models, fields

class master_Invoices(models.Model):
     _name = 'account.invoice'
     _inherit ='account.invoice'

     package = fields.Integer('Package')
     account = fields.Char('Account')

     Chipper = fields.Text()
     Consignee = fields.Selection(selection=[

      ('agent1', 'Agent 1'),

      ('agent2', 'Agent 2'), ],
          string='Consignee')
     Intermediate_consignee = fields.Selection(selection=[

      ('agent1', 'Agent 1'),

      ('agent2', 'Agent 2'), ],
          string='Intermediate Consignee')

     Exporting_carrier = fields.Char("Exporting Carrier")
     Exporting_date = fields.Date("Exporting Date")



#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100