# -*- coding: utf-8 -*-
from odoo import models, fields, api

class airway__bill(models.Model):
    _name = 'airway__bill.airway__bill'

    #consignee info
    consignee_name = fields.Selection(selection=[

         ('agent1', 'Agent 1'),

         ('agent2', 'Agent 2'), ],
         string='Consignee')

    #CHIPPER INFO
    chipper_name = fields.Selection(selection=[

         ('agent1', 'Agent 1'),

         ('agent2', 'Agent 2'), ],
         string='Chipper')



    #CHARGES INFO
    freight_charges = fields.Float('Freight Charges')
    discharge_expenses = fields.Float('Discharge Expenses')
    exw = fields.Float('ExWorks Charges')
    fob = fields.Float('FOB Charges')

    #cargo info
    delevary_order = fields.Char('Delevary Order')
    currency = fields.Char('Currency')
    package_no = fields.Integer('Package')
    net_weight = fields.Float('Net Weight')
    gross_weight = fields.Float('Gross Weight')

    #INVOICE INFO
    mawb = fields.Char('MAWB')
    hawb = fields.Char('HAWB')
    invoice_no = fields.Char('Invoice Number')
    invoice_date = fields.Date('Invoice Date')

#


#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100