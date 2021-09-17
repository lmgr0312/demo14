# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models
from odoo.tools import hmac


class SocialMedia(models.Model):
    _inherit = 'social.media'
    
    csrf_token = fields.Char('CSRF Token', compute='_compute_csrf_token',
        help="This token can be used to verify that an incoming request from a social provider has not been forged.")

    def _compute_csrf_token(self):
        for media in self:
            media.csrf_token = hmac(self.env(su=True), 'social_social-account-csrf-token', media.id)
