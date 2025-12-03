-- PARTS ORDERING DATABASE SCHEMA --
CREATE DATABASE PartsDB1;
USE PartsDB1;

-- 1. PART --
CREATE TABLE PART (
    PartID INT AUTO_INCREMENT PRIMARY KEY,
    PartName VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2),
    QuantityStock INT
);

-- 2. CUSTOMER --
CREATE TABLE CUSTOMER (
    Cus_Id INT AUTO_INCREMENT PRIMARY KEY,
    F_Name VARCHAR(50),
    L_Name VARCHAR(50),
    ZipCode VARCHAR(20)
);

-- 3. EMPLOYEE --
CREATE TABLE EMPLOYEE (
    Emp_Id INT AUTO_INCREMENT PRIMARY KEY,
    F_Name VARCHAR(50),
    L_Name VARCHAR(50),
    ZipCode VARCHAR(20)
);

-- 4. ORDER --
CREATE TABLE ORDERS (
    Order_Id INT AUTO_INCREMENT PRIMARY KEY,
    PaymentReceived VARCHAR(10),
    ExpectedShipDate DATE,
    ActualShipDate DATE,
    Cus_Id INT,
    Emp_Id INT,
    CONSTRAINT FK_ORDER_CUS FOREIGN KEY (Cus_Id)
        REFERENCES CUSTOMER(Cus_Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT FK_ORDER_EMP FOREIGN KEY (Emp_Id)
        REFERENCES EMPLOYEE(Emp_Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- 5. ORDER_PART --
CREATE TABLE ORDER_PART (
    Order_Id INT,
    CONSTRAINT FK_ORDERPART_ORDER FOREIGN KEY (Order_Id)
        REFERENCES ORDERS(Order_Id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    PartID INT,
    CONSTRAINT FK_ORDERPART_PART FOREIGN KEY (PartID)
        REFERENCES PART(PartID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    QuantityOrd INT
);

-- CUSTOMER DATA --
INSERT INTO CUSTOMER (F_Name, L_Name, ZipCode)
VALUES ('Ali', 'Al-Harthy', '100'),
       ('Mona', 'Al-Maskari', '112');

-- EMPLOYEE DATA --
INSERT INTO EMPLOYEE (F_Name, L_Name, ZipCode)
VALUES ('Salim', 'Al-Balushi', '130'),
       ('Sara', 'Al-Hinai', '111');

-- PART DATA --
INSERT INTO PART (PartName, Price, QuantityStock)
VALUES ('Brake Pad', 12.50, 200),
       ('Oil Filter', 6.75, 150),
       ('Air Filter', 9.90, 120);

-- ORDER DATA --
INSERT INTO ORDERS (PaymentReceived, ExpectedShipDate, ActualShipDate, Cus_Id, Emp_Id)
VALUES ('Yes', '2025-11-20', '2025-11-22', 1, 1),
       ('No', '2025-12-01', NULL, 2, 2);

-- ORDER_PART DATA --
INSERT INTO ORDER_PART (Order_Id, PartID, QuantityOrd)
VALUES (1, 1, 4),   -- Order 1 includes 4 Brake Pads
       (1, 2, 2),   -- Order 1 includes 2 Oil Filters
       (2, 3, 1);   -- Order 2 includes 1 Air Filter
