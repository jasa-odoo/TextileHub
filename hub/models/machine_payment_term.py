# -*- coding: utf-8 -*-
from odoo import models, fields


class MachinePaymentTerm(models.Model):
    _name = "machine.payment.term"
    _description = "Machine Payment Term Model"
    _order = "sequence,id"

    name = fields.Char(required=True, string="Term")
    sequence = fields.Integer('sequence')
