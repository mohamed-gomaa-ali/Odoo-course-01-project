from odoo import models, fields

# database model for the tag app and their columns
class Tag(models.Model):
    _name = 'tag'

    name = fields.Char(required = 1)
    property_ids = fields.Many2many("property")
