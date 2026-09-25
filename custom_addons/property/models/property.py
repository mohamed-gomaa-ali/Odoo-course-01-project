from odoo import models, fields, api

# database model for the property app and their columns
class Property (models.Model):
    _name = 'property'
    name = fields.Char(required = True, size = 25)
    description = fields.Char(default = "bla bla bla", size = 250)
    post_code = fields.Char(required = 1, default = 12345, size = 6)
    date_availability = fields.Datetime(default = fields.Datetime.now())
    expected_price = fields.Float(digits=(0,5))
    selling_price = fields.Float(default = 200.00)
    bed_rooms = fields.Integer(default = 2)
    living_area = fields.Integer(default = 5)
    garage = fields.Boolean(default = 1)
    gardian_area = fields.Integer(default = 25)
    gardian_oriantaition = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West")
        ],
        default= "east"
    )

    # Data tier constrains
    # Make name as a Unique attribute in all rows
    _sql_constraints = [
        ("unique_name", "unique('name')", "you enter an exist name")
    ]

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
