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
select Email from Person group by Email having count(Email)>1;

-- 183. Customers Who Never Order
select Name as Customers from (Customers a left join Orders b on a.Id=b.CustomerId ) where Customerid is null;
select name as customers from customers where customers.id not in (select customerid from orders);

-- 196. Delete Duplicate Emails


-- 596. Classes More Than 5 Students
select class as class from courses group by class having  count(distinct student)>4;