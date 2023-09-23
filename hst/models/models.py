from odoo import models, fields, api
#from odoo import ValidationError


class hst(models.Model):
    _inherit = 'res.partner'


    nhc_code = fields.Char(string='NHC', copy=False, default='new', readonly=True)
    dni = fields.Char(string='DNI')
    nass_code = fields.Char(string='NASS')
    cip_code = fields.Char(string='CIP')
    is_pacient = fields.Boolean(default=False)
    birthday = fields.Date(string='Birthday')
    other_obs = fields.Char(string='another Observation')
    #csb = fields.Char(string='gcdg')

    @api.model
    def create(self, vals_list):
        if vals_list.get('is_pacient')== True:

            if vals_list.get('dni'):
                pacient_with_dni = self.env['res.partner'].search([('dni','=', vals_list['dni']), ('dni', '=', vals_list['dni'].upper())])
                if pacient_with_dni:
                    raise ValidationError('DNI already exists')
                else:
                    vals_list['dni'] = vals_list['dni'].upper()
            
            # if vals_list.get('cip_code'):
            #     #cip_code = vals_list.get('cip_code').upper()
            #     pacient_with_cip_code = self.env['res.partner'].search([('cip_code', '=', vals_list['cip_code']),('cip_code', '=', vals_list['cip_code'].upper())])
            #     if pacient_with_cip_code:
            #         raise ValidationError('CIP already exists')
            #     else:
            #         vals_list['cip_code'] = vals_list['cip_code'].upper()
    @api.model_create_multi
    def create(self, vals_list):
        if vals_list.get('nhc_code', 'New') == 'New':
            vals_list['ref'] = self.env['ir.sequence'].next_by_code('res.P')
            vals_list['sequence_id'] = self.env['ir.sequence'].create().next_by_code()

            return super('nhc_code', self).create(vals_list)
            

            # vals_list['nhc_code'] = self.env['ir.sequence'].next_by_code('res.partner')
            # vals_list['sequence_id'] = self.env['ir.sequence'].create({
            #     'padding': 3,
            #     'name': vals_list['nhc_code'],
            #     'prefix': 'EDP.'
            # }).next_by_code('res.partner')
            # return super( self).create(vals_list)
            