# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineType(models.Model):
    _name = "machine.type"
    _description = "Machine Type Model"
    _order = "sequence,id"

    name = fields.Char(required=True)
    sequence = fields.Integer('sequence')

    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.id}]{record.name}"
            result.append((record.id, name))
        return result