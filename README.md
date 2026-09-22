# Letter Management

A simple, role-restricted app for creating official company letters
directly — no request/approval chain, no templates. One doctype:
**Official Letter**.

## Flow

1. A user holding the **Letter Manager** role opens **Official Letter >
   New**, picks the **Company**, picks (or lets it auto-pick) the
   **Letter Head**, and types the letter body into **Letter Content**.
2. They **Submit** it. The naming series (`LTR-.YYYY.-.#####`) becomes its
   official reference/serial number — searchable like any other document.
3. The letter can only be **printed after it is submitted** — this is
   enforced server-side (`before_print`), not just by hiding the Print
   button, so it also blocks a direct hit on the print/PDF URL while the
   letter is still a Draft or has been Cancelled.

## Roles

| Role | Can do |
|---|---|
| `Letter Manager` | Create, edit, submit, cancel, amend, print Official Letters. |
| `Letter User` | Read and print submitted Official Letters only — no create/edit. |

Both roles are installed automatically as **fixtures** on `bench migrate`
(see `letter_management/fixtures/role.json`) — you just need to assign
them to the right users via **User > Roles**.

## Letter Head, filtered by Company

Frappe's core **Letter Head** doctype doesn't have a Company field by
default, so this app adds one via a **Custom Field fixture**
(`letter_management/fixtures/custom_field.json`). Once installed:

- The **Letter Head** picker on Official Letter only shows letterheads
  belonging to the selected **Company**.
- If that Company has exactly **one** Letter Head, it is auto-selected —
  the user doesn't have to pick it manually.

You'll need to set the **Company** field on each of your existing
**Letter Head** records once, after installing this app (Desk > Letter
Head > open each > set Company > Save).

## Doctype

| Doctype | Purpose |
|---|---|
| `Official Letter` | The letter itself. Submittable, auto-numbered, company + letter head + free-text content. |

## Install

```
bench get-app letter_management <this-repo-url>
bench --site <your-site> install-app letter_management
bench --site <your-site> migrate
```

`migrate` also syncs the two Roles and the Letter Head > Company custom
field automatically — nothing else to configure by hand.

## Requirements

Uses only the core `Company` and `Letter Head` doctypes, so plain Frappe
is enough — no `erpnext`/`hrms` dependency (`required_apps` in
`hooks.py` is just `["frappe"]`).
