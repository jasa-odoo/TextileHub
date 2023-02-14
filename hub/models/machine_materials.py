# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineMaterials(models.Model):
    _name = "machine.materials"
    _description = "Machine materials Model"

    name = fields.Char(required=True)
    m_price = fields.Float(required=True)