# -*- coding: utf-8 -*-

from odoo import models, fields, api

class filling_master_info(models.Model):
    _name = 'f '

    consignee = fields.Many2one('consignee_info.consignee_info','Consignee')

    mawb = fields.Char('MAWB NO')
    hawb = fields.Char('HAWB NO')

    no_of_packages = fields.Integer('No Of Packages')
    gross_weight = fields.Float('Gross Weight')
    net_weight = fields.Float('Net Weight')

    date = fields.Date('Invoice Date')
    delivery_order = fields.Char('Delivery Order')

    destination_airport = fields.Char('Airport of Destination')
    departure_airport = fields.Char('Airport of Departure')

    charge_id = fields.Many2one('charges_model.charges_model', 'Charges')

    amount = fields.Float(string='Amount', store='true', compute='_compute_Amount')

    def _compute_Amount(self):
        current_ammount=0

        for x in self.charge_id:
            current_ammount= current_ammount + x.charge_id.charge_value











