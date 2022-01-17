SELECT COUNT(*) AS number_of_invoices,
	sum(invoice_total) AS grand_invoice_total
FROM invoices;