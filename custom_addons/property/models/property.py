from odoo import models, fields, api

# database model for the property app and their columns
class Property (models.Model):
    _name = 'property'
    name = fields.Char(required = True)
    description = fields.Char()
    post_code = fields.Char(required = 1)
    date_availability = fields.Date()
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

    # Decorators
    # check bedrooms filed if have 0 or not
    @api.constrains('bed_rooms')
    def _check_bedrooms_greater_zero(self):
        for record in self:
            if record.bed_rooms == 0:
                raise models.ValidationError("The number of bedrooms must be greater than zero.")


    # check living_area filed if have 0 or not
    @api.constrains('living_area')
    def _check_living_area_greater_zero(self):
        for record in self:
            if record.living_area == 0:
                raise models.ValidationError("The living area must be greater than zero.")
