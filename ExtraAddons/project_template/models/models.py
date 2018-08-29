# -*- coding: utf-8 -*-

from odoo import models,fields,api

class project(models.Model):
    _name = 'project.main'
    _description = 'this model contains all the details of the bill'

    consignee = fields.Many2one('consignee.info', 'Consignee')
    mawb = fields.Char('MAWB NO')
    hawb = fields.Char('HAWB NO')
    date = fields.Date('Invoice Date')

    destination_airport = fields.Char('Airport of Destination')
    departure_airport = fields.Char('Airport of Departure')

    cargo_connector = fields.One2many('cargo.info','cargo_project_connector', 'Cargo')
    charges_connector = fields.One2many('charges.info','charges_project_connector', 'Charges')

    totalCharges = fields.Float(string='Total', store=True, compute='_calCharges')

    @api.one
    @api.depends('charges_connector')
    def _calCharges(self):
        currentcharges = 0
        for charge in self.charges_connector:
            currentcharges = currentcharges + (charge.charge_value)

            self.totalCharges = currentcharges


class consignee_info(models.Model):
    _name = 'consignee.info'
    _inherit = 'res.partner'
    _description = 'contains Consignee Information'

    consignee_name = fields.Char('Consignee Name')
    mypartner = fields.Many2one('res.partner')
    consignee_street1 = fields.Char(related = 'mypartner.street', string='Address', store=True)
    consignee_street2 = fields.Char(related='mypartner.street2', string='Street 2', store=True)
    consignee_city = fields.Char(related='mypartner.city', string='City', store=True)
    consignee_state = fields.Many2one(related='mypartner.state_id', string='State', store=True)
    consignee_country = fields.Many2one(related='mypartner.country_id', string='Country', store=True)


    consignee_tel = fields.Char(related='mypartner.phone', string='Phone', store=True)
    consignee_fax = fields.Char('Fax')
    consignee_email = fields.Char(related='mypartner.email', string='Email', store=True)
    consignee_salesperson = fields.Many2one(related='mypartner.user_id', string='Sales Person', store=True)


class cargo_info(models.Model):
    _name = 'cargo.info'
    _description = 'this model contains the cargo iformation'

    cargo_project_connector =fields.Many2one('project.main')
    delivery_order = fields.Char('Delivery Order')
    no_of_packages = fields.Integer('No Of Packages')
    gross_weight = fields.Float('Gross Weight')
    net_weight = fields.Float('Net Weight')


class charges_info(models.Model):
    _name = 'charges.info'
    _description = 'this model contains the cargo iformation'

    charges_project_connector =fields.Many2one('project.main')
    charge_name = fields.Char('Charge Name')
    charge_value = fields.Float('Charge Value')
    totalCharges = fields.Float(string='Total', store= True, compute = '_calCharges')



