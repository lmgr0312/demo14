# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models


class SocialAccount(models.Model):
    _inherit = 'social.account'
    
    def _filter_by_media_types(self, media_types):
        return self.filtered(lambda account: account.media_type in media_types)
