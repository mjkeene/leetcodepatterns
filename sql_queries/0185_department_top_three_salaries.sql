-- Write your PostgreSQL query statement below
select "Department", "Employee", "Salary"
from (
    select b.name as "Department", a.name as "Employee", a.salary as "Salary",
    DENSE_RANK() OVER(partition by a.departmentId order by salary desc) as rn
    from Employee a left join Department b on a.departmentId = b.id
    )
where rn <= 3
