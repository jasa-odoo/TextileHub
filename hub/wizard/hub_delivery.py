# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ChooseDeliveryCarrier(models.TransientModel):
    _name = 'hub.delivery'
    _description = 'Delivery Selection Wizard'

    
    order_id = fields.Many2one('sale.order', ondelete="cascade")

    state_group_id = fields.Many2one("machine.delivery",string="Country Group",store=True)
    delivery = fields.Char(related="state_group_id.delivery",store=True)

    
    def button_confirm(self):
        self.order_id.delivery_days = self.delivery
        self.order_id.state_group_id =self.state_group_id
        print(self.order_id.delivery_days)

