
DROP TABLE IF EXISTS collisions;

CREATE TABLE collisions (
    date_str VARCHAR(20),
    time_str VARCHAR(20),
    borough VARCHAR(50),
    zip_code VARCHAR(10),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    on_street_name VARCHAR(100),
    number_of_pedestrians_injured INT,
    number_of_pedestrians_killed INT,
    number_of_cyclist_injured INT,
    number_of_cyclist_killed INT,
    number_of_motorist_injured INT,
    number_of_motorist_killed INT,
    contributing_factor_vehicle_1 VARCHAR(100),
    contributing_factor_vehicle_2 VARCHAR(100),
    contributing_factor_vehicle_3 VARCHAR(100),
    contributing_factor_vehicle_4 VARCHAR(100),
    contributing_factor_vehicle_5 VARCHAR(100),
    collision_id BIGINT PRIMARY KEY,
    vehicle_type_code_1 VARCHAR(50),
    vehicle_type_code_2 VARCHAR(50),
    vehicle_type_code_3 VARCHAR(50),
    vehicle_type_code_4 VARCHAR(50),
    vehicle_type_code_5 VARCHAR(50)
);
USE newyork;

LOAD DATA LOCAL INFILE '/Users/priya/Documents/Projects/Accident/accident.csv'
INTO TABLE collisions
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;



SELECT COUNT(*) FROM collisions;


select * 
from  new_york.acc;