# -*- coding: utf-8 -*-

from odoo import models,fields,api
class Cargo_Model(models.Model):
    _name = 'cargo.details'
    _rec_name = 'no_of_pieces'
    _description = 'Cargo Information'


    cargoM_IDs = fields.Many2one('mawb.model')
    cargoH_IDs = fields.Many2one('hawb.model')

    no_of_pieces = fields.Integer('No. of Pieces')
    gross_weight = fields.Float('Gross Weight',digits=(6, 2))
    class_rate = fields.Selection([('kg', 'Kg'),('q', 'Q')],default='kg')
    commodity_item_no = fields.Integer('Commodity Item No')
    Chargeable_Wight = fields.Float(compute='_compute_chargableW', string="Chargeable Weight",digits=(6, 2))
    rate_charge = fields.Float('Rate Charge',digits=(6, 2))
    total = fields.Float(compute='_compute_total', string="Total",digits=(6, 2))

    description = fields.Text('Goods Description')

    l = fields.Integer('Length')
    w = fields.Integer('width')
    h = fields.Integer('Hight')

    shipment_vol = fields.Float(compute='_compute_vol', string="VOL",digits=(6, 2))


    # ========= Functions ==================================================page2=============================================
    @api.one
    @api.depends('l', 'w', 'h', 'no_of_pieces')
    def _compute_vol(self):
        for ship in self:
            ship.shipment_vol = self.l * self.h * self.w * self.no_of_pieces

        return True

    @api.one
    @api.depends('shipment_vol')
    def _compute_chargableW(self):
        for shipChW in self:
            shipChW.Chargeable_Wight = self.shipment_vol * 167

        return True

    @api.one
    @api.depends('Chargeable_Wight', 'rate_charge')
    def _compute_total(self):
        for shipment in self:
            shipment.total = self.Chargeable_Wight * self.rate_charge

        return True




