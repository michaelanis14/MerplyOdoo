import uuid

from odoo import models,fields,api
class Air_freight_bill(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'
    _description = 'Air Freight Bill'

# ========= IDs ========================================================================================================
    mawb_afb_ID = fields.Many2one("mawb.model")
    hawb_afb_ID = fields.Many2one("hawb.model")

    services_ID = fields.One2many('services.model', 'invoice_id')


    afb_no_of_pieces = fields.Integer(related='hawb_afb_ID.h_no_of_pieces',
                                      string='No Of Pieces', store=True, readonly=True)
    afb_gross_weight = fields.Float(related='hawb_afb_ID.total_gross',
                                      string='Gross Weight', store=True, readonly=True)
    afb_Chargeable_Wight = fields.Float(related='hawb_afb_ID.total_chargable',
                                      string='Chargeable Weight', store=True, readonly=True)

    shipping_port = fields.Char('shipping port')
    arrival_port = fields.Char('Arrival port')

    freight_charge = fields.Float(compute='_compute_frieght_charge', string="Frieght Charge",digits=(6, 2))

    account_to = fields.Char('Account To')


    afb_weight = fields.Float(related='hawb_afb_ID.h_weight',
                       string='Weight', store=True, readonly=True)
    afb_price = fields.Float('Price', digits=(6, 2))
    mawb_a = fields.Many2one(related='hawb_afb_ID.mawb_IDs',
                             string='MAWB NO', store=True, readonly=True)
    # ========= modifying existing fields ==============================================================================
    partner_id = fields.Many2one(related='hawb_afb_ID.h_shipper')




#========= Functions ==================================================page2============================================
    @api.one
    @api.depends('afb_weight','price')
    def _compute_frieght_charge(self):

        return self.afb_weight * self.afb_price



    @api.one
    @api.depends('services_ID.price_subtotal', 'tax_line_ids.amount', 'tax_line_ids.amount_rounding',
                 'currency_id', 'company_id', 'date_invoice', 'type')
    def _compute_amount(self):
        round_curr = self.currency_id.round
        self.amount_untaxed = sum(line.price_subtotal for line in self.services_ID)
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

