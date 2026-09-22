app_name = "letter_management"
app_title = "Letter Management"
app_publisher = "Babar Mehmood"
app_description = "Directly-created, role-restricted Official Letters with company-specific Letter Heads and an auto reference number."
app_email = "you@example.com"
app_license = "MIT"
required_apps = ["frappe"]

# Uncomment if the Company doctype comes from erpnext in your setup (it
# usually does not need to be, Company is core to Frappe itself).
# required_apps = ["frappe", "erpnext"]

# NOTE: there is intentionally no "before_print" restriction wired up here.
# Whether printing is allowed before Submit is controlled from the Desk UI
# via a Server Script (DocType Event: Before Print, on "Official Letter") -
# see README.md. This keeps that rule editable without touching code or
# redeploying the app.

# Installed/synced on every `bench migrate` - see letter_management/fixtures/.
# - Role: adds "Letter Manager" (create/edit/submit/print) and "Letter User"
#   (read + print only).
# - Custom Field: adds a "Company" Link field to the core "Letter Head"
#   doctype, so Official Letter's Letter Head picker can be filtered to the
#   selected Company.
fixtures = [
	{"doctype": "Role", "filters": [["name", "in", ["Letter Manager", "Letter User"]]]},
	{"doctype": "Custom Field", "filters": [["name", "in", ["Letter Head-company"]]]},
]
