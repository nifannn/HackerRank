select N, IF(P IS NULL, 'Root', IF((select count(*) From BST where P=B.N)>0,'Inner', 'Leaf')) From Bst As B order by N;

