# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class MachineMaterials(models.Model):
    _name = "machine.materials"
    _description = "Machine materials Model"

    name = fields.Char(required=True)
    description = fields.Text()
    m_price = fields.Float(required=True, string="price")
    material_type_id = fields.Many2one(
        'machine.material.type', string="Material Type")
    printing_type = fields.Char(compute="_compute_printing_type",readonly=False)
    material_colour_id = fields.Many2many(
        'material.colour', string="Colour", domain="[('material_type_id', '=?', material_type_id)]")
    unit_of_measure = fields.Selection(
        selection=[('unit','Unit'),('ml','ml')]
    )
    material_namee = fields.Char(related = 'material_type_id.name')
    paper_weight = fields.Char()
    material_image = fields.Binary()
    volume = fields.Char()
    state = fields.Selection(
        selection=[('in_stock','In Stock'),('out_stock','Out Of Stock')],
        default="in_stock"
    )

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


    def action_stock_in(self):
        for record in self:
            if record.state != 'in_stock':
                record.state = 'in_stock'

    def action_stock_out(self):
        for record in self:
            if record.state != 'out_stock':
                record.state = 'out_stock'