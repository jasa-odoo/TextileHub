from odoo import models, fields

class MachineDelivery(models.Model):
    _name = "machine.delivery"
    _description = "Machine Delivery Model"
    _order = "sequence"
    _rec_name = "state_group_id"

    state_group_id  = fields.Char(required=True,string="State Group")
    states_id= fields.Many2many('res.country.state',required=True)
    sequence = fields.Integer('sequence')
    delivery = fields.Char(required=True)
 

   