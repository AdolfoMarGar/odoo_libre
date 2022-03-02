# -*- coding: utf-8 -*-
# from odoo import http


# class OdooLibre(http.Controller):
#     @http.route('/odoo_libre/odoo_libre/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_libre/odoo_libre/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_libre.listing', {
#             'root': '/odoo_libre/odoo_libre',
#             'objects': http.request.env['odoo_libre.odoo_libre'].search([]),
#         })

#     @http.route('/odoo_libre/odoo_libre/objects/<model("odoo_libre.odoo_libre"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_libre.object', {
#             'object': obj
#         })
