# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models


class SocialStreamPost(models.Model):
    _inherit = 'social.stream.post'

    def _filter_by_media_types(self, media_types):
        return self.filtered(lambda post: post.media_type in media_types)
