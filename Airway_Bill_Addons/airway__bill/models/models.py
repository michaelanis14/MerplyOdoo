# -*- coding: utf-8 -*-
from odoo import models, fields, api

class airway__bill(models.Model):
    _name = 'airway__bill.airway__bill'

    #consignee info
    consignee_name = fields.Many2one('res.partner', 'Consignee')
    intermediate_consignee = fields.Many2one('consignee_name', 'Intermediate Consignee')

    #CHIPPER INFO
    chipper_name = fields.Many2one('res.partner', 'Chipper')

    #CHARGES INFO
    freight_charges = fields.Float('Freight Charges')
    discharge_expenses = fields.Float('Discharge Expenses')
    exw = fields.Float('ExWorks Charges')
    fob = fields.Float('FOB Charges')

     #INVOICE INFO
    mawb = fields.Char('MAWB')
    hawb = fields.Char('HAWB')
    invoice_no = fields.Char('Invoice Number')
    invoice_date = fields.Date('Invoice Date')

    # cargo info
    package_no = fields.Integer('Number Of Package')
    delevary_order = fields.Many2one('product.template', 'Delevared Product')
    description = fields.Text('Description')
    account = fields.Text('Account')
    quantity = fields.Float('Quantity')
    currency = fields.Char('Currency')
    vat = fields.Float('VAT')
    net_weight = fields.Float('Net Weight')
    gross_weight = fields.Float('Gross Weight')
    amount = fields.Float('Amount')


#


#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100