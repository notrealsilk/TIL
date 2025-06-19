## SQL

- DB
    
    # DB
    
    체계적인 데이터 모음
    
    **>> 데이터를 구조적 저장, 조작(CRUD)**
    
    ---
    
    - 데이터, 기존 데이터 저장 방식
        
        ### 데이터
        
        저장,처리에 효율적인 형태로 변환된 정보
        
        <aside>
        💡
        
        >> 데이터를 저장, 관리하여 활용하는 기술이 중요해짐
        
        </aside>
        
        ---
        
        ### 기존의 데이터 저장방식
        
        ### 1. 파일(File)
        
        쉽게 사용, 데이터 구조적 관리 어렵
        
        ### 2. 스프레드 시트(Spreadsheet)
        
        테이블의 열, 행을 이용해 **데이터 구조적 관리**
        
        >> but, 크키의 한계 / 보안 (단순한 접근 권한 기능만 제공) /  정확성 (데이터 변경 번거로움)
        
    
    ## 관계형(Relational) DB
    
    데이터 간의 관계가 있는 데이터 항목 모음 >> 데이터를 구조적 저장!!
    
    ---
    
    
    >> 주문 테이블의 고객 ID로 고객 테이블의 pk를 참조
    
    ---
    
    - 테이블, 열,행의 정보를 구조화
    - **서로 관련된 데이터 포인터를 저장 → 엑세스 제공**
        
        : 데이터를 다양한 형식으로 조회 ㅇ
        
    
    ### 용어
    
    ### Table (relation)
    
    데이터 기록하는 곳
    
    ### Field (column, attribute,속성)
    
    각 필드에는 고유한 데이터 타입이 저장
    
    ### Record (row, tuple,행)
    
    각 레코드에는 구체적인 데이터 값이 저장됨
    
    ### Database (schema)
    
    테이블 집합
    
    ### Primary Key (기본키, pk)
    
    각 레코드의 고유한 값
    
    관계형 DB에서 **레코드 식별자** 활용
    
    ### Foreign Key (외래(참조)키,FK)
    
    테이블 필드 중, 다른 테이블의 레코드를 식별할 수 있는 키
    
    다른 테이블의 기본키 참조
    
    각 레코드에서 다른 테이블 간의 **관계 만드는데** 사용
    
    ## RDBMS
    
    Relational Database Management System
    
    ### DBMS (Database Management System)
    
    DB를 관리하는 소프트웨어 프로그램
    
    - db  - 사용자 간 인터페이스 역할
    - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 할 수 있게 함
    
    ### RDBMS
    
    관계형 DB를 관리하는 소프트웨어 프로그램
    
    ---
    
    <aside>
    💡
    
    ### 데이터 베이스 정리
    
    - Table은 데이터가 기록되는 곳
    - Table에는 기본키, 외래키 ㅇ
        - 기본키 : 행에서 고유하게 **식별가능**한 속성
        - 외래키 : 각 행에서 **서로 다른 테이블간 관계** 만듦
    - 데이터는 기본키, 외래키를 통해 join될 수 있는 여러 테이블을 구조화
    </aside>
    
    # SQL (Structure Query Language)
    
    DB에 정보를 저장, 처리하는 프로그래밍 언어 (DB와 소통하는 언어)
    
    : 테이블 형태로 **구조화**된 RDB에게 요청을 **질의(요청)**
    
    ---
    

    ### SQL Syntax
    
    ### 1. SQL 키워드는 대소문자 구분 x
    
    but, **대문자 권장** (..명시적 구분 때문에)
    
    ### 2. 각 SQL Statements 끝에는 세미콜론`;` 필요
    
    각 SQL Statements을 구분하는 방법 (**명령의 마침표**)
    
    ### 3. SQL Statement (셀렉트문)
    
    `SELECT`, `FROM` 으로 구성
    
    ### SQL Statement
    
    ### `SELECT`, `FROM`
    
    ---
    

### - SQL Statement 유형

: **DDL (정의) / DQL (검색) / DML (조작) / DCL (제어)**


---

- Single Table Queries : **DQL (검색)**
    
    # Querying data
    
    ## SELECT
    
    테이블의 데이터 조회, 반환
    
    ### SELECT 필드
    
    - 필드(컬럼) 1개 이상
    
    ### FROM 테이블 이름
    
    - 테이블 1개 이상
    - * (asterisk) 사용하면 모든 필드 선택
    
    ---
    
    ### 활용
    
    - 활용
        - 테이블 employees에서 LastName 필드의 모든 데이터 조회
        
        - 필드 2개 이상 조회하려면 , 로 추가
        
        SELETE LastName, FristName 
        
        FROM  employees;
        
        ---
        
        - 테이블 employees에서 FirstName 필드의 모든 데이터 조회
        

        - 단, 조회 시 FirstName대신 `이름` 으로 출력되도록
        

        ---
        

        - 해당 테이블에서 모든 필드 데이터 조회
        

        ---

        - 테이블  tracks 에서 Name, Millisecond 필드의 모든 데이터 조회
            
            (단, Millisecond 필드는 60000으로 나눠서 분 단위로 출력)
            

    
    ---
    
    # Sorting data
    
    ## ORDER BY
    
    **조회 결과**의 레코드 정렬
    
    ### ORDER BY Syntax
    
    - FROM절(clause) 뒤에 위치
    - 하나 이상의 컬럼을 기준으로 
    오름차순(`ASC`..기본값), 
    내림차순(`DESC`)
    - NULL 값이 있으면, 
    오름차순 시 NULL 먼저
    
    ---
    
    ---
    
    ### 활용
    
    - 활용
        

        - 테이블  customers 에서 **Country 필드를 기준으로 내림차순 → City 필드 기준으로 오름차순 정렬**

        ---
        
        - 테이블 track에서 Milliseconds 필드를 기준으로 내림차순(가장 재생시간이 긴 순서로 정렬), Name,Milliseconds 필드의 모든 데이터를 조회
            
            (단, Millisecond 필드는 60000으로 나눠서 분 단위로 출력)
            
      
        ---
        
        - NULL 값이 존재 → 오름차순 정렬 시 null  먼저 출력
        - 내림차순 시, null이 마지막에 출력

    
    # Filtering data
    
    데이터 조회시, **조건** 걸기
    

    ## DISTINCT
    
    조회 결과에서 중복된 레코드 제거
    
    ---
    
    - SELECT 키워드 바로 뒤에 작성
    - SELECT DISTINCT + 고유한 값을 선택하려는 하나의 이상의 필드
    
    ### 활용
    
    - 활용
        - customers에서 Country 필드이 모든 데이터를 **중복없이** 오름차순 조회

        << 중복있게 조회
        
    
    ## WHERE
    
    조회 시 특정 검색 조건을 지정
    
    ---
    
    - FROM 뒤에 위치
    - search_condition은 비교 연산자, 논리 연산자(and, or, not) 등을 사용
    
    ### 활용
    
    - 활용
        - 테이블 customers에서 / City 필드 값이 Prague인  / 데이터의 LastName, FirstNmae, City 조회
        
        cf)) `WHERE City != ‘Prague’;` << 프라하가 아닌 곳들을 조회
        
        ---
        
        - Company필드 값이 NULL 이고, Country 필드 값이 ‘USA’인 데이터의 LastName,FirstName,Company,Country 조회

        - NULL 값을 조회할 때는
        `IS NULL` 사용!
        
        ---
        
        - Company필드 값이 NULL 이거나 Country 필드 값이 ‘USA’인 데이터의 LastName,FirstName,Company,Country 조회
        
        ---
        
        - 테이블 track에서 10,000≤Byte 필드값≤500,000 이하인 데이터의 Name,Bytes를 Bytes 기준으로 오름차순 조회
        
        - 조회(WHERE) 후 정렬(ORDER BY)
        
        ---

        - customers 에서 Country 필드 값이 Canada, Germany, France인 데이터의 LastName, FirstName, Country 조회
        - 비교 연산자 사용해도 되긴 함..
        - 필드 값이 Canada, Germany, France아닌 데이터
        
        >> `WHERE` 
        
        `Country NOT IN (’Canada’, ‘Germany’, ‘France’)`

        ---

        - 테이블 customers에서 LastName 필드 값이 `son` 으로 끝나는 데이터의 LastName, FirstName 조회

        - `%` : 앞 글자 수 상관 없음
        
        ---

        - 테이블 customers에서 FirstName 필드 값이 4자리 + a 로 끝나는 데이터의 LastName, FirstName 조회
        

    
    ## Operators
    
    ### 비교 연산자

    ### 논리 연산자

    - IN :  값이 특정 목록 안에 있는지 확인
    - LIKE : 값이 특정 패턴에 일치하는지 확인 (Wildcards와 함께 사용)
    
    ### Wildcards
    
    - % : 0개 이상의 문자열과 일치 하는지 확인
    - _ : 단일 문자와 일치하는지 확인
    
    ## LIMIT
    
    조회하는 레코드 수를 제한
    
    ---
    - FROM절 뒤
    - 1~2개 인자 사용 (0~ 양의 정수)
    - row_count :  조회하는 최대 레코드 수 지정
    
    ---

    >> 2 이후 부터 5개 레코드 조회
    
    ### 활용
    
    - 활용
        - 테이블 tracks에서 Trackld, Name,Bytes 필드 데이터를 Bytes 기준 내림차순으로 7개 조회
        
        - (파일이 큰 순서대로 7개 조회)
        
        ---
        
        - tracks에서 TrackID, Name, Bytes 필드 데이터를 Byte기준으로 내림차순하고 4~7번째 데이터 조회
    
    # Grouping data
    
    ## GROUP BY
    
    레코드를 그룹화 → 데이터 요약본 생성 / 집계 함수(AggregationFunctions)와 같이 사용
    
    : SUM, AVG, MAX, MIN, COUNT
    
    ---

    - FROM, WHERE 절 뒤
    - 그룹화 할 필드 목록 작성
    
    <aside>
    💡
    
    ### **HAVING** clause
    
    - 집계 항목에 대한 세부 조건 지정
    - GROUP BY와 함께 사용, GROUP BY가 없으면 WHERE처럼 동작
    : 일반적인 조건과 명시적으로 구분하기 위해 사용
    
    </aside>
    
    ### 활용
    
    - 활용

        >> DISTINCT와 달리 오름차순 정렬도 해줌
        
        ---

        - 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
            - AS 로 바꿀 시, 이름도 같이 바꿔주기
              
        ---

        - 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10 미만인 데이터 조회
        - **HAVING**
        
        ---
        
    
    # SELECT statement 실행순서

- Managing Table : **DDL (정의)**
    
    # Greate a table
    
    ## CREATE TABLE
    
    테이블 생성
    
    ---

    - 각 필드에 적용할 데이터 타입 작성
    - 테이블, 필드의 제약조건(constraint) 작성
        
        >> 데이터 무결성 유지, DB 일관성 보장
        
    
    ### 제약조건 (Constraints)
    
    테이블 필드에 적용되는 규칙, 제한 사항
    
    ### PRIMARY KEY
    
    해당 필드를 기본키로 사용 / INTEGER 타입만 적용
    
    ### NOT NULL
    
    해당 필드에 NULL 값 허용 x
    
    ### FOREIGN KEY
    
    다른 테이블과의 외래 키 관계 정의
    
    ### PRAGMA
    

    |  | ExamID | LastName | FirstName |
    | --- | --- | --- | --- |
    | 데이터 타입 | INTEGER | VARCHAR(50) | VARCHAR(50) |
    | 제약 조건 | PRIMARY KEY | NOT NULL | NOT NULL |
    
    ### AUTOINCREMENT
    
    자동으로 고유한 정수 값을 생성, 할당하는 필드 속성
    
    <aside>
    💡
    
    특징
    
    - **필드가 추가될 때 마다 값이 자동증가 >> 주로 기본키 필드에 적용**
    - INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는
    항상 새로운 레코드에 대해 이전 최대 값보다 큰 값 할당
    - 삭제된 값은 무시, 재사용 x
    </aside>
    
    # Modifying a table fields
    
    ## ALTER TABLE
    
    테이블, 필드 조작
    

    ---
    
    ### ADD COLUMN

    - 추가하고자하는 새 필드 이름, 데이터 타입, 제약 조건 작성
    - 단, 추가하는 필드에 NOT NULL 제약조건이 ㅇ → NULL이 아닌 기본값 설정 필요
    
    - 활용
        - examples 테이블에 Country 필드 추가

        <aside>
        💡
        
        결론적으로, `LastName`과 `FirstName` 열이 `NOT NULL`인데 기본값(`dflt_value`)이 `NULL`로 표시된 것은 **기본값이 따로 설정되지 않은 상태**를 나타내는 것이며, 실제로 값이 비어 있으면 오류가 발생
        
        </aside>
        
        ### **DEFAULT**
        
        열의 기본값을 설정하는 데 사용 / 값을 입력하지 않으면 지정한 기본값이 자동으로 입력
        
        ---
        
        - examples 테이블에 Age, Address 필드 추가
        
        - SQLite는 한번에 여러 필드 추가 불가
        
    
    ### RENAME COLUMN

    이름을 바꾸려는 필드 이름 TO 새 이름
    
    - 활용
        - examples 테이블 Address 필드의 이름을 PostCode로 변경

        ---
        
    
    ### DROP COLUMN

    - DROP COLUMN + 삭제할 필드 이름
    
    - examples 테이블의 PostCode 필드를 삭제
        
    ### RENAME TO
    
    ---
    
    - RENAME TO + 새로운 테이블 이름

    # Delete a table
    
    ## DROT TABLE
    
    테이블 삭제
    
    ---
    

    - 삭제할 테이블 이름 작성

    - 참고
        
        ### 타입 선호도 (Type Affinity)
        
        컬럼에 데이터 타입이 명시적으로 지정x, 지원x면 자동으로 데이터 타입 추론

        >> 유연한 데이터 타입 지원, 간편한 데이터 처리, SQL 호환성..

    
- Modifying Data : **DML (조작)**
    
    # Insert data
    
    테이블 레코드 삽입
    
    ## INSERT

    - INSERT INTO + 테이블 이름 (필드 목록)
    - VALUES (필드에 삽입할 값 목록)
    
    ### 활용
    
    - 활용
        - articles 테이블에 데이터 입력
        
        - 데이터 추가입력

        - DATE 함수로 데이터 추가 입력
    
    # Update data
    
    테이블 레코드 수정
    
    ## UPDATE

    - SET + 수정할 필드, 새 값 지정
    - WHERE + 수정 할 레코드를 지정하는 조건
        
        >> WHERE절 없으면 모든 레코드를 수정함
        
    
    ### 활용
    
    - 활용
        - articles 테이블 1번 레코드의 title 필드 값을 ‘update Title’로 변경
        
        ---
    # Delete data
    
    테이블 레코드 삭제
    
    ## DELETE
    
    - DELETE FROM + 테이블 이름
    - WHERE + 삭제할 조건
    - WHERE절 없으면 모든 레코드 삭제
    
    ### 활용
    
    - 활용
        - articles 테이블의 1번 레코드 삭제
        
        ---
        
        - articles 테이블에서 작성일이 오래된 순으로 레코드 2개 삭제

        - 2개의 경우를 합친 것

- Multi table queries : **DCL (제어)**
    
    # Join
    
    2개 이상의 테이블에서 데이터 검색하는 방법
    
    ### 관계
    
    → 여러 테이블 간의 연결 
    
    : 데이터 관리, 조회의 효율성을 위해 테이블을 분리, 결합할 필요 ㅇ→ **join 사용**
    
    : 테이블 분리 >> 데이터 관리 용이, but 출력시 문제 → 다른 테이블과 결합해서 출력 
    
    → join!!
    
    # INNER JOIN
    
    두 테이블에서 값이 일치하는 레코드에 대해서만 결과 반환 (교집합 결과 반환)
    
    ---
    
    - 사전준비
        
    - FROM + 메인 테이블
    - INNER JOIN + 조인할 테이블
    - ON + 조인 조건 (두 테이블 간의 레코드를 일치시키는 규칙 지정)
    
    ### 활용
    
    - 활용
        - 작성자가 있는 모든 게시글을 작성자 정보와 함께 조회

        ---
        
        - 1번 회원 (하석주)가 작성한 모든 게시글의 제목, 작성자명 조회

        ---
        
    
    # LEFT JOIN
    
    오른쪽 테이블에 일치한 레코드 + 왼쪽 테이블의 모든 레코드 반환

    <aside>
    💡
    
    - 왼쪽 테이블의 모든 테코드 표기
    - 오른쪽 테이블과 매칭되는 레코드 없으면 NULL
    </aside>
    
    ---
    
    - FROM + 왼쪽 테이블
    - LEFT JOIN + 오른쪽 테이블
    - ON + 조인 조건 (왼쪽 테이블의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치 시키기)
    
    ### 활용
    
    - 활용
        - 모든 게시글을 작성자 정보와 함께 조회
                
        ---
        
        - 게시글 작성한 이력이 없는 회원 정보 조회
        
        ---
