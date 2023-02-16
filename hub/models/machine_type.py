# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineType(models.Model):
    _name = "machine.type"
    _description = "Machine Type Model"
    _order = "sequence,id"

    name = fields._String(required=True)
    sequence = fields.Integer('sequence')