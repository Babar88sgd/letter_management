import frappe
from frappe.model.document import Document
from frappe.utils import getdate, nowdate


class OfficialLetter(Document):
	def autoname(self):
		raw = (frappe.db.get_value("Company", self.company, "custom_letter_prefix") or "LTR-001").strip()

		prefix, start_num = self._split_start_number(raw)
		prefix = self._resolve_date_tokens(prefix).rstrip("-.")

		last_num = self._get_last_number(prefix)
		next_num = max(last_num + 1, start_num) if last_num is not None else start_num

		self.name = f"{prefix}-{next_num:03d}"

	def _split_start_number(self, raw):
		"""'CG-100' -> ('CG', 100) | 'CG-.YYYY.-005' -> ('CG-.YYYY.', 5) | 'CG-.YYYY.' -> ('CG-.YYYY.', 1)"""
		parts = raw.rsplit("-", 1)
		if len(parts) == 2 and parts[1].strip().isdigit():
			return parts[0], int(parts[1])
		return raw, 1

	def _resolve_date_tokens(self, prefix):
		"""'.YYYY.', '.YY.', '.MM.', '.DD.' ko current date se replace karta hai"""
		d = getdate(nowdate())
		tokens = {
			"YYYY": d.strftime("%Y"),
			"YY": d.strftime("%y"),
			"MM": d.strftime("%m"),
			"DD": d.strftime("%d"),
		}
		return "".join(tokens.get(p, p) for p in prefix.split("."))

	def _get_last_number(self, prefix):
		"""Isi prefix wale letters mein sab se bara number (sirf numeric suffix)"""
		names = frappe.get_all(
			"Official Letter",
			filters={"name": ["like", f"{prefix}-%"]},
			pluck="name",
		)
		nums = [
			int(n[len(prefix) + 1:])
			for n in names
			if n[len(prefix) + 1:].isdigit()
		]
		return max(nums) if nums else None