# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineAssecories(models.Model):
    _name = "machine.assecories"
    _description = "Machine assecories Model"

    name = fields.Char(required=True)
    a_price = fields.Float(required=True , string="Price")
    machine_type_id = fields.Many2one('machine.type' ,required=True, string="Machine Type")
    a_image = fields.Binary()

    