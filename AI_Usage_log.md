Project: Agency ERPNext App
ERPNext Version: v15
Date: 2025-08-28
AI Tool Used: ChatGPT (OpenAI)

| Issue                                  | Prompt Used                                                                | AI Suggested                                                        | What I Implemented                                                                                          |
| -------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Validation logic for Manufacturer Item | “How do I enforce unique fields in ERPNext v15 DocType?”                   | Use `frappe.db.exists` in `validate()` or add Unique field property | Added `frappe.db.exists` in `validate()` to prevent duplicate `(manufacturer, item_code)` entries.          |
| Workspace creation in ERPNext          | “How to create a Workspace programmatically in ERPNext?”                   | Use `frappe.get_doc` with Workspace doctype and `insert()`/`save()` | Created a Workspace manually via Python script after debugging errors with `Name` field.                    |
| Export fixtures for app data           | “How to export fixtures (Custom Field, Workspace, Items) in ERPNext?”      | Use `bench --site <site> export-fixtures` with proper filters       | Exported fixtures including Agencies, Manufacturers, and Items.                                             |
| Debugging Workspace creation errors    | “Why does Workspace creation fail with ValidationError/DoesNotExistError?” | Check mandatory fields, naming, and avoid using deprecated imports  | Fixed workspace creation by correctly setting `name` and `title`, and using `save(ignore_permissions=True)` |
