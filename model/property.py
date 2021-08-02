from odoo import api, fields, models
class customer(models.Model):
    _name = 'aks.customer'
    _description ='Customer'

    name = fields.Char(string='Customer Name')
    phone = fields.Char(string="phone")
    email = fields.Char()

class PropertyTag(models.Model):
    _name = 'prop.tag'
    _description = 'Property Tag'

    name = fields.Char(string='Tag Name')
    color=fields.Integer()

class OfferDetails(models.Model):
    _name = 'offer.details'
    _description = 'Offer Details'

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    partner_id = fields.Many2one('aks.customer', string='')
    prop_id = fields.Many2one('estate.prop', string='Property')
    validity = fields.Integer(string='Validity Days')
    deadline = fields.Date(string='Deadline')

    def accept_offer(self):
        pass

    def decline_offer(self):
        pass

class property(models.Model):
    _name = 'estate.prop'
    _description = 'property'

    ref = fields.Char(string='Ref')
    name = fields.Char(string='Title')
    prop_type = fields.Selection([
        ('apartment', 'Apartment'),('flat', 'Flat'),('rent', 'Rent'),('villa', 'Villa')
    ], string='property Type')

    post_code = fields.Char(string='Post Code')
    
    avail_from = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected price')
    best_offer = fields.Float(string='Best offer')
    selling_price = fields.Float(string='selling price')
    tag_ids = fields.Many2many('prop.tag', string='Tags')

    desc = fields.Char(string='Description')
    bedrooms = fields.Integer(string='Bedrooms')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    living_area = fields.Char(string='Living Area')
    toal_area = fields.Char(string='Total Area(sqft)')

    offer_line_ids = fields.One2many('offer.details', 'prop_id', string='Offer Details')

   
    
