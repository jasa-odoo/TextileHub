# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class MachineMaterials(models.Model):
    _name = "machine.materials"
    _description = "Machine materials Model"

    name = fields.Char(required=True)
    m_price = fields.Float(required=True, string="price")
    material_type_id = fields.Many2one(
        'machine.material.type', string="Material Type")
    printing_type = fields.Char(compute="_compute_printing_type")
    material_colour_id = fields.Many2many(
        'material.colour', string="Colour", domain="[('material_type_id', '=?', material_type_id)]")
    packing = fields.Char(readonly=True,default="1000ml")
    paper_weight = fields.Char(readonly=True,default="60gsm")

    @api.depends('name')
    def _compute_printing_type(self):
        for record in self:
            if record.name:
                if record.name.lower() == "sublimation ink":
                    record.printing_type = "Transfer Printing"
                elif record.name.lower() == "reactive - pigment ink":
                    record.printing_type = "Direct Fabric Printing"
                else:
                    record.printing_type = None
            else:
                record.printing_type = None
