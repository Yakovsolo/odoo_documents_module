{
    "name": "Documents information",
    "version": "1.0",
    "depends": ["base"],
    "author": "Jakov Solovov",
    "category": "Documents management",
    "description": """
    The module is designed for maintaining a database of company documents.
    """,
    "data": [
        "views/documents_views.xml",
        "views/wizard_view.xml",
        "reports/report.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
