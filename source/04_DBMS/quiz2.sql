-- quiz part2
-------------------------------
--1. 이름, 직속상사명
SELECT W.ENAME, M.ENAME 직속상사명
FROM EMP W, EMP M
WHERE W.MGR = M.EMPNO(+);
--2. 이름, 급여, 업무, 직속상사명
SELECT W.ENAME, W.SAL, W.JOB, M.ENAME 직속상사명
FROM EMP W, EMP M
WHERE W.MGR = M.EMPNO(+);
--3. 이름, 급여, 업무, 직속상사명 . (상사가 없는 직원까지 전체 직원 다 출력.
    --상사가 없을 시 '없음'으로 출력)
SELECT W.ENAME, W.SAL, W.JOB, NVL(M.ENAME, '없음') 직속상사명
FROM EMP W, EMP M
WHERE W.MGR = M.EMPNO(+);
--4. 이름, 급여, 부서명, 직속상사명
SELECT ENAME, SAL, DNAME, 직속상사명
FROM DEPT D, 
    (SELECT W.ENAME, W.SAL, NVL(M.ENAME, '없음') 직속상사명, W.DEPTNO
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) EMP
WHERE D.DEPTNO = EMP.DEPTNO;
--5. 상사가 없는 직원과 상사가 있는 직원 모두에 대해 이름, 급여, 부서코드, 부서명, 근무지, 직속상사명을 출력하시오(단, 직속상사가 없을 경우 직속상사명에는 ‘없음’으로 대신 출력하시오)
SELECT ENAME, SAL, EMP.DEPTNO, DNAME, LOC, 직속상사명
FROM DEPT D, 
    (SELECT W.ENAME, W.SAL, NVL(M.ENAME, '없음') 직속상사명, W.DEPTNO
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) EMP
WHERE D.DEPTNO = EMP.DEPTNO;
--6. 이름, 급여, 등급, 부서명, 직속상사명. 급여가 2000이상인 사람
SELECT ENAME, SAL, GRADE||'등급'GRADE , DNAME, 직속상사명
FROM DEPT D, SALGRADE,
    (SELECT W.ENAME, W.SAL, NVL(M.ENAME, '없음') 직속상사명, W.DEPTNO
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) EMP
WHERE D.DEPTNO = EMP.DEPTNO
AND EMP.SAL BETWEEN LOSAL AND HISAL;
--7. 이름, 급여, 등급, 부서명, 직속상사명, (직속상사가 없는 직원까지 전체직원 부서명 순 정렬)
SELECT ENAME, SAL, GRADE||'등급'GRADE , DNAME, 직속상사명
FROM DEPT D, SALGRADE,
    (SELECT W.ENAME, W.SAL, NVL(M.ENAME, '없음') 직속상사명, W.DEPTNO
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) EMP
WHERE D.DEPTNO = EMP.DEPTNO
AND EMP.SAL BETWEEN LOSAL AND HISAL
ORDER BY DNAME;
--8. 이름, 급여, 등급, 부서명, 연봉, 직속상사명. 연봉=(급여+comm)*12으로 계산
SELECT ENAME, SAL, GRADE||'등급'GRADE , DNAME, (SAL+NVL(COMM,0))*12 연봉, 직속상사명
FROM DEPT D, SALGRADE,
    (SELECT W.ENAME, W.SAL, NVL(M.ENAME, '없음') 직속상사명, W.DEPTNO, W.COMM
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) EMP
WHERE D.DEPTNO = EMP.DEPTNO
AND EMP.SAL BETWEEN LOSAL AND HISAL;

--9. 8번을 부서명 순 부서가 같으면 급여가 큰 순 정렬
SELECT ENAME, SAL, GRADE||'등급'GRADE , DNAME, (SAL+NVL(COMM,0))*12 연봉, 직속상사명
FROM DEPT D, SALGRADE,
    (SELECT W.ENAME, W.SAL, NVL(M.ENAME, '없음') 직속상사명, W.DEPTNO, W.COMM
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) EMP
WHERE D.DEPTNO = EMP.DEPTNO
AND EMP.SAL BETWEEN LOSAL AND HISAL
ORDER BY DNAME, SAL DESC;

--10. 사원테이블에서 사원명, 사원의 상사를 검색하시오(상사가 없는 직원까지 전체).
SELECT W.ENAME, M.ENAME 직속상사명
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+);

--11. 사원명, 상사명, 상사의 상사명을 검색하시오(self join)
SELECT MGR_EMP.ENAME, 직속상사명, M_MGR.ENAME 상사의직속상사
FROM
    (SELECT W.EMPNO, W.ENAME, M.ENAME 직속상사명, M.MGR
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) MGR_EMP,
        EMP M_MGR
WHERE MGR_EMP.MGR = M_MGR.EMPNO(+);
--12. 위의 결과에서 상위 상사가 없는 모든 직원의 이름도 출력되도록 수정하시오(outer join)
SELECT MGR_EMP.ENAME, 직속상사명, M_MGR.ENAME 상사의직속상사
FROM
    (SELECT W.EMPNO, W.ENAME, M.ENAME 직속상사명, M.MGR
        FROM EMP W, EMP M
        WHERE W.MGR = M.EMPNO(+)) MGR_EMP,
        EMP M_MGR
WHERE MGR_EMP.MGR = M_MGR.EMPNO(+);