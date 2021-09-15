# -*- coding: utf-8 -*-
# Copyright 2021 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    account_analytic_id = fields.Many2one('account.analytic.account',
    	string='Analytic Account', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    @api.onchange('account_analytic_id')
    def set_account_analytic_to_lines(self):
        for rec in self:
            for line in rec.order_line:
                line.account_analytic_id = rec.account_analytic_id
