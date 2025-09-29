# Copyright (c) 2025, mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Member(Document):
	def before_validate(self):
		# ensure member_id is set before mandatory validation
		if not getattr(self, 'member_id', None):
			self.member_id = self.name

	def before_insert(self):
		# ensure member_id follows the autoname (MEM series)
		self.member_id = self.name
