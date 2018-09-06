# -*- coding: utf-8 -*-

from odoo import models,fields,api

class project(models.Model):
    _name = 'project.main'
    _description = 'MAWB Model'
    _rec_name = 'consignee'

    connector = fields.Many2one('project.main')
    invoice_no = fields.Char(string='Invoice Number')
# ========= adressess information ==================================================page2=============================================
    shipper = fields.Many2one('res.partner', 'Shipper', requiered=True)
    consignee = fields.Many2one('res.partner', 'Consignee', requiered=True)
    agent_name = fields.Many2one('res.partner', 'Agent Name', requiered=True)

    accounting_information =fields.Text('Accounting Information')
    AITA_code =fields.Char('AITA Code', requiered=True)
    account_no = fields.Char(string='Account No', relted='project.main.AITA_code', store=True)

    # ============ Routing and distnation =======================================================page1==============================================

    airport_of_departure = fields.Char('Airport of Departure', requiered=True)
    airport_of_destination = fields.Char('Airport of Destination', requiered=True)

    by_first_carrier = fields.Char('By First Carrier')
    to = fields.Char('TO')
    by = fields.Char('BY')
    flight_no = fields.Char('Flight No', requiered=True)
    flight_date = fields.Date('Flight Date', requiered=True)


    # ==============================Charge Information====================================================================================================

    currency_id = fields.Many2one('res.currency')
    charge_code = fields.Char('CHGS CODE')
    declared_carriage = fields.Selection([('nvd', 'NVD'),('value', 'Value')],default='nvd')
    carriage_value = fields.Float('Carriage Value')
    declared_customs = fields.Selection([('ncv', 'NCV'),('value', 'Value')],default='ncv')
    customs_value = fields.Float('Customs Value')

    account_insurance = fields.Char('Amount of Insurance')

    wt = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')
    others = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')

    # ========================================Handling Information==============================================================================
    handling_information = fields.Text('Handling Information')
    _destination = fields.Char('Destination')
    sci = fields.Char('SCI')

    # ========= charges Sammary ===============================================================================================
    currency_rate = fields.Float('Currency Convertion Rates')
    cc_charges_in_dest_currency = fields.Float('Charges in Dest Currency')
    charges_at_dest = fields.Float('Charges at Destination')
    other_charges = fields.Text('Other Charges')
    total_collect_charges = fields.Float('Total Collect Charges')

    # ========= charges in Destination currency ===============================================================================================
    weight_charge = fields.Float('Weight Charge')
    valuation_charge = fields.Float('Valuation Charge')
    tax = fields.Float('Tax')
    Charges_due_agent = fields.Float('Total Other Charges Due Agent')
    Charges_due_carrier = fields.Float('Total Other Charges Due Carrier')

    # ========= connectors ==================================================page2=============================================
    #airportsO2M_connector = fields.One2many('airports','project_connector', 'Airports')
    cargosO2M_connector = fields.One2many('cargo.details','cargosM2O_connector', 'Rate Description Item')

    # ========= Functions ==================================================page2=============================================



#========= opertional shipping information ==================================================page2=============================================
class cargo_details(models.Model):
    _name = 'cargo.details'
    _rec_name = 'no_of_pieces'
    _description = 'this model contains Cargo Information'

    cargosM2O_connector = fields.Many2one('project.main')
    no_of_pieces = fields.Integer('No. of Pieces')
    gross_weight = fields.Float('Gross Weight')
    class_rate = fields.Selection([('kg', 'Kg'),('q', 'Q')],default='kg')

    commodity_item_no = fields.Integer('Commodity Item No')
    description = fields.Text('Goods Description')

    l = fields.Integer('Length')
    w = fields.Integer('width')
    h = fields.Integer('Hight')

    shippment_vol = fields.Float(compute='_compute_vol', string="VOL")
    Chargeable_Wight = fields.Float(compute='_compute_chargableW', string="Chargable Weight")
    rate_charge = fields.Float('Rate Charge')
    total = fields.Float(compute='_compute_total', string="Total")
    #quantity = fields.One('nature.goods',string='Nature and Quantity of Goods')

    # ========= Functions ==================================================page2=============================================

    @api.depends('l', 'w', 'h', 'no_of_pieces')
    def _compute_vol(self):
        for ship in self:
            ship.shippment_vol = self.l * self.h * self.w * self.no_of_pieces

        return True

    @api.depends('shippment_vol')
    def _compute_chargableW(self):
        for shipChW in self:
            shipChW.Chargeable_Wight = self.shippment_vol * 167

        return True

    @api.depends('Chargeable_Wight', 'rate_charge')
    def _compute_total(self):
        for shipment in self:
            shipment.total = self.Chargeable_Wight * self.rate_charge

        return True










