-- Easy
-- 175. conbine two tables
select FirstName, LastName, City, State
from Person a
         left join Address b on a.PersonId = b.PersonId;

-- 176. Second Highest Salary
select max(salary) as SecondHighestSalary
from employee
where Salary < (select max(salary) from Employee);
-- 182. Duplicate Emails