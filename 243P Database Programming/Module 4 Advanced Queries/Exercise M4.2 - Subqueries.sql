-- Exercises 1–7 in Section 2, Chapter 7 on pages 228–229 of the textbook.

/* 1. Write a SELECT statement that returns the same result set as this SELECT
statement, but don't use a join. Instead, use a subquery in a WHERE clause
that uses the IN keyword.
SELECT DISTINCT vendor name
FROM vendors JOIN invoices
	ON vendors.vendor id= invoices.vendor id
ORDER BY vendor_name */

SELECT vendor_name
FROM Vendors
	WHERE vendor_id IN (SELECT DISTINCT vendor_id FROM Invoices)
ORDER BY vendor_name;

/* 2. Write a SELECT statement that answers this question: Which invoices have
a payment total that's greater than the average payment total for all invoices
with a payment total greater than O?
Return the invoice_number and invoice_total columns for each invoice. This
should return 20 rows.
Sort the results by the invoice_total column in descending order.*/

SELECT invoice_number, invoice_total
FROM Invoices
WHERE payment_total >
     (SELECT AVG(payment_total)
      FROM Invoices
      WHERE payment_total > 0)
ORDER BY invoice_total DESC;

/* 3. Write a SELECT statement that returns two columns from the
General_Ledger_Accounts table: account_number and account_description.
Return one row for each account number that has never been assigned to any
line item in the Invoice_Line_Items table. To do that, use a subquery introduced
with the NOT EXISTS operator. This should return 54 rows.
Sort the results by the account_number column.*/

SELECT account_number, account_description
FROM general_ledger_accounts gl
WHERE NOT EXISTS
    (SELECT *
     FROM invoice_line_items i
     WHERE i.account_number = gl.account_number)
ORDER BY account_number;

/* 4. Write a SELECT statement that returns four columns: vendor_name, invoice_id,
invoice_sequence, and line_item_amount.
Return a row for each line item of each invoice that has more than one line
item in the Invoice_Line_Items table. Hint: Use a s·ubquery that tests for
invoice_sequence > 1. This should return 6 rows.
Sort the results by the vendor_name, invoice_id, and invoice_sequence
columns.*/

SELECT vendor_name, i.invoice_id, invoice_sequence, line_item_amount
FROM Vendors v JOIN Invoices i
	ON v.vendor_id = i.vendor_id
  JOIN Invoice_Line_Items il
	ON i.invoice_id = il.invoice_id
WHERE i.invoice_id IN
      (SELECT DISTINCT invoice_id
       FROM Invoice_Line_Items               
       WHERE invoice_sequence > 1)
ORDER BY vendor_name, i.invoice_id, invoice_sequence;


/* 5. Write a SELECT statement that returns two columns: vendor id and the
largest unpaid invoice for each vendor. To do this, you can group the result set
by the vendor_id column. This should return 7 rows.
Write a second SELECT statement that uses the first SELECT statement in its
FROM clause. The main query should return a single value that represents the
sum of the largest unpaid invoices for each vendor.*/

SELECT SUM(invoice_max) AS largest_unpaid_invoices_sum
FROM (SELECT vendor_id, MAX(invoice_total) AS invoice_max
      FROM Invoices
      WHERE invoice_total - credit_total - payment_total > 0
      GROUP BY vendor_id) a;

/* 6. Write a SELECT statement that returns the name, city, and state of each
vendor that's located in a unique city and state. In other words, don't include
ve.ndors that have a city and state in common with another vendor. This
should return 38 rows.
Sort the results by the vendor_state and vendor_city columns.*/

SELECT vendor_name, vendor_city, vendor_state
FROM Vendors
WHERE CONCAT (vendor_city, vendor_state) IN(
	SELECT CONCAT (vendor_city, vendor_state) AS city_state
	FROM vendors
	GROUP BY vendor_city, vendor_state
	HAVING COUNT(*) = 1)
ORDER BY vendor_state, vendor_city;

/* 7. Use a correlated subquery to return one row per vendor, representing the
vendor's oldest invoice (the one with the earliest date). Each row should
include these four columns: vendor_name, invoice_number, invoice_date, and
invoice- total. This should return 34 rows.
Sort the results by the vendor_name column.*/

SELECT vendor_name, invoice_number, invoice_date, invoice_total
FROM Invoices i JOIN Vendors v
  ON i.vendor_id = v.vendor_id
WHERE invoice_date =
  (SELECT MIN(invoice_date)
   FROM Invoices 
   WHERE vendor_id = i.vendor_id)
ORDER BY vendor_name;