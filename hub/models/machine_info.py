from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineInfo(models.Model):
    _name = "machine.info"
    _description = "Machine Info Model"

    name = fields.Char(required=True)
    description = fields.Char(required=True)
    product_type_id = fields.Char(required=True, string="Product Type")
    price = fields.Float()
    date_avilability = fields.Date()
    delivery_time = fields.Char()
    power = fields.Char()
    payment_term = fields.Char()
    operating_type = fields.Char()
    machine_image = fields.Binary()


