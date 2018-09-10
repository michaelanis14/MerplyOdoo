# -*- coding: utf-8 -*-

from odoo import models,fields,api

class MAWB_Model(models.Model):
    _name = 'mawb.model'
    _rec_name = 'mawb_no'
    _description = 'MAWB Model'

    mawb_no = fields.Char(string='MAWB Number')

# ========= adressess information ===============================================================================================
    shipper = fields.Many2one('res.partner', 'Shipper', requiered=True)
    consignee = fields.Many2one('res.partner', 'Consignee', requiered=True)
    agent_name = fields.Many2one('res.partner', 'Agent Name', requiered=True)

    accounting_information = fields.Text('Accounting Information')
    AITA_code = fields.Char('AITA Code', requiered=True)
    account_no = fields.Char(string='Account No', relted='project.main.AITA_code', store=True)


# ============ Routing and distnation =======================================================page1==============================================

    airport_of_departure = fields.Char('Airport of Departure', requiered=True)
    airport_of_destination = fields.Char('Airport of Destination', requiered=True)

    to = fields.Char('TO')
    by_first_carrier = fields.Char('By First Carrier')
    to_1 = fields.Char('TO')
    by_1 = fields.Char('BY')
    to_2 = fields.Char('TO')
    by_2 = fields.Char('BY')
    flight_no = fields.Char('Flight No', requiered=True)
    flight_date = fields.Date('Flight Date', requiered=True)

#==============================Charge Information====================================================================================================

    currency_ID = fields.Many2one('res.currency')
    charge_code = fields.Char('CHGS CODE')
    declared_carriage = fields.Selection([('nvd', 'NVD'),('value', 'Value')],default='nvd')
    carriage_value = fields.Float('Carriage Value')
    declared_customs = fields.Selection([('ncv', 'NCV'),('value', 'Value')],default='ncv')
    customs_value = fields.Float('Customs Value')

    account_insurance = fields.Char('Amount of Insurance')

    wt = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')
    others = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')

#========================================Handling Information==============================================================================
    handling_information = fields.Text('Handling Information')
    _destination = fields.Char('Destination')
    sci = fields.Char('SCI')

#========= charges Sammary ===============================================================================================
    currency_rate = fields.Float('Currency Convertion Rates')
    cc_charges_in_dest_currency = fields.Float('Charges in Dest Currency')
    charges_at_dest = fields.Float('Charges at Destination')
    other_charges = fields.Text('Other Charges')
    total_collect_charges = fields.Float('Total Collect Charges')

#========= charges in Destination currency ===============================================================================================

    weight_charge = fields.Float(compute='_cal_total', string="Weight Charge", store= True)
    valuation_charge = fields.Float('Valuation Charge')
    tax = fields.Float('Tax')
    Charges_due_agent = fields.Float('Total Other Charges Due Agent')
    Charges_due_carrier = fields.Float('Total Other Charges Due Carrier')
    total_charges = fields.Float(compute='_compute_total_charges')

#========= IDs ==================================================page2=============================================

    cargos_ID = fields.One2many('cargo.details','cargo_IDs', 'Rate Description Item')
    mawb_ID = fields.Many2one('mawb.model')
    #hawb_ID = fields.One2many(comodel_name='hawb.model', relation='mawb_IDs')


#========= Functions ==================================================page2=============================================

    @api.one
    @api.depends('cargos_ID')
    def _cal_total(self):
        current_total = 0
        for item in self.cargos_ID:
            current_total = current_total + item.total

            self.weight_charge = current_total


    @api.one
    @api.depends('weight_charge', 'valuation_charge', 'tax', 'Charges_due_agent', 'Charges_due_carrier')
    def _compute_total_charges(self):
        self.total_charges = self.weight_charge + self.valuation_charge + self.tax + self.Charges_due_agent + self.Charges_due_carrier

        return True

