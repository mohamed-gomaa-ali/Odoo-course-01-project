from odoo import models, fields

# database model for the owner app and their columns
class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required = 1)
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many("property", "owner_id")
    status = fields.Selection(
        [
            ('one_property','1 Property'),
            ('two_property','2 Properties'),
            ('three_property','3 Properties')
        ], default = "one_property"
    )


    # buttons actions
    def action_one_property(self):
        for rec in self:
            rec.status = 'one_property'

    def action_two_property(self):
        for rec in self:
         rec.status = 'two_property'

    def action_three_property(self):
        for rec in self:
          rec.status = 'three_property'