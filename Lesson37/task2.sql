-- Select queries

-- Use the sample SQLite database hr.db

-- SQLite database hr.db link:

-- As a solution to HW, create a file named: task2.sql with all SQL queries:
--     write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
--     write a query to get the unique department ID from the employee table
--     write a query to get all employee details from the employee table ordered by first name, descending
--     write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
--     write a query to get the maximum and minimum salary from the employees table
--     write a query to get a monthly salary (round 2 decimal places) of each and every employee


SELECT first_name as 'First Name', last_name as 'Last Name' from employees;
SELECT department_id FROM employees LIMIT 1;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary*0.12 as PF FROM employees;
SELECT MIN(salary) as MIN, MAX(salary) as MAX FROM employees;
SELECT first_name as 'First Name', last_name as 'Last Name', round(salary/12, 2) as 'Monthly Salary' FROM employees;