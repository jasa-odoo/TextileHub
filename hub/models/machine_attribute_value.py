# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MachineAttributeValue(models.Model):
    _name = "machine.attribute.value"
    _description = "Machine Attribute Value Model"

    name = fields.Char(string="Value")
    attribute_id = fields.Many2one('machine.attribute')