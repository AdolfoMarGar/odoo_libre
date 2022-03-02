
from odoo import models, fields, api


class aparcami(models.Model):
    _name = 'odoo_libre.aparcami'
    _description = 'Define las caracteristicas de un aparcamiento'

    name = fields.Char('Direccion', required=True)
    plazas = fields.Integer(string='N. de plazas',required=True)

    coche_ids = fields.One2many('odoo_libre.coche','aparcami_id',string='Coches')


class coche(models.Model):
    _name = 'odoo_libre.coche'
    _description = 'Define las caracteristicas de un coche'
    _order = 'name'

    name = fields.Char(string='N. de matricula',required=True, size=7)
    modelo = fields.Char(string= 'Modelo')
    fechaCompra = fields.Date(string='Fecha de compra')
    consumo = fields.Float('Consumo cada 100Km',(4,1),default=0.0)
    anios = fields.Integer(string='Años', default=0)
    descripcion = fields.Text('Descripcion')
    averiado = fields.Boolean(string = 'Averiado', default= False)

    
    aparcami_id = fields.Many2one('odoo_libre.aparcami',string='Aparcamiento')
    servicio_ids = fields.Many2many('odoo_libre.servicio',string ='Servicios')




class servicio(models.Model):
    _name = 'odoo_libre.servicio'
    _description = 'Define las caracteristicas del servicio'
    _order = 'fecha'

    fecha = fields.Date('Fecha', required=True, default = fields.date.today())
    tipo = fields.Selection(string='Tipo servicio', selection=[('l','Lavar'),('r','Revision'),('m','Mecanica'),('p','Pintura')],default = 'l')
    coste = fields.Float('Coste',(8,2), default=0.0)

    coche_ids = fields.Many2many('odoo_libre.coche',string='Coches')

