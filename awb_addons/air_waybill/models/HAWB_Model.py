from odoo.exceptions import ValidationError

from odoo import models,fields,api

class HAWB_Model(models.Model):
    _name = 'hawb.model'
    _rec_name = 'hawb_no'
    _description = 'HAWB Model'

# ========= IDs ========================================================================================================
    mawb_IDs = fields.Many2one("mawb.model")
    hawb_IDs = fields.Many2one("hawb.model")
    h_cargos_ID = fields.One2many('cargo.details', 'cargoH_IDs')


    hawb_no = fields.Char(size=12, string='HAWB Number')

#========= adressess information =======================================================================================
    h_shipper = fields.Many2one('res.partner', 'Shipper', requiered=True)
    h_consignee = fields.Many2one('res.partner', 'Consignee', requiered=True)

    h_agent_name = fields.Many2one(related='mawb_IDs.agent_name',
                       string='Agent Name', store=True, readonly=True)

    h_aiata_code = fields.Char(related='mawb_IDs.aiata_code',
                       string='AITA Code', store=True, readonly=True)

    h_account_no = fields.Char(related='mawb_IDs.account_no',
                       string='Account No', store=True, readonly=True)

    h_accounting_information = fields.Text(related='mawb_IDs.accounting_information',
                       string='Accounting Information', store=True, readonly=True)

#============ Routing and distnation =======================================================page1=======================
    h_airport_of_departure = fields.Char(related='mawb_IDs.airport_of_departure',
                       string='Airport of Departure', store=True, readonly=True)
    h_airport_of_destination = fields.Char(related='mawb_IDs.airport_of_destination',
                       string='Airport of Destination', store=True, readonly=True)

    h_flight_no = fields.Char(related='mawb_IDs.flight_no',
                              string='Flight No', store=True, readonly=True)
    h_flight_date = fields.Date(related='mawb_IDs.flight_date',
                                string='Flight Date', store=True, readonly=True)

    h_to = fields.Char(related='mawb_IDs.to',
                       string='TO', store=True, readonly=True)
    h_by_first_carrier = fields.Char(related='mawb_IDs.by_first_carrier',
                       string='By First Carrier', store=True, readonly=True)
    h_to_1 = fields.Char(related='mawb_IDs.to_1',
                       string='TO', store=True, readonly=True)
    h_by_1 = fields.Char(related='mawb_IDs.by_1',
                       string='BY', store=True, readonly=True)
    h_to_2 = fields.Char(related='mawb_IDs.to_2',
                       string='TO', store=True, readonly=True)
    h_by_2 = fields.Char(related='mawb_IDs.by_2',
                       string='BY', store=True, readonly=True)

#==============================Charge Information=======================================================================
    h_currency_ID = fields.Many2one(related='mawb_IDs.currency_ID',
                       string='Currency', store=True, readonly=True)

    h_declared_carriage = fields.Selection(related='mawb_IDs.declared_carriage',
                       string='Declared Carriage', store=True, readonly=True)
    h_carriage_value = fields.Float(related='mawb_IDs.carriage_value',
                       string='Declared Value', store=True, readonly=True,digits=(6, 2))
    h_declared_customs = fields.Selection(related='mawb_IDs.declared_customs',
                       string='Customs Carriage', store=True, readonly=True)
    h_customs_value = fields.Float(related='mawb_IDs.carriage_value',
                       string='Customs Value', store=True, readonly=True,digits=(6, 2))

    h_account_insurance = fields.Selection(related='mawb_IDs.account_insurance',
                       string='Amount of Insurance', store=True, readonly=True)
    h_insurance_value = fields.Text(related='mawb_IDs.insurance_value',
                       string='Other', store=True, readonly=True)

    h_wt = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')
    h_others = fields.Selection([('ppd', 'PPD'), ('coll', 'COLL')], default='ppd')
    h_charge_code = fields.Char('CHGS CODE')

# =========== Handling Information =====================================================================================
    h_handling_information = fields.Text(related='mawb_IDs.handling_information',
                       string='Handling Information', store=True, readonly=True)
    h_sci = fields.Char(related='mawb_IDs.sci',
                       string='SCI', store=True, readonly=True)

# ========= charges Sammary ============================================================================================
    h_currency_rate = fields.Float('Currency Convertion Rates',digits=(6, 2))
    h_cc_charges_in_dest_currency = fields.Float('Charges in Dest Currency',digits=(6, 2))
    h_charges_at_dest = fields.Float('Charges at Destination',digits=(6, 2))
    h_other_charges = fields.Text('Other Charges')
    h_total_collect_charges = fields.Float('Total Collect Charges',digits=(6, 2))

# ========= charges in Destination currency ============================================================================
    h_weight_charge = fields.Float(compute='_cal_weight_charge', string="Weight Charge", store=True,digits=(6, 2))
    h_valuation_charge = fields.Float('Valuation Charge',digits=(6, 2))
    h_tax = fields.Float('Tax',digits=(6, 2))
    h_Charges_due_agent = fields.Float('Total Other Charges Due Agent',digits=(6, 2))
    h_Charges_due_carrier = fields.Float('Total Other Charges Due Carrier',digits=(6, 2))
    h_total_charges = fields.Float(compute='_compute_total_charges',digits=(6, 2))

    # ========= calcs ============================================================================
    total_gross = fields.Float(compute='_compute_gross', string="gross", digits=(6, 2))
    total_chargable = fields.Float(compute='_compute_chargable', string="chargable", digits=(6, 2))

    h_weight = fields.Float(compute='_compare_weights', string="weight",digits=(6, 2))
    h_no_of_pieces = fields.Integer(compute='_compute_no_of_pieces', string="No of Pieces", digits=(6, 2))


# ========= Functions ==================================================================================================

    @api.one
    @api.depends('h_cargos_ID')
    def _cal_weight_charge(self):
        current_total = 0
        for item in self.h_cargos_ID:
            current_total = current_total + item.total

            self.h_weight_charge = current_total

        return True


    @api.one
    @api.depends('h_weight_charge', 'h_valuation_charge', 'h_tax', 'h_Charges_due_agent', 'h_Charges_due_carrier')
    def _compute_total_charges(self):
        self.h_total_charges = self.h_weight_charge + self.h_valuation_charge + self.h_tax + self.h_Charges_due_agent \
                             + self.h_Charges_due_carrier

        return True

    @api.one
    @api.depends('h_cargos_ID')
    def _compute_gross(self):
        current_GW = 0
        for item in self.h_cargos_ID:
            current_GW = current_GW + item.gross_weight

            self.total_gross = current_GW

    @api.one
    @api.depends('h_cargos_ID')
    def _compute_chargable(self):
        current_ch = 0
        for item in self.h_cargos_ID:
            current_ch = current_ch + item.Chargeable_Wight

            self.total_chargable = current_ch


    @api.one
    @api.depends('total_gross', 'total_chargable')
    def _compare_weights(self):

        if self.total_gross > self.total_chargable:
            self.h_weight = self.total_gross
        else:
            self.h_weight = self.total_chargable

    @api.one
    @api.depends('h_cargos_ID')
    def _compute_no_of_pieces(self):
        current_no = 0
        for item in self.h_cargos_ID:
            current_no = current_no + item.no_of_pieces

            self.h_no_of_pieces = current_no