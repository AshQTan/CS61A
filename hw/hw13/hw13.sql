create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs, sizes where min < height and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select child from parents, dogs where parent = name order by height DESC;

-- Sentences about siblings that are the same size

create table sentences as
  with temp(sib1, sib2) as (
  	select a.child, b.child from parents as a, parents as b where a.parent = b.parent and a.child<b.child
  	)
  select sib1 || ' and ' || sib2 || ' are ' || a.size || ' siblings' from temp, size_of_dogs as a, size_of_dogs as b where a.size = b.size and a.name = sib1 and b.name = sib2;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
	with stacked_table(dogs, total, x, lim) as (
		select name, height, 1, height from dogs union
		select dogs || ', ' || name, total+height, x+1, height from stacked_table, dogs where x<4 and lim<height
		)
  select dogs, total from stacked_table where total >= 170 and x = 4 order by total;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
	with mul(num, total) as (
		select a.n, a.n/b.n from ints as a, ints as b where a.n%b.n = 0
		) 
    select num as 'num', count(*) as 'count'
    from mul group by num order by num;

create table primes as
    select a.num from divisors as a where a.count = 2;
