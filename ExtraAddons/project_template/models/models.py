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

    # ==============================Cargo Information====================================================================================================

    no_of_pieces = fields.Integer('No. of Pieces RCP')
    gross_weight = fields.Float('Gross Weight')
    commodity_item_no = fields.Integer('Commodity Item No')
    Chargeable_Wight = fields.Float('Chargeable Weight')
    rate_charge = fields.Float('Rate Charge')
    total = fields.Float('Total')

    tax = fields.Float('Tax')

    quantity = fields.Text('Nature and Quantity of Goods')

    # ========= connectors ==================================================page2=============================================
    routingO2M_connector = fields.One2many('routing.details','raoutingM2O_connector', 'Routing and distnation')
    chargesO2M_connector = fields.One2many('charges.details','chargesM2O_connector', 'Charges Decleration')


#============ Routing and distnation =======================================================page1==============================================
class routing_details(models.Model):
    _name = 'routing.details'
    _description = 'this model contains Routing and distnation Information'
    _rec_name = 'flight_no'

    raoutingM2O_connector = fields.Many2one('project.main')
    airport_of_departure = fields.Char('Airport of Departure')
    airport_of_destination = fields.Char('Airport of Destination')
    to = fields.Char('TO')
    by = fields.Char('BY')
    flight_no = fields.Char('Flight No')
    flight_date = fields.Date('Flight Date')

#========= opertional shipping information ==================================================page2=============================================
class charges_details(models.Model):
    _name = 'charges.details'
    _description = 'this model contains Charges Information'

    chargesM2O_connector = fields.Many2one('project.main')
    currency = fields.Many2many('res.currency', 'Currency')

    charge_code = fields.Char('CHGS CODE')
    ppd = fields.Boolean("PPD")
    coll = fields.Boolean('COLL')

    declared_carriage = fields.Char('Declared Value for Carriage')
    declared_customs = fields.Char('Declared Value for Customs')

    accouunt_insurance = fields.Char('Amount of Insurance')





