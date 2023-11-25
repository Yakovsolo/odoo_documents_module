from odoo.tests.common import TransactionCase
from odoo import fields


class TestDocumentReportWizard(TransactionCase):
    def setUp(self):
        super(TestDocumentReportWizard, self).setUp()
        self.wizard_model = self.env["document.report.wizard"]
        self.document_model = self.env["document.management"]
        self.company = self.env.ref("base.main_company")

    def test_create_wizard(self):
        wizard_data = {
            "date_from": "2023-01-01",
            "date_to": "2023-12-31",
        }
        wizard = self.wizard_model.create(wizard_data)
        self.assertEqual(wizard.date_from, fields.Date.from_string("2023-01-01"))

    def test_print_report(self):
        wizard_data = {
            "date_from": "2023-01-01",
            "date_to": "2023-12-31",
        }
        wizard = self.wizard_model.create(wizard_data)

        document_data = {
            "name": "Test Document",
            "description": "Test Description",
            "company_id": self.company.id,
            "date": "2023-06-15",
        }
        document = self.document_model.create(document_data)

        report_action = wizard.print_my_report()
        self.assertTrue(report_action)

        self.assertIn("context", report_action)

        self.assertIn("report_action", report_action["context"])

        expected_date_from = fields.Date.from_string("2023-01-01")
        self.assertEqual(
            report_action["context"]["report_action"]["data"]["form_data"]["date_from"],
            expected_date_from,
        )

    def test_print_report_no_date(self):
        wizard_data = {}
        wizard = self.wizard_model.create(wizard_data)

        document_data = {
            "name": "Test Document",
            "description": "Test Description",
            "company_id": self.company.id,
            "date": "2023-06-15",
        }
        document = self.document_model.create(document_data)

        report_action = wizard.print_my_report()
        self.assertTrue(report_action)

        self.assertFalse(
            report_action["context"]["report_action"]["data"]["form_data"]["date_from"]
        )

    def test_print_report_with_multiple_documents(self):
        wizard_data = {
            "date_from": fields.Date.from_string("2023-01-01"),
            "date_to": fields.Date.from_string("2023-05-31"),
        }
        wizard = self.wizard_model.create(wizard_data)

        document_data1 = {
            "name": "Document 1",
            "description": "Test Description 1",
            "company_id": self.company.id,
            "date": fields.Date.from_string("2023-03-15"),
        }
        document1 = self.document_model.create(document_data1)

        document_data2 = {
            "name": "Document 2",
            "description": "Test Description 2",
            "company_id": self.company.id,
            "date": fields.Date.from_string("2023-06-20"),
        }
        document2 = self.document_model.create(document_data2)

        document_data3 = {
            "name": "Document 3",
            "description": "Test Description 3",
            "company_id": self.company.id,
            "date": fields.Date.from_string("2023-09-10"),
        }
        document3 = self.document_model.create(document_data3)

        report_action = wizard.print_my_report()
        self.assertTrue(report_action)

        documents_in_report = report_action["context"]["report_action"]["data"][
            "documents"
        ]
        self.assertIn(document1.id, [doc["id"] for doc in documents_in_report])        
        self.assertNotIn(document2.id, [doc["id"] for doc in documents_in_report])
        self.assertNotIn(document3.id, [doc["id"] for doc in documents_in_report])
