from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    delivery_days = fields.Char("Delivery Days")
    state_group_id =fields.Many2one("machine.delivery")

    def action_open_delivery_wizard(self):
        view_id = self.env.ref('hub.hub_delivery_view_form').id
        return {
            'name': 'Delivery',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hub.delivery',
            'view_id': view_id,
            'views': [(view_id, 'form')],
            'target': 'new',
            'context': {
                'default_order_id': self.id,
            }

        }

