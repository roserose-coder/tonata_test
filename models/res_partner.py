from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'


    @api.model
    def create(self, vals):
        if 'name' in vals:
            res_partner = self.env['res.partner'].search([('name', '=', vals["name"])])
            if res_partner :
                raise ValidationError(_('Nama terkait sudah ada'))

        res = super(ResPartnerInherit, self).create(vals)
        if not res.mobile:
            raise ValidationError(_('Nomor Ponsel wajib diisi'))
        return res


