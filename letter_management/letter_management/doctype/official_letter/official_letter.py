import frappe
from frappe.model.document import Document


class OfficialLetter(Document):
	def autoname(self):
		raw = frappe.db.get_value("Company", self.company, "custom_letter_prefix") or "LTR-000"

		parts = raw.rsplit("-", 1)
		prefix = parts[0]
		start_num = 0
		if len(parts) > 1:
			try:
				start_num = int(parts[1])
			except ValueError:
				prefix = raw
				start_num = 0

		last = frappe.db.sql(
			"""
			SELECT name FROM `tabOfficial Letter`
			WHERE name LIKE %s
			ORDER BY creation DESC LIMIT 1
			""",
			(prefix + "-%",),
		)

		if last:
			last_num = int(last[0][0].split("-")[-1])
		else:
			last_num = start_num - 1

		next_num = last_num + 1
		self.name = f"{prefix}-{next_num:03d}"
