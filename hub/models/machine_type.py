# -*- coding: utf-8 -*-
from odoo import models, fields


class MachineType(models.Model):
    _name = "machine.type"
    _description = "Machine Type Model"
    _order = "sequence,id"

    name = fields.Char(required=True)
    sequence = fields.Integer('sequence')
    product_id = fields.One2many('product.template','machine_type_id')
