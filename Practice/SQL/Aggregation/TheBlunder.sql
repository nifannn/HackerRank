select ceil(avg(Salary)-avg(replace(Salary, '0', ''))) from EMPLOYEES;
