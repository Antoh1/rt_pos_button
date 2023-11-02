# -*- coding: utf-8 -*-
from odoo import http

# class RtPosButt(http.Controller):
#     @http.route('/rt_pos_button/rt_pos_button/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rt_pos_button/rt_pos_button/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rt_pos_button.listing', {
#             'root': '/rt_pos_button/rt_pos_button',
#             'objects': http.request.env['rt_pos_button.rt_pos_button'].search([]),
#         })

#     @http.route('/rt_pos_button/rt_pos_button/objects/<model("rt_pos_button.rt_pos_button"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rt_pos_button.object', {
#             'object': obj
#         })