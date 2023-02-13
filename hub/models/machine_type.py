# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineType(models.Model):
    _name = "machine.type"
    _description = "Machine Type Model"

    name = fields.Char(required=True)
    