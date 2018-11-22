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
    afb_price = fields.Float('Price')

    freight_charge= fields.Float(compute='_compute_freight_charge', string="Freight Charge", store=True)

    customer_curr = fields.Many2one(related='hawb_afb_ID.h_currency_ID', string='Customer Currency',
                                  store=True, readonly=True)

    customer_curr_total =fields.Monetary(string='Customer Services Total',store=True, readonly=True,
                                         currency_field='customer_curr', compute='_compute_customer_total')

    #currency_id = fields.Many2one('res.currency', string='Currency',
    #                              required=True, readonly=True,
     #                             compute='_select_currency_type', track_visibility='always')

    #invoice_selector= fields.Selection([('egp_invoice', 'EGP Invoice'),
     #                        ('foreign_invoice', 'Foreign Invoice')], default='egp_invoice', index=True, required=True)


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

    @api.one
    @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type','freight_charge')
    def _compute_amount(self):
        round_curr = self.currency_id.round
        self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)+ self.freight_charge
        self.amount_tax = sum(round_curr(line.amount_total) for line in self.tax_line_ids)
        self.amount_total = self.amount_untaxed + self.amount_tax
        amount_total_company_signed = self.amount_total
        amount_untaxed_signed = self.amount_untaxed
        if self.currency_id and self.company_id and self.currency_id != self.company_id.currency_id:
            currency_id = self.currency_id.with_context(date=self.date_invoice)
            amount_total_company_signed = currency_id.compute(self.amount_total, self.company_id.currency_id)
            amount_untaxed_signed = currency_id.compute(self.amount_untaxed, self.company_id.currency_id)
        sign = self.type in ['in_refund', 'out_refund'] and -1 or 1
        self.amount_total_company_signed = amount_total_company_signed * sign
        self.amount_total_signed = self.amount_total * sign
        self.amount_untaxed_signed = amount_untaxed_signed * sign





class Air_invoice_line(models.Model):
    _inherit =  "account.invoice.line"

    name = fields.Selection([('f_ch', 'FOB Charges (EX-Works)'),
                             ('fuel', 'FUEL'),
                             ('sec', 'SEC'),
                             ('fuel_sec', 'FUEL & SEC'),
                             ('courier', 'COURIR'),
                             ('eur', 'EUR 1'),
                             ('eur', 'EUR 1'),
                             ('x_ray', 'X-RAY'),
                             ('dgr', 'DGR'),
                             ('awb', 'AWB'),
                             ('customs', 'CUSTOMS'),
                             ('goods_cost', 'COST OF GOODS'),
                             ('pick', 'PICK UP'),
                             ('packing', 'PACKING'),
                             ('packaging', 'PACKAGING'),
                             ('sv_charges', 'S.V CHARGES'),
                             ('handling', 'HANDLING'),
                             ('special', 'SPECIAL TRUCK'),
                             ('inspection', 'INSPECTION'),
                             ('fumigation', 'FUMIGATION'),
                             ('leg_cost', 'COST OF LEGALIZATION'),
                             ('clearance', 'CLEARANCE'),
                             ('origin', 'CERTIFICATE OF ORIGIN'),
                             ('collection', 'COLLECTION'),
                             ], default='f_ch', index=True, required=True, translate=True,string=' Service ')






