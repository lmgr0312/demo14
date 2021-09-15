# -*- coding: utf-8 -*-
# Copyright 2021 Morwi Encoders Consulting SA de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_path = fields.Char()
    purchase_order_analytic_count = fields.Integer(
        "Number of Purchase Order with same Analytic "
        "Account of the Sale Order",
        compute='_compute_purchase_order_analytic_count',)
    purchase_order_analytic_total = fields.Float(
        "Amount total of Purchase Order with same Analytic "
        "Account of the Sale Order",
        compute='_compute_purchase_order_analytic_count',)

    @api.depends('analytic_account_id')
    def _compute_purchase_order_analytic_count(self):
        for order in self:
            porders = self.env['purchase.order'].search([(
                'account_analytic_id', '=', order.analytic_account_id.id),
                ('account_analytic_id', '!=', False)])
            order.purchase_order_analytic_count = len(porders)
            po_total_amount = []
            for po in porders:
                po_amount = po.currency_id._convert(
                po.amount_total, po.company_id.currency_id, po.company_id,
                    fields.date.today(), round=False)
                po_total_amount.append(po_amount)   
            order.purchase_order_analytic_total = sum(po_total_amount)

    def action_view_purchase_orders_with_analytic(self):
        action = {
            'name': _('Purchase Order(s)'),
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'target': 'current',
            'domain': [('account_analytic_id', '=', self.analytic_account_id.id)],
        }
        orders = self.env['purchase.order'].search(
            [('account_analytic_id', '=', self.analytic_account_id.id)])
        if orders:
            action['view_mode'] = 'tree,form'
        else:
            action['view_mode'] = 'form'
        return action
