# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, fields, models


class SocialPost(models.Model):
    _name = 'social.post'
    _inherit = ['social.post', 'social.post.template']
