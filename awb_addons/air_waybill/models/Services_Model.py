# -*- coding: utf-8 -*-
import dp as dp

from odoo import models,fields,api
class Cargo_Model(models.Model):
    _name = 'services.model'
    _inherit = "account.invoice.line"
    _rec_name = 'service_name'
    _description = 'Services Information'



    #afb_sevices_IDs = fields.Many2one('account.invoice')
    sevice_ID = fields.Many2one('services.model')

    service_name = fields.Selection([('f_ch', 'FOB Charges (EX-Works)'),
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
                                     ],default='f_ch')
    sale = fields.Float('Sale')
    main = fields.Boolean('Main')
    cost = fields.Monetary('Cost')
    description = fields.Text('Description')
    vendor =fields.Char('Vendor')
    lump_sum = fields.Boolean('Lumb Sum')

    # overriding compute_price

    @api.one
    @api.depends('cost', 'discount', 'invoice_line_tax_ids',
                 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
                 'invoice_id.date_invoice', 'invoice_id.date')
    def _compute_price(self):
        currency = self.invoice_id and self.invoice_id.currency_id or None
        price = self.cost * (1 - (self.discount or 0.0) / 100.0)
        taxes = False
        if self.invoice_line_tax_ids:
            taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id,
                                                          partner=self.invoice_id.partner_id)       #problem here
        self.price_subtotal = price_subtotal_signed = taxes['total_excluded'] if taxes else self.cost
        self.price_total = taxes['total_included'] if taxes else self.price_subtotal
        if self.invoice_id.currency_id and self.invoice_id.currency_id != self.invoice_id.company_id.currency_id:
            price_subtotal_signed = self.invoice_id.currency_id.with_context(
                date=self.invoice_id._get_currency_rate_date()).compute(price_subtotal_signed,
                                                                        self.invoice_id.company_id.currency_id)
        sign = self.invoice_id.type in ['in_refund', 'out_refund'] and -1 or 1
        self.price_subtotal_signed = price_subtotal_signed * sign
