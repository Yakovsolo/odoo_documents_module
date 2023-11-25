from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from odoo import fields


class TestDocumentManagement(TransactionCase):
    def setUp(self):
        super(TestDocumentManagement, self).setUp()
        self.Document = self.env["document.management"]
        self.company = self.env.ref("base.main_company")

    def test_create_document(self):
        document_data = {
            "name": "Test Document",
            "description": "Test Description",
            "company_id": self.company.id,
        }
        document = self.Document.create(document_data)
        self.assertEqual(document.name, "Test Document")

    def test_document_date_default_today(self):
        document_data = {
            "name": "Test Document",
            "description": "Test Description",
            "company_id": self.company.id,
        }
        document = self.Document.create(document_data)
        self.assertEqual(document.date, fields.Date.today())
