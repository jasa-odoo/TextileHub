from odoo import models, fields

class MachineDelivery(models.Model):
    _name = "machine.delivery"
    _description = "Machine Delivery Model"
    _order = "sequence"

    name = fields.Char(required=True, string="State Group")
    states = fields.Many2many('res.country.state',required=True)
    in_state = fields.Char(related="states.code")
    sequence = fields.Integer('sequence')
    delivery = fields.Char(requried=True)
 

    