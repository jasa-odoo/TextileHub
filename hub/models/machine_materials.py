# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MachineMaterials(models.Model):
    _name = "machine.materials"
    _description = "Machine materials Model"

    name = fields.Char(required=True)
    m_price = fields.Float(required=True,string="price")
    material_type_id = fields.Many2one('machine.material.type', string="Material Type")
    printing_type = fields.Char(compute="_compute_printing_type")



    @api.depends('name')
    def _compute_printing_type(self):
        for record in self:
            if record.name.lower() == "sublimation ink":
                record.printing_type =  "Transfer Printing"
            else:
                record.printing_type = "Direct Fabric Printing"