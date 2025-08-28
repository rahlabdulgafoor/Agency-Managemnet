import frappe
from frappe.model.document import Document

class Agency(Document):
    def validate(self):
        if not self.is_active and self.agency_items:
            frappe.throw("Cannot deactivate an Agency with linked items")

    def on_submit(self):
        pass
# supplerd creation sectuwon
    @frappe.whitelist()
    def create_supplier(self):
        if not frappe.db.exists("Supplier", {"supplier_name": self.agency_name}):
            supplier = frappe.get_doc({
                "doctype": "Supplier",
                "supplier_name": self.agency_name,
                "supplier_group": "All Supplier Groups",
                "territory": self.territory,
                "supplier_type": "Company"
            })
            supplier.insert()
            frappe.msgprint(f"Supplier {supplier.name} created")
        else:
            frappe.throw("Supplier already exists.")
