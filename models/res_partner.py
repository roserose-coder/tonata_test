from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        res = super(ResPartnerInherit, self).create(vals)
        if not res.mobile:
            raise ValidationError(_('Ponsel wajib diisi'))
        return res
