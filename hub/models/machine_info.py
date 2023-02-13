# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineInfo(models.Model):
    _name = "machine.info"
    _description = "Machine Info Model"

    name = fields.Char(required=True)
    description = fields.Text(required=True)
    product_type_id = fields.Char(required=True, string="Machine Type")
    price = fields.Float()
    date_avilability = fields.Date()
    delivery_time = fields.Char()
    power = fields.Char()
    payment_terms = fields.Char()
    operating_type = fields.Char()
    machine_image = fields.Binary()
    materials = fields.Char()
    production_capacity = fields.Char()
    


