-- Exercises 1–9 in Section 1, Chapter 5 on pages 164–165

-- 1. Write an INSERT statement that adds this row to the Terms table:
-- terms_id:					6
-- terms_description:			Net due 120 days
-- terms_due_days:				120
-- Use MySQL Workbench to review the column definitions for the Terms table
-- and include a column list with the required columns in the INSERT statement.

INSERT INTO terms(terms_id, terms_description, terms_due_days)
VALUES(6, 'Net due 120 days', 120);

-- 2. Write an UPDATE statement that modifies the row you just added to the
-- Terms table. This statement should change the terms_description column to
-- "Net due 125 days", and it should change the terms_due_days column to 125.

UPDATE terms
SET	terms_description = 'Net due 125 days', terms_due_days = 125
WHERE terms_id = 6;

-- 3. Write a DELETE statement that deletes the row you added to the Terms table
-- in exercise 1.

DELETE from terms
WHERE terms_id = 6;

-- 4. Write an INSERT statement that adds this row to the Invoices table:
-- invoice id:				The next automatically generated ID
-- vendor_id:				32
-- invoice_number:			AX-014-027
-- invoice_date:			8/1/2018
-- invoice_total:			$434.58
-- payment_total:			$0.00
-- credit_total:			$0.00
-- terms_id:				2
-- invoice_due_date:		8/31/2018
-- payment_date:			null
-- Write this statement without using a column list.

INSERT INTO Invoices
VALUES (DEFAULT, 32, 'AX-014-027', '2018-08-01', 434.58, 0, 0, 2, '2018-08-31', NULL);

-- 5. Write an INSERT statement that adds these rows to the Invoice_Line_Items table:
-- invoice_sequence:		1				2
-- account_number:			160				527
-- line_item_amount:		$180.23			$254.35
-- line_item_description:	Hard drive		Exchange Server update
-- Set the invoice_id column of these two rows to the invoice ID that was generated
-- by MySQL for the invoice you added in exercise 4.

INSERT INTO Invoice_Line_Items 
VALUES(115, 1, 160, 180.23, 'Hard drive'),
      (116, 2, 527, 254.35, 'Exchange Server update');

-- 6. Write an UPDATE statement that modifies the invoice you added in exercise
-- 4. This statement should change the credit_total column so it's 10% of the
-- invoice_total column, and it should change the payment_total column so the
-- sum of the payment_total and credit_total columns are equal to the
-- invoice_total column.

SELECT * FROM invoices WHERE invoice_id = 115;
UPDATE invoices
SET credit_total = invoice_total * 0.1,
    payment_total = invoice_total - credit_total
WHERE invoice_id = 115;

-- 7. Write an UPDATE statement that modifies the Vendors table. Change the
-- default_account_number column to 403 for the vendor with an ID of 44.

UPDATE Vendors
SET default_account_number = 403
WHERE vendor_id = 44;

-- 8. Write an UPDATE statement that modifies the Invoices table. Change the
-- terms_id column to 2 for each invoice that's for a vendor with a
-- default_terms_id of 2.

UPDATE Invoices
SET terms_id = 2
WHERE vendor_id IN
    (SELECT vendor_id
     FROM Vendors
     WHERE default_terms_id = 2); 

-- 9. Write a DELETE statement that deletes the row that you added to the Invoices
-- table in exercise 4. When you execute this statement, it will produce an error
-- since the invoice has related rows in the Invoice_Line_Items table. To fix that,
-- precede the DELETE statement with another DELETE statement that deletes
-- the line items for this invoice. (Remember that to code two or more statements
-- in a script, you must end each statement with a semicolon.)

DELETE FROM invoice_line_items
WHERE invoice_id = 115 OR invoice_id = 116;

DELETE FROM invoices
WHERE invoice_id = 115;

