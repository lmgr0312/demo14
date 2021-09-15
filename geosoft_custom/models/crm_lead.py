# -*- coding: utf-8 -*-
# Copyright 2021 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
import pytz

from datetime import datetime
from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
        default=lambda self: self.env.company.currency_id.id)
    currency_rate = fields.Float(string='Conversion Rate', compute='_compute_currency_rate', help='Conversion rate of current day')
    won_date = fields.Date(store=True,)
    
    def action_new_quotation(self):
        action = super().action_new_quotation()
        action['context']['default_client_order_ref'] = self.name
        action['context']['default_currency_id'] = self.currency_id.id
        return action

    @api.depends('company_id', 'currency_id')
    def _compute_currency_rate(self):
        MailTrackingValue = self.env['mail.tracking.value'].sudo()
        stage_id = self.env.ref('crm.field_crm_lead__stage_id')
        won_stage = self.env['crm.stage'].search([('is_won', '=', True)])
        for opportunity in self:
            tracking_value = MailTrackingValue.search([
                ('mail_message_id', 'in', opportunity.message_ids.ids),
                ('field', '=', stage_id.id),
                ('new_value_integer', '=', won_stage.id)], limit=1)
            if tracking_value:
                date = tracking_value.mail_message_id.date.astimezone(
                    pytz.timezone('America/Mexico_City')).strftime(
                    '%Y-%m-%d')
                value = date
                opportunity.won_date = fields.Date.from_string(date)
            else:
                value = fields.date.today()
                opportunity.won_date = False
            opportunity.currency_rate = opportunity.currency_id._convert(
                1.0, opportunity.company_id.currency_id, opportunity.company_id,
                    value, round=False)                               
