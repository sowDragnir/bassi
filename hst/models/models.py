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

    def create(self, vals_list):
        if vals_list.get('is_pacient')== True:

            if vals_list.get('dni'):
                pacient_with_dni = self.env['res.partner'].search([('dni','=', vals_list['dni']), ('dni', '=', vals_list['dni'].upper())])
                if pacient_with_dni:
                    raise ValidationError('DNI already exists')
                else:
                    vals_list['dni'] = vals_list['dni'].upper()
            
            if vals_list.get('cip_code'):
                #cip_code = vals_list.get('cip_code').upper()
                pacient_with_cip_code = self.env['res.partner'].search([('cip_code', '=', vals_list['cip_code']),('cip_code', '=', vals_list['cip_code'].upper())])
                if pacient_with_cip_code:
                    raise ValidationError('CIP already exists')
                else:
                    vals_list['cip_code'] = vals_list['cip_code'].upper()
            
            vals_list['nhc_code'] = self.env['ir.sequence'].next_by_code('res.partner')
            vals_list['sequence_id'] = self.env['ir.sequence'].create({
                'padding': 3,
                'name': vals_list['nhc_code'],
                'prefix': 'EDP.'
            }).next_by_code()
            return super()
            
            # Mostrar los campos adicionales solo si 7777is_pacient es True
            if is_pacient:
                # Aquí puedes agregar el código para manejar los campos adicionales
                # Por ejemplo, puedes asignar valores a campos específicos en vals_list
                vals_list['campo1'] = 'ValorCampo1'
                vals_list['campo2'] = 'ValorCampo2'
            
            # Continúa con la creación del registro usando vals_list
            # ...

    # def create(self, vals_list):
    #     if vals_list.get('is_pacient') == True:

    #         if vals_list.get('dni'):
    #             paccient_with_dni = self.env['res.partner'].search([])