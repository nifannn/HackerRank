set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor) from
(select case Occupation
        when "Doctor" then @r1:=@r1+1
        when "Professor" then @r2:=@r2+1
        when "Singer" then @r3:=@r3+1
        when "Actor" then @r4:=@r4+1
        end As RowLine,
        case when Occupation="Doctor" then Name end As Doctor,
        case when Occupation="Professor" then Name end As Professor,
        case when Occupation="Singer" then Name end As Singer,
        case when Occupation="Actor" then Name end As Actor
        From Occupations order by Name) As T group by RowLine;
