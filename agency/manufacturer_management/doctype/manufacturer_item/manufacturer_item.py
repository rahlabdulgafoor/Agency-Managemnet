import frappe
from frappe.model.document import Document

class ManufacturerItem(Document):
    def validate(self):
        manufacturer = frappe.get_doc("Manufactur", self.manufacturer) 
        if manufacturer.is_blocked:
            frappe.throw("Cannot add items to a blocked manufacturer.")

        if frappe.db.exists("Manufacturer Item", {
            "manufacturer": self.manufacturer,
            "item_code": self.item_code,
            "name": ("!=", self.name)
        }):
            frappe.throw("This Manufacturer-Item pair already exists.")

        if not self.part_number:
            self.part_number = self.item_code
