Agency Management ERPNext App

Custom ERPNext app to manage Agencies, Manufacturers, and Items, with validations, workspace setup, and sample data.

Features

Agency management

Manufacturer management with unique (manufacturer, item_code) validation

Auto-fill part_number if blank

Block creation if manufacturer is blocked

REST API to fetch manufacturer mappings

Custom Workspace: “Pharmacy”

Fixtures/sample data:

2 Agencies

3 Items

2 Manufacturers

Prerequisites

Python 3.12+

Node.js 18+

Yarn

Redis, MariaDB/MySQL, and wkhtmltopdf installed

Frappe/ERPNext v15

Setup Instructions for Cloners

Clone the repository

git clone https://github.com/rahlabdulgafoor/Agency-Managemnet.git
cd Agency-Managemnet


Create a new Frappe bench (if not already)

# Install bench if not installed
pip install frappe-bench

# Create bench with ERPNext v15
bench init laundry-bench --frappe-branch version-15 --python python3.12
cd laundry-bench


Create a new site

bench new-site site.demo
# It will ask for MySQL root password and Admin password for ERPNext site


Get the app from local repo

bench get-app ../Agency-Managemnet


Install the app on your site

bench --site site.demo install-app agency


Apply migrations

bench --site site.demo migrate


Load fixtures / sample data

bench --site site.demo import-fixtures


Start the development server

bench start


Access your ERPNext site

Open http://localhost:8000

Login using the Admin password you set

Open the Pharmacy Workspace to see Agencies, Items, and Manufacturers

Testing Instructions

Test creating Agencies, Manufacturers, and Items

Verify validations:

Duplicate (manufacturer, item_code) blocked

Blocked manufacturer prevents item creation

Auto-fills part_number when blank
