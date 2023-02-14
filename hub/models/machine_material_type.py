# -*- coding: utf-8 -*-
from odoo import models, fields

class MachineMaterialType(models.Model):
    _name = "machine.material.type"
    _description = "Machine Material Type Model"

    name = fields.Char(required=True)