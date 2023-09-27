from odoo import models, fields, api
from odoo.exceptions import ValidationError


class hst(models.Model):
    _inherit = 'res.partner'


    nhc_code = fields.Char(string='NHC', copy=False, default='new', readonly=True)
    dni = fields.Char(string='DNI')
    nass_code = fields.Char(string='NASS')
    cip_code = fields.Char(string='CIP')
    is_pacient = fields.Boolean(default=False)
    birthday = fields.Date(string='Birthday')
    other_obs = fields.Char(string='another Observation')

    @api.model
    def create(self, vals_list):
        if vals_list.get('is_pacient')== True:

            if vals_list.get('dni'):
                pacient_with_dni = self.env['res.partner'].search([('dni','=', vals_list['dni']), ('dni', '=', vals_list['dni'].upper())])
                if pacient_with_dni:
                    raise ValidationError('DNI ya existe')
                else:
                    vals_list['dni'] = vals_list['dni'].upper()

            if vals_list.get('nhc_code', 'new') =='new':
                    vals_list['nhc_code'] = self.env['ir.sequence'].next_by_code('res.partner') or ('New')
                    result = super(hst , self).create(vals_list)
                    return result

            
            
   