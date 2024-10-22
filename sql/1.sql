-- Please create the ToDo Databse First and then run the command 

create database todo;
use todo;

CREATE TABLE users (
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    task varchar(255),
    deleted INT(1) DEFAULT 0 NOT NULL
);

CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL,
    status int(1) DEFAULT 1,
    deleted int(1) default 0,
    added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
