# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineMaterialType(models.Model):
    _name = "machine.material.type"
    _description = "Machine Material Type Model"
    _order = "sequence,id"

    name = fields.Char(required=True)
    sequence = fields.Integer('sequence')
    tags_color = fields.Integer()
    