from odoo import models, fields, api


class hst(models.Model):
    _inherit = 'res.partner'


    nhc_code = fields.Char(string='NHC', readonly=True)
    dni = fields.Char(string='DNI')
    nass_code = fields.Char(string='NASS')
    cip_code = fields.Char(string='CIP')
    is_pacient = fields.Boolean(default=False)
    birthday = fields.Date(string='Birthday')
    other_obs = fields.Char(string='another Observation')