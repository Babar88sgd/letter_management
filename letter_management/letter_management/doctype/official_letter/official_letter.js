// Copyright (c) 2026, Letter Management
frappe.ui.form.on("Official Letter", {
	setup(frm) {
		frm.set_query("letter_head", () => ({
			filters: { company: frm.doc.company },
		}));
	},

	company(frm) {
		frm.set_value("letter_head", "");
		if (!frm.doc.company) return;

		frappe.db
			.get_list("Letter Head", {
				filters: { company: frm.doc.company },
				limit: 2,
			})
			.then((rows) => {
				if (rows && rows.length === 1) {
					frm.set_value("letter_head", rows[0].name);
				}
			});
	},
});
