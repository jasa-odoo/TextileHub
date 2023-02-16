# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineInfo(models.Model):
    _name = "machine.info"
    _description = "Machine Info Model"

    name = fields.Char(required=True,default="machine name")
    description = fields.Text(required=True)
    price = fields.Float()
    date_avilability = fields.Date()
    delivery_time = fields.Char()
    power = fields.Char()
    payment_term_id = fields.Many2one('machine.payment.term')
    operating_type_id = fields.Many2one('machine.operating.type',required=True,string="Operating Type")
    machine_image = fields.Binary()
    material_type_id = fields.Many2many('machine.material.type', string="Materials")
    production_capacity = fields.Char()
    machine_heads = fields.Integer(string="Number of heads")
    machine_type_id = fields.Many2one('machine.type', required=True)
    temperature_req = fields.Char(string="Temperature Requirements",compute="_compute_temperature")

    @api.depends('machine_type_id')
    def _compute_temperature(self):
        for record in self:
            words = record.machine_type_id.name.lower().split()
            if "sublimation" in words:
                record.temperature_req = "18 - 24 ° C"
            else:
                record.temperature_req = "Normal"

