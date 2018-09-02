# -*- coding: utf-8 -*-

from odoo import models,fields,api

class project(models.Model):
    _name = 'project.main'
    _description = 'this model contains all the details of the bill'
    _rec_name = 'consignee'

# ========= adressess information ==================================================page2=============================================
    shipper = fields.Many2one('res.partner', 'Shipper')
    consignee = fields.Many2one('res.partner', 'Consignee')
    agent_name = fields.Many2one('res.partner', 'Agent Name')

    accounting_information =fields.Text('Accounting Information')
    AITA_code =fields.Char('AITA Code')
    account_no = fields.Char(string='Account No', relted='project.main.AITA_code', store=True)

    # ========================================Handling Information==============================================================================


    handling_information = fields.Text('Handling Information')
    _destination = fields.Char('Destination')
    sci = fields.Char('SCI')

    # ============ Routing and distnation =======================================================page1==============================================

    airport_of_departure = fields.Char('Airport of Departure')
    airport_of_destination = fields.Char('Airport of Destination')

    by_first_carrier = fields.Char('By First Carrier')
    flight_no = fields.Char('Flight No')
    flight_date = fields.Date('Flight Date')


    # ==============================Charge Information====================================================================================================

    currency_id = fields.Many2one('res.currency')
    charge_code = fields.Char('CHGS CODE')
    declared_carriage = fields.Char('Declared Value for Carriage')
    declared_customs = fields.Char('Declared Value for Customs')

    accouunt_insurance = fields.Char('Amount of Insurance')

    wt = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')
    others = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')

    # ========= charges Sammary ===============================================================================================
    currency_rate = fields.Float('Currency Convertion Rates')
    cc_charges_in_dest_currency = fields.Float('Charges in Dest. Currency')
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
    airportsO2M_connector = fields.One2many('airports','project_connector', 'Airports')
    cargosO2M_connector = fields.One2many('cargo.details','cargosM2O_connector', 'Rate Description Item')


# ========= Airports ==================================================page2=============================================
class airports(models.Model):
    _name = 'airports'
    _rec_name = 'to'

    project_connector = fields.Many2one('project.main', 'Airports')
    to = fields.Char('TO')
    by = fields.Char('BY')


#========= opertional shipping information ==================================================page2=============================================
class cargo_details(models.Model):
    _name = 'cargo.details'
    _description = 'this model contains Cargo Information'

    cargosM2O_connector = fields.Many2one('project.main')
    no_of_pieces = fields.Integer('No. of Pieces RCP')
    gross_weight = fields.Float('Gross Weight')
    class_rate = fields.Many2one('product.uom', 'Class Rate')

    commodity_item_no = fields.Integer('Commodity Item No')
    Chargeable_Wight = fields.Float('Chargeable Weight')
    rate_charge = fields.Float('Rate Charge')
    total = fields.Float('Total')

    quantity = fields.Text('Nature and Quantity of Goods')





