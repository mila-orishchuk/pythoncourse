-- Joins

-- Use the sample SQLite database hr.db (same database you used in the previous lesson for homework tasks)

-- As a solution to HW, create a file named: task1.sql with all SQL queries:

-- write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT em.first_name, em.last_name, em.department_id, dep.department_name
FROM employees 'em'
INNER JOIN department 'dep'
ON em.department_id = dep.department_id;

-- write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT em.first_name, em.last_name, dep.department_name, loc.city, loc.state_province
FROM employees 'em'
INNER JOIN department 'dep', locations 'loc'
ON em.department_id = dep.department_id
AND dep.location_id = loc.location_id;

-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT em.first_name, em.last_name, em.department_id, dep.department_name
FROM employees 'em'
INNER JOIN department 'dep'
ON em.department_id = dep.department_id
AND (em.department_id = 80 OR em.department_id = 40);

-- write a query in SQL to display all departments including those where does not have any employee
SELECT dep.department_id, depart_name, COUNT(employee_id) 'No. employees'
FROM departments 'dep'
LEFT JOIN employees 'em'
ON em.department_id = dep.department_id
GROUP BY dep.department_id

-- write a query in SQL to display the first name of all employees including the first name of their manager
SELECT em.first_name 'first name of employee', mng.first_name 'first name of manager'
FROM employees 'em'
LEFT JOIN employees 'mng' ON em.manager_id = mng.employee_id

-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT j.job_title 'Job Title', em.first_name ||' '|| em.last_name 'Full Name', j.max_salary-em.salary 'Difference'
FROM employees 'em'
INNER JOIN jobs 'j' ON em.job_id = j.job_id;

-- write a query in SQL to display the job title and the average salary of employees
SELECT j.job_title, AVG(em.salary)
FROM employees 'em'
INNER JOIN jobs 'j' ON j.job_id = em.job_id
GROUP BY j.job_title;

-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT em.first_name || ' ' || em.last_name 'Full Name', em.salary 'Salary'
FROM employees 'em'
INNER JOIN departments 'dep' ON dep.department_id = em.department_id
INNER JOIN locations 'loc' ON loc.location_id = dep.location_id
WHERE loc.city = 'London';

-- write a query in SQL to display the department name and the number of employees in each department
SELECT dep.department_name, COUNT(em.department_id)
FROM department 'dep'
INNER JOIN employees 'em' ON dep.department_id = em.department_id
GROUP BY dep.department_name;