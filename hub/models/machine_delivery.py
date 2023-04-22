from odoo import models, fields

class MachineDelivery(models.Model):
    _name = "machine.delivery"
    _description = "Machine Delivery Model"
    _order = "sequence"
    _rec_name = "state_group_id"

<<<<<<< HEAD
    state_group_id  = fields.Char(required=True,string="State Group")
    states_id= fields.Many2many('res.country.state',required=True)
=======
    state_group_id  = fields.Char(required=True,string="Country Group")
    state_ids= fields.Many2many('res.country.state',required=True)
>>>>>>> 73534e6 (Report modified)
    sequence = fields.Integer('sequence')
    delivery = fields.Char(required=True)
 

    # country_ids = fields.Many2many('res.country', 'res_country_res_country_group_rel',
    #                                'res_country_group_id', 'res_country_id', string='Countries')
