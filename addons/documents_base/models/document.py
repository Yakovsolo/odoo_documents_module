from odoo import fields, models


class Document(models.Model):
    _name = "document.management"
    _description = "Dokument Information"

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string="Description", required=True)
    company_id = fields.Many2one("res.company", string="Company", required=True)
    date = fields.Date(
        string="Created",
        default=fields.Date.today(),
        required=True,
        date_format="%Y-%m-%d",
    )
