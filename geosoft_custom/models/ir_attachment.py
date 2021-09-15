# -*- coding: utf-8 -*-
# Copyright 2021 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.model
    def create(self, vals):
        attach = self.search([
            ('res_id', '=', vals['res_id']),
            ('res_model', '=', vals['res_model']),
            ('name', '=', vals['name'])])
        mail_attach = self.search([
            ('name', '=', vals['name'])])
        if attach:
            vals['res_id'] = False
            vals['res_model'] = False
        if mail_attach and vals['res_model'] == 'mail.compose.message':
            vals['res_model'] = False
        res = super().create(vals)
        return res
