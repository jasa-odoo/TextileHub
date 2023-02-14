# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineOperatingType(models.Model):
    _name = "machine.operating.type"
    _description = "Machine operating type Model"

    name = fields.Char(required=True)