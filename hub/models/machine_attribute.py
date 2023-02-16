# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MachineAttribute(models.Model):
    _name = "machine.attribute"
    _description = "Machine Attribute Model"

    name = fields.Char(string="Attribute Name")
    value_id = fields.One2many('machine.attribute.value','attribute_id')