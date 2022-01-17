USE ap;
-- 1
SELECT vendor_name
FROM vendors
WHERE vendor_id IN
     (SELECT DISTINCT vendor_id FROM invoices)
ORDER BY vendor_name;

-- 2
SELECT invoice_number, invoice_total
FROM invoices
WHERE payment_total >
     (SELECT AVG(payment_total)
      FROM invoices
      WHERE payment_total > 0)
ORDER BY invoice_total DESC;

-- 3 
SELECT account_number, account_description
FROM general_ledger_accounts g
WHERE NOT EXISTS
    (SELECT *
     FROM invoice_line_items i
     WHERE i.account_number = g.account_number)
ORDER BY account_number;

-- 4
SELECT vendor_name, i.invoice_id, invoice_sequence, line_item_amount
FROM vendors v JOIN invoices i
	ON v.vendor_id = i.vendor_id
  JOIN invoice_line_items il
	ON i.invoice_id = il.invoice_id
WHERE i.invoice_id IN
      (SELECT DISTINCT invoice_id
       FROM invoice_line_items               
       WHERE invoice_sequence > 1)
ORDER BY vendor_name, i.invoice_id, invoice_sequence;

-- 5
SELECT SUM(invoice_max) AS sum_of_max_unpaid
FROM (SELECT vendor_id, MAX(invoice_total) AS invoice_max
      FROM invoices
      WHERE invoice_total - credit_total - payment_total > 0
      GROUP BY vendor_id) a;
      
-- 6 
SELECT vendor_name,vendor_city,vendor_state
FROM vendors
WHERE CONCAT (vendor_city,vendor_state) in(
	SELECT CONCAT (vendor_city,vendor_state) AS city_state
	FROM vendors
	GROUP BY vendor_city, vendor_state
	HAVING COUNT(*) = 1)
ORDER BY vendor_state,vendor_city;
     
-- 7 
SELECT vendor_name, invoice_number,invoice_date, invoice_total
FROM invoices i JOIN vendors v
  ON i.vendor_id = v.vendor_id
WHERE invoice_date =
  (SELECT MIN(invoice_date)
   FROM invoices 
   WHERE vendor_id = i.vendor_id)
ORDER BY vendor_name;



