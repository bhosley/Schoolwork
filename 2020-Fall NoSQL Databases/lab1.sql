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
