-- Exercises 1–5 in Section 2, Chapter 11 on pages 379 of the textbook


--  1. Write a script that adds an index to the AP database for the zip code field in
-- the Vendors table.
USE ap;
CREATE INDEX vendors_zip_code_ix
	ON ap.vendors(vendor_zip_code);

-- 2 Write a script that contains the CREATE TABLE statements needed to implement
-- the following design in the EX database:
-- These tables provide for members of an association, and each member can be
-- registered in one or more committees within the association.
-- The member_id and committee_id columns are the primary keys of the
-- Members and Committees tables, and these columns are foreign keys in the
-- Members_ Committees table.
-- Include any constraints or default values that you think are necessary.
-- Include statements to drop the tables if they already exist

USE ex;
DROP TABLE IF EXISTS Members;
CREATE TABLE Members 
(
  member_id     INT           PRIMARY KEY   AUTO_INCREMENT, 
  first_name    VARCHAR(50)   NOT NULL, 
  last_name     VARCHAR(50)   NOT NULL, 
  address       VARCHAR(50)   NOT NULL, 
  city          VARCHAR(50)   NOT NULL, 
  state         CHAR(2)       NOT NULL, 
  postal_code   CHAR(10)      NOT NULL
);

DROP TABLE IF EXISTS Committees;
CREATE TABLE Committees 
(
  committee_id      INT            PRIMARY KEY   AUTO_INCREMENT, 
  committee_name    VARCHAR(50)    NOT NULL
);

DROP TABLE IF EXISTS Members_Committees;
CREATE TABLE Members_Committees
(
  member_id       INT    NOT NULL, 
  committee_id    INT    NOT NULL,
  CONSTRAINT members_committees_fk_members 
	FOREIGN KEY (member_id)	REFERENCES Members (member_id), 
  CONSTRAINT members_committes_fk_committees 
	FOREIGN KEY (committee_id)	REFERENCES Committees (committee_id)
);
    
-- 3 Write INSERT staten1ents that add rows to the tables that are created in exercise 2.
-- Add two rows to the Members table for the first two member IDs.-
-- Add two rows to the Committees table for the first two committee IDs.
-- Add three rows to the Members - Committees table: one row for member 1 and
-- committee 2 ; one for member 2 and committee 1; and one for member 2 and
-- committee 2.
-- Write a SELECT statement that joins the three tables and retrieves the
-- committee name, member last name, and member first name. Sort the results
-- by the com1nittee name, member last name, and member first name.

USE ex;
INSERT INTO Members
VALUES (DEFAULT, 'Peter', 'Anteater', '401 E. Peltason Drive','Irvine','CA','92697'), 
      (DEFAULT, 'Donald', 'Bren', '4011 E. Peltason Drive','Irvine','CA','92697');
    
INSERT INTO Committees
VALUES (DEFAULT, 'UCI ICS'),
	   (DEFAULT, 'UCI Engineering');	

INSERT INTO Members_Committees
VALUES (1, 2),
	   (2, 1),
	   (2, 2);

SELECT c.committee_name, m.last_name, m.first_name
FROM committees c 
	JOIN members_committees mc
		ON c.committee_id = mc.committee_id
    JOIN members m
		ON mc.member_id = m.member_id
ORDER BY c.committee_name, m.last_name, m.first_name;


-- 4. Write an ALTER TABLE statement that adds two new columns to the Members
-- table created in exercise 2.
-- Add one column for annual dues that provides for three digits to the left of the
-- decimal point and two to the right. This column should have a default value of 52.50.
-- Add one column for the payment date.

USE ex;
ALTER TABLE ex.Members
	ADD annual_dues   DECIMAL(5,2)  DEFAULT 52.50,
	ADD payment_date  DATE;

-- 5. Write an ALTER TABLE statement that modifies the Committees table created
-- in exercise 2 so the committee name in each row has to be unique. Then, use an
-- INSERT statement to attempt to insert a duplicate name. This statement should
-- fail due to the unique constraint.

USE ex;
ALTER TABLE ex.Committees
	MODIFY committee_name VARCHAR(50) NOT NULL UNIQUE;

INSERT INTO ex.Committees
	VALUES (DEFAULT, 'UCI ICS'); 
    
