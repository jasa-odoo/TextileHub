# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineInfo(models.Model):
    _name = "machine.info"
    _description = "Machine Info Model"
    # _inherits={"product.product" : "product_id"}
    # name = fields.Char(required=True)
    # description = fields.Text(required=True)
    # price = fields.Float()
    # date_avilability = fields.Date()
    # state_group_id = fields.Many2one('machine.delivery')
    # states_id = fields.Many2many('res.country.state',compute="_compute_state_id")
    # # state_id = fields.Many2one('res.country.state',string="State",domain="[('id', 'in', states_id)]")
    # delivery_time = fields.Char(related="state_group_id.delivery")
    # power = fields.Char()
    # payment_term_id = fields.Many2one('machine.payment.term')
    # operating_type_id = fields.Many2one('machine.operating.type',required=True,string="Operating Type")
    # machine_image = fields.Binary()
    # material_type_id = fields.Many2many('machine.material.type', string="Materials")
    # production_capacity = fields.Char()
    # machine_heads = fields.Integer(string="Number of heads")
    # machine_type_id = fields.Many2one('machine.type', required=True)
    # temperature_req = fields.Char(string="Temperature Requirements",compute="_compute_temperature")
    # state = fields.Selection(
    #     selection=[('in_stock','In Stock'),('out_stock','Out Of Stock')],default="in_stock"
    #     )
    # product_id = fields.Many2one('product.product',required=True,ondelete="cascade")
    # # product_ids = fields.One2many('product.product','machine_id', string='Products')

    # @api.depends('machine_type_id')
    # def _compute_temperature(self):
    #     for record in self:
    #         if record.machine_type_id.name:
    #             words = record.machine_type_id.name.lower().split(" ")
    #             if "sublimation" in words:
    #                 record.temperature_req = "18 - 24 ° C"
    #             else:
    #                 record.temperature_req = "Normal"
    #         else:
    #             record.temperature_req = None

    # @api.depends('state_group_id')
    # def _compute_state_id(self):
    #     for record in self:
    #         record.states_id = record.state_group_id.mapped('states_id')

    # def action_stock_in(self):
    #     for record in self:
    #         if record.state != 'in_stock':
    #             record.state = 'in_stock'

    # def action_stock_out(self):
    #     for record in self:
    #         if record.state != 'out_stock':
    #             record.state = 'out_stock'

# class ProductProduct(models.Model):
#      _inherit = "product.product"
