# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Assecories(models.Model):
    _name = "assecories"
    _description = "Assecories Model"

    name = fields.Char(required=True)
    a_price = fields.Float(required=True)
    product_type_id = fields.Char(required=True, string="Machine Type")