from odoo import models, fields

# data base model for the property app and their columns
class PropertyModel (models.Model):
    _name = 'property.model'
    name = fields.Char()
    description = fields.Char()
    post_code = fields.Char()
    date_availabilty = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bed_rooms = fields.Integer()
    living_area = fields.Integer()
    garage = fields.Boolean()
    gardian_area = fields.Integer()
    gardian_oriantaition = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West")
        ]
    )
