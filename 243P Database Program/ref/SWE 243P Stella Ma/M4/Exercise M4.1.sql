use ap;

-- 1
SELECT vendor_id, SUM(invoice_total)
FROM Invoices
GROUP BY vendor_id;

-- 2
SELECT v.vendor_name, SUM(i.payment_total) AS payment_total_sum
FROM vendors v LEFT JOIN invoices i
  ON v.vendor_id = i.vendor_id
GROUP BY v.vendor_id
ORDER BY payment_total_sum DESC;

-- 3
SELECT v.vendor_name, COUNT(i.invoice_id) AS invoice_count, SUM(invoice_total) AS invoice_total_sum
FROM vendors v LEFT JOIN invoices i
  ON v.vendor_id = i.vendor_id
GROUP BY v.vendor_id
ORDER BY invoice_count DESC;

-- 4
SELECT g.account_description, COUNT(*) AS line_item_count, SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts g JOIN invoice_line_items i
  ON g.account_number = i.account_number
GROUP BY account_description
HAVING line_item_count > 1
ORDER BY line_item_amount_sum DESC;

-- 5
SELECT g.account_description, COUNT(*) AS line_item_count, SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts g JOIN invoice_line_items il
  ON g.account_number = il.account_number
  JOIN invoices i
  ON i.invoice_id = il.invoice_id
WHERE invoice_date BETWEEN '2018-04-01' AND '2018-06-30'
GROUP BY account_description
HAVING line_item_count > 1
ORDER BY line_item_amount_sum DESC;

-- 6
SELECT account_number, SUM(line_item_amount) AS sum_line_item
FROM invoice_line_items
GROUP BY account_number WITH ROLLUP;

-- 7
SELECT v.vendor_name, COUNT(DISTINCT il.account_number) AS count_general_ledger_accounts
FROM vendors v JOIN invoices i
    ON v.vendor_id = i.vendor_id
  JOIN invoice_line_items il
    ON i.invoice_id = il.invoice_id
GROUP BY vendor_name
HAVING count_general_ledger_accounts > 1;

-- 8 
SELECT IF(GROUPING(terms_id) = 1, 'Grand Totals', terms_id) AS terms_id,
       IF(GROUPING(vendor_id) = 1, 'Terms ID Totals', vendor_id) AS vendor_id,
       MAX(payment_date) AS last_payment_date,
       SUM(invoice_total - credit_total - payment_total) AS balance_due
FROM invoices
GROUP BY terms_id, vendor_id WITH ROLLUP;










