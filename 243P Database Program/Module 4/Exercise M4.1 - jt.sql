-- Exercises 1–8 in Section 2, Chapter 6 on pages 196–197 of the textbook
USE ap;
-- 1. Write a SELECT statement that returns one row for each vendor in the
-- Invoices table that contains these columns:
-- The vendor_id column from the Invoices table
-- The sum of the invoice- total columns in the Invoices table for that vendor
-- This should return 34 rows.

SELECT vendor_id, SUM(invoice_total)
	FROM Invoices
GROUP BY vendor_id;

/*2. Write a SELECT statement that returns one row for each vendor that contains
these columns:
The vendor_name column from the Vendors table
The sum of the payment_total columns in the Invoices table for that vendor
Sort the result set in descending sequence by the payment total sum for each
vendor.*/

SELECT v.vendor_name, SUM(i.payment_total) AS payment_total_sum
FROM Vendors v LEFT JOIN Invoices i
  ON v.vendor_id = i.vendor_id
GROUP BY v.vendor_id
ORDER BY payment_total_sum DESC;

/*3. Write a SELECT statement that returns one row for each vendor that contains
three columns:
The vendor name column from the Vendors table
The count of the invoices in the Invoices table for each vendor
The sum of the invoice_total columns in the Invoices table for each vendor
Sort the result set so the vendor with the most invoices appears first. */

SELECT v.vendor_name, COUNT(i.invoice_id) AS invoices_count, SUM(i.invoice_total) AS invoice_total_sum
FROM Vendors v LEFT JOIN Invoices i
  ON v.vendor_id = i.vendor_id
GROUP BY v.vendor_id
ORDER BY invoices_count DESC;

/* 4. Write a SELECT statement that returns one row for each general ledger
account number that contains three columns:
The account_description column from the General_Ledger_Accounts table
The count of the items in the Invoice_Line_Items table that have the same
account_number.
The sum of the line item amount columns in the Invoice_Line_Items table
that have the same account_number
Return only those rows where the count of line items is greater than 1. This
should return 10 rows.
Group the result set by the account_description column.
Sort the result set in descending sequence by the sum of the line item
a1nounts.*/

SELECT gl.account_description, COUNT(*) AS line_item_count, SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts gl JOIN invoice_line_items i
  ON gl.account_number = i.account_number
GROUP BY account_description
HAVING line_item_count > 1
ORDER BY line_item_amount_sum DESC;

/*5. Modify the solution to exercise 4 so it returns only invoices dated in the
second quarter of 2018 (April 1, 2018 to June 30, 2018). This should still
return 10 rows but with some different line item counts for each vendor. Hint:
Join to the Invoices table to code a search condition based on invoice_date. */

SELECT gl.account_description, COUNT(*) AS line_item_count, SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts gl JOIN invoice_line_items il
  ON gl.account_number = il.account_number
	JOIN invoices i
		ON i.invoice_id = il.invoice_id
	WHERE invoice_date BETWEEN '2018-04-01' AND '2018-06-30'
GROUP BY account_description
HAVING line_item_count > 1
ORDER BY line_item_amount_sum DESC;

/* 6. Write a SELECT statement that answers this question: What is the total
amount invoiced for each general ledger account number? Return these
columns:
The account number column from the Invoice Line Items table - - -
The sum of the line_item_amount columns from the Invoice_Line_Items
table
Use the WITH ROLLUP operator to include a row that gives the grand total.
This should return 22 rows. */

SELECT account_number, SUM(line_item_amount) AS line_item_sum
FROM invoice_line_items
GROUP BY account_number WITH ROLLUP;

/* 7. Write a SELECT statement that answers this question: Which vendors are
being paid from more than one account? Return these columns:
The vendor name column from the Vendors table
The count of distinct general ledger accounts that apply to that vendor's
invoices
This should return 2 rows. */

SELECT v.vendor_name, COUNT(DISTINCT il.account_number) AS distinct_general_ledger_accounts_count
FROM vendors v JOIN invoices i
    ON v.vendor_id = i.vendor_id
  JOIN invoice_line_items il
    ON i.invoice_id = il.invoice_id
GROUP BY vendor_name
HAVING distinct_general_ledger_accounts_count > 1;

/* 8. Write a SELECT statement that answers this question: What are the last
payment date and total amount due for each vendor with each terms id?
Return these columns:
The terms id column from the Invoices table
The vendor id column from the Invoices table
The last payment date for each combination of terms id and vendor id in the
Invoices table
The sum of the balance due (invoice_total - payment_total - credit_total)
for each combination of terms id and vendor id in the Invoices table
Use the WITH ROLLUP operator to include rows that give a summary for
each terms id as well as a row that gives the grand total. This should return 40
rows.
Use the IF and GROUPING functions to replace the null values in the terms_id
and vendor_id columns with literal values if they're for st1mmary rows. */

SELECT IF(GROUPING(terms_id) = 1, 'Grand_Total', terms_id) AS terms_id,
       IF(GROUPING(vendor_id) = 1, 'Terms_ID Total', vendor_id) AS vendor_id,
       MAX(payment_date) AS last_payment_date,
       SUM(invoice_total - credit_total - payment_total) AS balance_due
FROM invoices
GROUP BY terms_id, vendor_id WITH ROLLUP;
