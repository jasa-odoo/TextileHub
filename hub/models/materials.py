# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Materials(models.Model):
    _name = "materials"
    _description = "Materials Model"

    name = fields.Char(required=True)
    m_price = fields.Float(required=True)