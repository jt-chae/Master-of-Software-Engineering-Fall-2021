--  1 
CREATE INDEX vendors_zip_code_ix
ON ap.vendors(vendor_zip_code);

-- 2
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
  phone         CHAR(10)      NOT NULL
);

DROP TABLE IF EXISTS Committees;
CREATE TABLE Committees 
(
  committee_id      INT            PRIMARY KEY   AUTO_INCREMENT, 
  committee_name    VARCHAR(50)    NOT NULL
);

DROP TABLE IF EXISTS Members_committees;
CREATE TABLE Members_committees
(
  member_id       INT    NOT NULL, 
  committee_id    INT    NOT NULL,
  CONSTRAINT members_committees_fk_members 
	FOREIGN KEY (member_id)	REFERENCES members (member_id), 
  CONSTRAINT members_committes_fk_committees 
	FOREIGN KEY (committee_id)	REFERENCES committees (committee_id)
);
    
-- 3
USE ex;
INSERT INTO Members
VALUE (DEFAULT, 'John', 'Doe', '37 Turing st.','Irvine','CA','9498340726'), 
      (DEFAULT, 'Stella', 'Ma', '38 Turing st.','Irvine','CA','9498340727');
    
INSERT INTO Committees
VALUES (DEFAULT, 'UCI CS Department'),
	   (DEFAULT, 'UCI Medical Department');

INSERT INTO Members_committees
VALUES (1, 2),
	   (2, 1),
	   (2, 2);

SELECT c.committee_name, m.last_name, m.first_name
FROM committees c JOIN members_committees mc
    ON c.committee_id = mc.committee_id
    JOIN members m
    ON mc.member_id = m.member_id
ORDER BY c.committee_name, m.last_name, m.first_name;


-- 4
ALTER TABLE ex.Members
ADD annual_dues   DECIMAL(5,2)  DEFAULT 52.50,
ADD payment_date  DATE;

-- 5
ALTER TABLE ex.Committees
MODIFY committee_name VARCHAR(50) NOT NULL UNIQUE;

INSERT INTO ex.Committees
VALUES (DEFAULT, 'UCI CS Department'); 