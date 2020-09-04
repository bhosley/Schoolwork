--LAB1A
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS inventory CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;

CREATE TABLE users (                                               
    id SERIAL PRIMARY KEY,                                            
    first_name char(16),                                                   
    last_name char(16),                                                    
    email text NOT NULL,                                               
    password text NOT NULL,                                            
    created_at timestamp,                                              
    updated_at timestamp                                               
); 

CREATE TABLE status (                                              
    id SERIAL PRIMARY KEY,                                                    
    description char(12) NOT NULL,                                                
    created_at timestamp,                                                     
    updated_at timestamp                                                      
);  

CREATE TABLE inventory (                                           
    id SERIAL PRIMARY KEY,
    status_id int,                                             
    CONSTRAINT fk_inventory_status FOREIGN KEY (status_id) REFERENCES status(id),       
    description text NOT NULL,                                         
    created_at timestamp,                                              
    updated_at timestamp                                               
);  

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id int,
    inventory_id int,
    CONSTRAINT fk_transaction_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_transaction_inventory FOREIGN KEY (inventory_id) REFERENCES inventory(id),
    checkout_time timestamp NOT NULL,
    scheduled_checkin_time timestamp,
    actual_checkin_time timestamp,
    created_at timestamp,
    updated_at timestamp 
);

INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
VALUES 
    ('John', 'Doe', 'john.joe@gmail.com', 'p@ssw0rd', current_timestamp, current_timestamp),
    ('Jeff', 'Desmos', 'billions@aws.com', 'lot$ofca$h', current_timestamp, current_timestamp),
    ('Formerly', 'Prince', 'LittleRed@corvette.net', 'PurpleRain', current_timestamp, current_timestamp),
    ('Jessie', 'James', 'wild@west.com', 'RiseAgain', current_timestamp, current_timestamp),
    ('Marshmallow', 'Man', 'Steyer@pufft.io', 'Campfire', current_timestamp, current_timestamp);

INSERT INTO status (description, created_at, updated_at)
VALUES
    ('Available', current_timestamp, current_timestamp),
    ('Checked out',current_timestamp, current_timestamp), 
    ('Overdue', current_timestamp, current_timestamp),
    ('Unavailable', current_timestamp, current_timestamp),
    ('Under Repair', current_timestamp, current_timestamp);

INSERT INTO inventory (status_id, description, created_at, updated_at)
VALUES 
    (1, 'Laptop1', current_timestamp, current_timestamp), 
    (1, 'Laptop2', current_timestamp, current_timestamp), 
    (1, 'Webcam1', current_timestamp, current_timestamp), 
    (1, 'TV1', current_timestamp, current_timestamp), 
    (1, 'Microphone1', current_timestamp, current_timestamp);

INSERT INTO transactions (user_id, inventory_id, checkout_time, scheduled_checkin_time, actual_checkin_time, created_at, updated_at)
VALUES
    (1, 1, current_timestamp, current_timestamp + (30 ||' days')::interval, NULL, current_timestamp, current_timestamp),
    (1, 5, current_timestamp, current_timestamp + (30 ||' days')::interval, NULL, current_timestamp, current_timestamp),
    (2, 4, current_timestamp, current_timestamp + (30 ||' days')::interval, NULL, current_timestamp, current_timestamp);
UPDATE inventory
SET status_id = 2
WHERE id = 1 OR id = 5 OR id = 4 ;

-- 9. Alter the users table to add a column for signed_agreement (Boolean column that defaults to false).
ALTER TABLE users
ADD COLUMN signed_agreement BOOLEAN NOT NULL DEFAULT FALSE;

-- 10. Write a query that returns a list of all the equipment and its scheduled_checkin_time that is checked out ordered by scheduled_checkin_time in descending order.
SELECT inventory.description, transactions.scheduled_checkin_time
FROM inventory
INNER JOIN transactions
    ON inventory.id = transactions.inventory_id
ORDER BY transactions.scheduled_checkin_time DESC;

-- 11. Write a query that returns a list of all equipment due after July 31, 2020. 
SELECT inventory.description
FROM transactions
INNER JOIN inventory
    ON transactions.inventory_id = inventory.id
WHERE scheduled_checkin_time >= '2020-07-31';

-- 12. Write a query that returns a count of the number of items with a status of Checked out by user_id 1. 
SELECT COUNT(*) 
FROM transactions
INNER JOIN inventory
    ON transactions.inventory_id = inventory.id
WHERE user_id = 1 and status_id = 2;

--LAB1B

/***************************** TRANSACTION SIMULATING FUNCTIONS
 * CREATE OR REPLACE FUNCTION checkout (
 *     @user_id int, 
 *     @inventory_id int, 
 *     @checkout_time timestamp DEFAULT current_timestamp, 
 *     @scheduled_checkin_time timestamp DEFAULT current_timestamp + (30 ||' days')::interval, 
 *     @actual_checkin_time timestamp DEFAULT NULL, 
 *     @created_at timestamp DEFAULT current_timestamp, 
 *     @updated_at timestamp DEFAULT current_timestamp)
 * RETURNS text AS $$
 * DECLARE
 *     asset_status int;
 *     transaction_status text;
 * BEGIN
 *     SELECT status_id 
 *     FROM inventory
 *     INTO asset_status
 *     WHERE id = @inventory_id;
 * 
 *     CASE 
 *     WHEN asset_status = 1 THEN
 *         INSERT INTO transactions (user_id, inventory_id, checkout_time, scheduled_checkin_time, actual_checkin_time, created_at, updated_at)
 *             VALUES (@user_id, @inventory_id, @checkout_time, @scheduled_checkin_time, @actual_checkin_time, @created_at, @updated_at);
 *         UPDATE inventory
 *             SET status_id = 2
 *             WHERE id = @inventory_id ;
 *         transaction_status = "Asset successfully checked out."
 *     WHEN asset_status = 2 || asset_status = 3 THEN
 *         transaction_status = "Error! Asset already checked out."
 *     WHEN asset_status = 4 THEN
 *         transaction_status = "Error! Asset is currently unavailable."
 *     WHEN asset_status = 5 THEN
 *         transaction_status = "Error! Asset is currently under repair."
 *     ELSE
 *         transaction_status = "Error! Something went wrong."
 *     END -- END CASE
 *     RETURN asset_status;
 * END;
 * $$ LANGUAGE plpgsql;
 * 
 * CREATE OR REPLACE FUNCTION return (
 *     @transaction_id int,
 *     @return_time timestamp DEFAULT current_timestamp)
 * RETURNS text AS $$
 * DECLARE
 *     asset_status int;
 *     transaction_status text;
 * BEGIN
 *     -- Query for Order's Asset's Status
 *     SELECT status_id
 *     FROM inventory
 *     INNER JOIN transactions
 *     ON inventory.id = transactions.inventory_id
 *     INTO asset_status 
 *     WHERE transactions.id = @transaction_id
 *     
 *     -- If asset was checked out, set to returned and update transaction information
 *     CASE 
 *         WHEN asset_status = 1 THEN
 *             transaction_status = "Error! Asset already returned."
 *         WHEN asset_status = 2 || asset_status = 3 THEN
 *             UPDATE transactions 
 *                 SET 
 *                     actual_checkin_time = @return_time, 
 *                     updated_at = current_timestamp;
 *                 WHERE id = @transaction_id ;
 *             UPDATE inventory
 *                 SET status_id = 1
 *                 WHERE id = @inventory_id ;
 *             transaction_status = "Asset has been successfully returned."
 *         WHEN asset_status = 4 THEN
 *             transaction_status = "Error! Asset is currently unavailable."
 *         WHEN asset_status = 5 THEN
 *             transaction_status = "Error! Asset is currently under repair."
 *         ELSE
 *             transaction_status = "Error! Something went wrong."
 *     END -- END CASE
 *     RETURN asset_status;
 * END;
 * $$ LANGUAGE plpgsql;
 ***************************************************/

/* 1.A
 * Using the tables created in Lab 1 Part 1, insert 20 transactions. 
 * Three of these transactions need to have the actual_checkin_time after the scheduled_checkin_time. 
 * This will allow you to test the view you will be creating in the next steps. 
 * For example, a transaction where the scheduled_checkin_time is 2018-08-01 14:39:53 and the actual_checkin_time is 2018-08-02 14:39:53. 
 * Additionally, five of the transactions need to have a checkout_time after September 3 2018.
 */


-- Dummy Data replicates a records transfer
INSERT INTO transactions (user_id, inventory_id, checkout_time, scheduled_checkin_time, actual_checkin_time, created_at, updated_at)
VALUES --  Checkout             Due Date                                        Actual Return                                   Creation Time       Last Edit
    (1, 1, '2011-08-01 14:39:53', '2011-09-01 14:39:53', '2011-08-11 14:39:53', '2011-08-01 14:39:53', current_timestamp),  
    (2, 2, '2011-03-01 14:39:53', '2011-04-01 14:39:53', '2011-03-11 14:39:53', '2011-03-01 14:39:53', current_timestamp),
    (3, 3, '2011-03-13 14:39:53', '2011-04-13 14:39:53', '2011-03-15 14:39:53', '2011-03-13 14:39:53', current_timestamp),
    (1, 4, '2012-06-21 14:39:53', '2012-07-21 14:39:53', '2012-07-05 14:39:53', '2012-06-21 14:39:53', current_timestamp),
    (2, 1, '2012-08-01 14:39:53', '2012-09-01 14:39:53', '2012-08-11 14:39:53', '2012-08-01 14:39:53', current_timestamp), -- Transaction 5
    (1, 1, '2013-04-15 14:39:53', '2013-05-15 14:39:53', '2013-05-16 14:39:53', '2013-04-15 14:39:53', current_timestamp), -- 1/3 Late Transaction
    (1, 3, '2013-08-01 14:39:53', '2013-09-01 14:39:53', '2014-08-01 14:39:53', '2013-08-01 14:39:53', current_timestamp), -- 2/3 Late Transaction
    (2, 1, '2014-09-01 14:39:53', '2014-10-01 14:39:53', '2020-09-01 14:39:53', '2014-09-01 14:39:53', current_timestamp), -- 3/3 Late Transaction
    (5, 2, '2015-08-01 14:39:53', '2015-09-01 14:39:53', '2015-08-13 14:39:53', '2015-08-01 14:39:53', current_timestamp),
    (5, 3, '2015-09-15 14:39:53', '2015-10-15 14:39:53', '2015-09-27 14:39:53', '2015-09-15 14:39:53', current_timestamp), -- Transaction 10
    (5, 5, '2015-11-01 14:39:53', '2015-12-01 14:39:53', '2015-11-13 14:39:53', '2015-11-01 14:39:53', current_timestamp),
    (3, 4, '2016-04-05 14:39:53', '2016-05-05 14:39:53', '2016-04-20 14:39:53', '2016-04-05 14:39:53', current_timestamp),
    (1, 2, '2017-08-02 14:39:53', '2017-09-02 14:39:53', '2017-08-16 14:39:53', '2017-08-02 14:39:53', current_timestamp),
    (1, 3, '2018-08-02 14:39:53', '2018-09-02 14:39:53', '2018-08-16 14:39:53', '2018-08-02 14:39:53', current_timestamp),
    (1, 5, '2018-08-02 14:39:53', '2018-09-02 14:39:53', '2018-08-16 14:39:53', '2018-08-02 14:39:53', current_timestamp), -- Transaction 15
    (4, 4, '2018-08-05 14:39:53', '2018-09-05 14:39:53', '2018-09-04 14:39:50', '2018-08-05 14:39:53', current_timestamp), -- Transaction 16-20 have a checkout_time after September 3 2018.
    (3, 4, '2019-08-01 14:39:53', '2019-09-01 14:39:53', '2019-08-01 14:39:52', '2019-08-01 14:39:53', current_timestamp),
    (4, 2, '2020-06-01 14:39:53', '2020-07-01 14:39:53', '2020-06-30 14:39:53', '2020-06-01 14:39:53', current_timestamp),
    (5, 4, '2020-06-11 14:39:53', '2020-07-11 14:39:53', '2020-06-26 14:39:53', '2020-06-11 14:39:53', current_timestamp),
    (1, 2, current_timestamp, current_timestamp + (30 ||' days')::interval, NULL, current_timestamp, current_timestamp); -- Transaction 20
UPDATE inventory
SET status_id = 2
WHERE id = 2 ;

/* 1.B
 * Create a late checkins view of distinct items that were checked in late grouped by user_id, inventory_id, and description. 
 * This view should display the total number of late checkins per device per user. 
 * For example, if user1 checked in two items late, there should be two rows displayed for user1 and 
 * each row should include the total number of times that user returned that particular item late. 
 */

CREATE VIEW late AS
SELECT transactions.user_id, transactions.inventory_id, count(transactions.id)
FROM transactions
INNER JOIN inventory
    ON transactions.inventory_id = inventory.id
INNER JOIN users
    ON transactions.user_id = users.id
WHERE transactions.actual_checkin_time > transactions.scheduled_checkin_time
GROUP BY transactions.user_id, transactions.inventory_id;
 
-- 1.C  Test the late checkins view by selecting and displaying all records from the view.

SELECT * FROM late;

-- 2.A On our PostgreSQL VM, run the lab1.sql file from Step 1 to create the tables and data. 
-- 2.B Access our PostgreSQL databases from a Laravel PHP app.  Laravel is a PHP framework.
-- 2.C Execute a query from Laravel using Laravel’s Eloquent Object-Relational Mapping (ORM).
-- 2.D Display our query results on a webpage.

