select s.Name from Students as s 
inner join Packages as sp on s.ID=sp.ID
inner join Friends as f on s.ID=f.ID
inner join Packages as fp on f.Friend_ID=fp.ID
where fp.Salary>sp.Salary
order by fp.Salary;
