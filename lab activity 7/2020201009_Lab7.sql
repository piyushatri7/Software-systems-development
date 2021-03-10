#1 
select Fname from Employee where Super_ssn in (select Ssn from Employee where Fname = 'Jennifer' and Lname = 'Wallace');

#q2
select E.fname from employee E,Dependent D where E.ssn = D.Essn AND E.fname = D.Dependent_name AND E.sex = D.sex;

#q3
create view prodx as
select  W.* from works_on W,Project P where P.pname='ProductX' and W.pno = P.pnumber;
select E.fname,E.lname from Employee E,prodx P where E.dno = 5 and  E.ssn = P.essn and P.hours > 10;
drop view prodx;

#q4
select P.Pnumber, P.Dnum, E.lname, E.address, E.bdate 
from Employee E, Department D, Project P 
where P.Plocation = 'Stafford' AND P.dnum = D.dnumber AND D.Mgr_ssn = E.ssn; 

#q5
select E.fname
from Employee E , WORKS_ON W, PROJECT P 
WHERE P.DNUM = 5 AND P.PNUMBER = W.PNO AND W.ESSN = E.SSN 
GROUP BY E.SSN 
having  COUNT(W.PNO) in (select count(pnumber) from project where dnum = 5 group by dnum);