# models/wizard.py
from odoo import fields, models


class DocumentReportWizard(models.TransientModel):
    _name = "document.report.wizard"
    _description = "Wizard for Document Reports"

    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def print_my_report(self):
        domain = []
        date_from = self.date_from
        if date_from:
            domain += [("date", ">=", date_from)]
        date_to = self.date_to
        if date_to:
            domain += [("date", "<=", date_to)]

        documents = self.env["document.management"].search_read(domain)

        data = {
            "form_data": self.read()[0],
            "documents": documents,
        }

        report = self.env["ir.actions.report"]._get_report_from_name(
            "documents_base.all_documents_template"
        )

        return report.report_action(self, data=data)
