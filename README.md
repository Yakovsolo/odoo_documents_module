<img src="addons/documents_base/static/description/icon.png" alt="Module Icon" width="150" align="left">

# Odoo Module: Documents Information

## Overview

The "Documents Information" module is designed for managing a database of company documents within the Odoo platform. It provides functionalities for creating, viewing, and reporting on documents associated with different companies.

## Features

- **Document Management:** Maintain a database of company documents with essential information such as name, description, company affiliation, and creation date.

- **Reporting Wizard:** A wizard allows users to generate reports based on specified date ranges, providing insights into the documents created during that period.

## Installation

To install the module, follow these steps:

1. Make sure the module dependencies are met. The module depends on the "base" module.

2. Copy the module files to the Odoo addons directory.

3. Install the module through the Odoo interface.

## Usage

1. After installation, navigate to the "Documents" menu in Odoo.

2. Create and manage documents by providing necessary details like name, description, company, and creation date.

3. Use the "Reporting Wizard" to generate reports based on specific date ranges.

## Module Structure

The module consists of the following components:

- **Models:**
  - `document.management`: Model for storing document information, including name, description, company affiliation, and creation date.
  - `document.report.wizard`: Wizard model for generating document reports based on date ranges.

- **Views:**
  - `documents_views.xml`: XML file defining the views for displaying document information.
  - `wizard_view.xml`: XML file defining the view for the reporting wizard.

- **Reports:**
  - `report.xml`: XML file defining the structure of the document report.

- **Security:**
  - `ir.model.access.csv`: CSV file specifying access control for the document management model.

## Author

- **Author:** Jakov Solovov

## Version Information

- **Version:** 1.0
