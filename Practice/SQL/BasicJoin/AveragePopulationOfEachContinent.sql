select continent, floor(avg(a.population)) from city a inner join country b on a.countrycode=b.code group by continent;
