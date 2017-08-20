select sum(a.population) from city a inner join country b on a.countrycode=b.code where continent='Asia';
