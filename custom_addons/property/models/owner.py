from odoo import models, fields

# database model for the owner app and their columns
class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required = 1)
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many("property", "owner_id")
