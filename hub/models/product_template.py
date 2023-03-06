# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    description = fields.Text()
    price = fields.Float()
    date_avilability = fields.Date()
    state_group_id = fields.Many2one('machine.delivery')
    states_id = fields.Many2many('res.country.state',compute="_compute_state_id")
    # state_id = fields.Many2one('res.country.state',string="State",domain="[('id', 'in', states_id)]")
    delivery_time = fields.Char(related="state_group_id.delivery")
    power = fields.Char()
    payment_term_id = fields.Many2one('machine.payment.term')
    operating_type_id = fields.Many2one('machine.operating.type',string="Operating Type")
    machine_image = fields.Binary()
    material_type_id = fields.Many2many('machine.material.type', string="Materials")
    production_capacity = fields.Char()
    machine_heads = fields.Integer(string="Number of heads")
    machine_type_id = fields.Many2one('machine.type')
    temperature_req = fields.Char(string="Temperature Requirements",compute="_compute_temperature")
    state = fields.Selection(
        selection=[('in_stock','In Stock'),('out_stock','Out Of Stock')],default="in_stock"
        )
    product_type = fields.Selection(
        selection=[('machine','Machine'),('assecories','Assecories'),('material','Material')]
    )

    @api.depends('machine_type_id')
    def _compute_temperature(self):
        for record in self:
            if record.machine_type_id.name:
                words = record.machine_type_id.name.lower().split(" ")
                if "sublimation" in words:
                    record.temperature_req = "18 - 24 ° C"
                else:
                    record.temperature_req = "Normal"
            else:
                record.temperature_req = None

    @api.depends('state_group_id')
    def _compute_state_id(self):
        for record in self:
            record.states_id = record.state_group_id.mapped('states_id')

    def action_stock_in(self):
        for record in self:
            if record.state != 'in_stock':
                record.state = 'in_stock'

    def action_stock_out(self):
        for record in self:
            if record.state != 'out_stock':
                record.state = 'out_stock'
    # machine_id = fields.Many2one('hub.machine_info', string='Machine')
    # name = fields.Char(delegate=['machine_id.name'])
    # description = fields.Text(delegate=['machine_id.description'])
    # list_price = fields.Float(delegate=['machine_id.price'])
    # default_code = fields.Char(delegate=['machine_id.name'])