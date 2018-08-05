# -*- coding: utf-8 -*-

from odoo import models, fields, api

class awbinvoices(models.Model):
     _name = 'awbinvoices.awbinvoices'

     InvoceName = fields.Char()
     Chipper= fields.Text()
     Consignee = fields.Text()
     Intermideate_consignee = fields.Text()
     forwarding_agent  = fields.Text()
     commercial_invoice_no = fields.Integer()
     exporting_carrier = fields.Text()
     date = fields.Date()
     customer_no = fields.Integer()
     awb_no = fields.Integer()
     origin_contry = fields.Char()
     export_date = fields.Date()
     payment_terms = fields.Text()
     export_reference = fields.Char()
     currency = fields.Char()
     packages = fields.Integer()
     discription = fields.Text()
     net_weight = fields.Float()
     gross_weight = fields.Float()
     quentity = fields.Float()
     total_value = fields.Float()
     unit_price = fields.Float()
     charges = fields.Text()
     package_marks = fields.Integer()




#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100