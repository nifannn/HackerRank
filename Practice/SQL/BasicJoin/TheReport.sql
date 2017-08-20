SELECT IF(g.grade>=8, s.name, null),g.grade,s.marks FROM students s INNER JOIN grades g ON s.marks BETWEEN min_mark AND max_mark ORDER BY g.grade DESC,s.name,s.marks;
