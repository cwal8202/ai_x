/* ------ QUIZ ------*/

-- 1. 사번, 이름, 급여를 출력
select pno,pname, pay from personal;

-- 2. 급여가 2000~5000 사이 모든 직원의 모든 필드
select * from personal where pay between 2000 and 5000;

-- 3. 부서번호가 10또는 20인 사원의 사번, 이름, 부서번호
select pno, pname, dno from personal where dno in (10,20);

-- 4. 보너스가 null인 사원의 사번, 이름, 급여 급여 큰 순정렬
select pno, pname, pay from personal where bonus is null order by pay desc;

-- 5. 사번, 이름, 부서번호, 급여. 부서코드 순 정렬 같으면 PAY 큰순
select pno, pname, dno, pay from personal order by dno, pay desc;

-- 6. 사번, 이름, 부서명
select pno, pname, dname from personal p join division d on p.dno = d.dno;

-- 7. 사번, 이름, 상사이름
select p.pno, p.pname, m.pname as '상사이름' from personal p join personal m on p.manager = m.pno;

-- 8. 사번, 이름, 상사이름(상사가 없는 사람도 출력하되 상사가 없는 경우 ★CEO★로 출력)
select p.pno, p.pname, ifnull(m.pname, '★CEO★') as '상사이름' from personal p left outer join personal m on p.manager = m.pno;

-- 8-1 사번, 이름, 상사사번(상사가 없으면 ceo로 출력. ifnull함수의 매개변수의 타입이 상이해도 상관없음)
select p.pno, p.pname, ifnull(m.pno, '★CEO★') as '상사사번' from personal p left outer join personal m on p.manager = m.pno;

-- 8-2. 사번, 이름, 상사이름, 부서명(상사가 없는 사람도 출력) – 같이 합시다
select pno, pname, mname as '상사이름' ,dname from division d 
	join  (select p.dno, p.pno, p.pname, ifnull(m.pname, '★CEO★') as mname
		from personal p left outer join personal m on p.manager = m.pno) as p2
	on d.dno = p2.dno;

select w.pno, w.pname, m.pname, dname
	from division d, personal w left outer join personal m
    on w.manager=m.pno
	where d.dno=w.dno;

-- 9. 이름이 s로 시작하는 사원 이름 (like 이용)
select pname from personal where pname like 's%';

-- 10. 사번, 이름, 급여, 부서명, 상사이름
select pno, pname, pay, dname, pay,mname as '상사이름' from division d 
	join  (select p.pay, p.dno, p.pno, p.pname, ifnull(m.pname, '★CEO★') as mname
		from personal p left outer join personal m on p.manager = m.pno) as p2
	on d.dno = p2.dno;