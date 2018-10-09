import uuid

import dp

from odoo import models,fields,api
class Air_freight_bill(models.Model):
    #_name = 'account.invoice'
    _inherit = 'account.invoice'
    _description = 'Air Freight Bill'

# ========= IDs ========================================================================================================
    hawb_afb_ID = fields.Many2one("hawb.model",string='HAWB NO')

    customer_services_id= fields.One2many("services.info","afb_id")

    mawb_a = fields.Many2one(related='hawb_afb_ID.mawb_IDs',
                             string='MAWB NO', store=True, readonly=True)

    partner_id = fields.Many2one(related='hawb_afb_ID.h_consignee',string='Partner', store=True, change_default=True,
                                 required=True, readonly=True, states={'draft': [('readonly', False)]},
                                 track_visibility='always')

    afb_no_of_pieces = fields.Integer(related='hawb_afb_ID.h_no_of_pieces',
                                      string='No Of Pieces', store=True, readonly=True)
    afb_gross_weight = fields.Float(related='hawb_afb_ID.total_gross',
                                      string='Gross Weight', store=True, readonly=True)
    afb_Chargeable_Wight = fields.Float(related='hawb_afb_ID.total_chargable',
                                      string='Chargeable Weight', store=True, readonly=True)



    afb_weight = fields.Float(related='hawb_afb_ID.h_weight',
                       string='Weight', store=True, readonly=True)
    afb_price = fields.Float('Price', digits=(6, 2))

    freight_charge= fields.Float(compute='_compute_freight_charge', string="Freight Charge", store=True, digits=(6, 2))

    customer_curr = fields.Many2one(related='hawb_afb_ID.h_currency_ID', string='Customer Currency',
                                  store=True, readonly=True)

    customer_curr_total =fields.Monetary(string='Total',store=True, readonly=True,
                                         currency_field='customer_curr', compute='_compute_customer_total')





#========= Functions ==================================================page2============================================
    @api.one
    @api.depends('afb_weight','afb_price')
    def _compute_freight_charge(self):

        self.freight_charge=self.afb_weight * self.afb_price



    @api.one
    @api.depends('customer_services_id','customer_curr','freight_charge')
    def _compute_customer_total(self):
        round_curr = self.customer_curr.round
        serv_costs = 0
        for cust_serv in self.customer_services_id:
            serv_costs = serv_costs + round_curr(cust_serv.custom_service_cost) + self.freight_charge

            self.customer_curr_total = serv_costs











