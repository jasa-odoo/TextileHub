# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ChooseDeliveryCarrier(models.TransientModel):
    _name = 'hub.delivery'
    _description = 'Delivery Selection Wizard'

    address = fields.Char("Address")

    state_group_id = fields.Many2one("machine.delivery",string="Country Group")
    delivery = fields.Char(related="state_group_id.delivery")
    # state_id = fields.Many2many("machine.delivery",readonly=False,string='Country Groups')

    

