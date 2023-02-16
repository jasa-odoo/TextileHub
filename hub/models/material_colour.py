# -*- coding: utf-8 -*-
from odoo import models, fields

class MaterialColour(models.Model):
    _name = "material.colour"
    _description = "Material Colour Model"

    name = fields.Char()
    material_type_id = fields.Many2many('machine.material.type',string="Only For")


    def name_get(self):
        result = []
        for record in self:
            name = f"[{'00'}{record.id}]{record.name}"
            result.append((record.id, name))
        return result
    
