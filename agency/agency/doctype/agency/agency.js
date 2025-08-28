// Copyright (c) 2025, rahla and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Agency", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Agency', {
    refresh(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Create Supplier'), function() {
                frm.call('create_supplier');
            });
        }
    }
});

// List view color for inactive
frappe.listview_settings['Agency'] = {
    get_indicator: function(doc) {
        if (!doc.is_active) {
            return [__("Inactive"), "red", "is_active,=,0"];
        }
        return [__("Active"), "green", "is_active,=,1"];
    }
}
