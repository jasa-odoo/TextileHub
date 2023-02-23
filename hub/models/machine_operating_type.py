# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineOperatingType(models.Model):
    _name = "machine.operating.type"
    _description = "Machine operating type Model"
    _order = "sequence,id"

    name = fields.Char(required=True,requried=True)
    sequence = fields.Integer('sequence')
    