# PART 1. 객관식 정답 + 선지별 해설

## A. Spring 개요, 로깅, 테스트

### 1. ②

① 오답. Spring Boot는 Spring 위에서 동작하며 DI 컨테이너를 그대로 사용한다.
② 정답. Spring Boot는 Spring 애플리케이션을 빠르게 개발하기 위한 일종의 템플릿이며, 핵심은 설정 자동화이다.
③ 오답. 자동 구성 덕분에 XML 설정 없이 실행할 수 있다.
④ 오답. 웹이 아닌 배치·콘솔 애플리케이션에도 사용할 수 있다.

### 2. ④

① 오답. Slf4j는 구현체가 아니라 인터페이스(Facade)이며 실제 기록은 Logback 등이 담당한다.
② 오답. trace, debug, info, warn, error 5단계로 로그를 구별한다.
③ 오답. 레벨별로 출력 여부를 제어할 수 있다는 점이 println과 다르다.
④ 정답. Facade 패턴은 복잡한 구조를 단순한 인터페이스로 제공하는 패턴이며, Slf4j는 Logback·Log4j를 구현체로 사용한다.

### 3. ③

① 오답(옳은 설명). Fast는 외부 환경에 의존하지 않고 빠르게 동작해야 한다는 원칙이다.
② 오답(옳은 설명). Independent는 테스트끼리 상태를 공유하지 않아야 한다는 원칙이다.
③ 정답(옳지 않은 설명). Repeatable은 여러 번 반복해도 항상 동일하게 동작해야 한다는 원칙이다.
④ 오답(옳은 설명). Self-Validating은 사람이 확인하지 않아도 테스트가 스스로 검증해야 한다는 원칙이다. 나머지 Timely는 TDD라면 프로덕션 코드 전에 테스트를 작성한다는 원칙이다.

### 4. ①

① 정답. given은 테스트에 필요한 상황 준비(회원 객체 생성), when은 테스트할 메서드 실행(join), then은 결과 검증(assertEquals)이다.
② 오답. 객체를 준비하는 부분이 given이다.
③ 오답. assertEquals로 결과를 확인하는 부분이 then이다.
④ 오답. 순서가 반대로 되어 있다.

### 5. ③

① 오답. 특정 메서드만 격리해 빠르게 검증하는 것은 단위 테스트의 특징이다.
② 오답. @SpringBootTest는 스프링 컨테이너를 띄우고 빈을 주입받아 테스트한다.
③ 정답. @SpringBootTest는 애플리케이션 전체를 구동하는 통합 테스트용 어노테이션이라 특정 동작만 보는 단위 테스트에는 부적합하다.
④ 오답. static으로 선언해야 하는 것은 @BeforeAll, @AfterAll이며 @SpringBootTest는 클래스에 붙인다.

## B. DI와 Bean 관리

### 6. ④

① 오답. getBean(타입)은 이름과 관계없이 타입으로 조회하며, WasherUser 타입 빈이 하나뿐이라 정상 조회된다.
② 오답. @Configuration 클래스는 CGLIB 프록시로 동작해 sWasher()를 다시 호출해도 컨테이너의 기존 빈을 반환한다.
③ 오답. @Bean 메서드 안에서 생성자 주입이나 setter 주입 모두 사용할 수 있다.
④ 정답. 스프링은 빈을 싱글톤으로 관리하므로 user에 주입된 Washer와 getBean(SWasher.class)로 꺼낸 객체는 같아 true가 출력된다. 빈 이름은 myWasherUser, sWasher, lWasher이다.

### 7. ①

① 정답. @Component는 "빈이 될 수 있다"는 의도만 나타내며, @ComponentScan이 대상을 스캔해야 실제 빈으로 등록된다.
② 오답. 스캔 범위에 포함되지 않으면 @Component가 있어도 빈으로 등록되지 않는다.
③ 오답. @Component의 value 속성으로 빈 이름을 재정의할 수 있다.
④ 오답. @Autowired는 타입 기반 주입이며, 같은 타입이 여러 개면 충돌이 나서 @Qualifier로 이름 조건을 추가해야 한다.

### 8. ②

① 오답(옳은 연결). @Repository는 DAO 계열 빈에 쓴다.
② 정답(옳지 않은 연결). @Service는 Model의 Service 계열 빈에 쓰며, 클라이언트 요청을 받는 빈은 @Controller이다.
③ 오답(옳은 연결). @Configuration은 Java 기반 설정 클래스에 쓴다.
④ 오답(옳은 연결). @Component는 다른 스테레오타입에 해당하지 않을 때 쓴다.

## C. Spring MVC 요청 처리

### 9. ③

① 오답. 클래스 레벨 @RequestMapping 경로는 모든 메서드 경로의 prefix가 된다.
② 오답. @PostMapping은 POST 요청만 처리한다.
③ 정답. 클래스의 /board와 메서드의 경로가 합쳐져 GET /board/list, POST /board/write가 된다. @GetMapping, @PostMapping은 @RequestMapping의 method 속성을 축약한 것이다.
④ 오답. @RequestMapping은 클래스 레벨과 메서드 레벨 모두에서 사용할 수 있다.

### 10. ①

① 정답. @RequestParam은 파라미터 이름과 같은 변수에 값을 매핑하고 자동 형 변환도 해 준다. name 속성("num3")을 지정하면 다른 변수명(result)으로 받을 수 있다.
② 오답. 이름을 지정했으므로 result라는 파라미터가 아니라 num3을 찾는다.
③ 오답. Integer 등으로 자동 형 변환을 지원한다.
④ 오답. 메서드 이름은 파라미터 바인딩과 관계없다.

### 11. ④

① 오답. @ModelAttribute는 프로퍼티 이름을 기준으로 setter를 호출해 값을 채운다.
② 오답. 생성된 객체는 자동으로 Model에 attribute로 추가된다.
③ 오답. JSON 본문을 메시지 컨버터로 읽는 것은 @RequestBody이다.
④ 정답. 기본 생성자로 객체를 만들고(없으면 유일한 생성자 사용) setter로 프로퍼티를 설정한 뒤, 클래스 이름을 카멜 케이스로 바꾼 member라는 이름으로 Model에 추가한다.

### 12. ②

① 오답. @CookieValue는 @RequestParam처럼 자동 형 변환을 지원한다.
② 정답. 변수 이름과 같은 이름의 쿠키 값을 가져오며, int 같은 타입으로 자동 변환된다.
③ 오답. 쿠키 생성은 기존처럼 응답에 Cookie를 추가하는 방식으로 직접 해야 한다.
④ 오답. 요청 파라미터를 바인딩하는 것은 @RequestParam이다.

### 13. ③

① 오답. 일반적으로 뷰 이름만 전달하면 forward로 처리되고, redirect할 때 redirect: 접두사를 붙인다.
② 오답. RedirectAttributes의 일반 속성은 query string으로 전달되므로 문자열 데이터만 보낼 수 있다.
③ 정답. Flash Scope는 redirect가 완료될 때까지만 저장되는 일회성 스코프이며, 범위는 request < flash < session이다.
④ 오답. session에 넣은 단발성 데이터는 사용 후 직접 지워야 하는 번거로움이 있다.

## D. MyBatis

### 14. ①

① 정답. namespace는 DAO 인터페이스와 연결하기 위해 Fully Qualified Name을 쓰고, id는 연결할 DAO 메서드 이름을 쓰는 것이 권장된다.
② 오답. @Mapper 인터페이스는 런타임에 MyBatis가 구현체 프록시를 생성한다.
③ 오답. ? 대신 #{propertyName} 형태로 작성한다.
④ 오답. useGeneratedKeys는 Auto Increment로 생성된 키를 사용할지 정하는 속성이다.

### 15. ④

① 오답. 컬럼명에 해당하는 setter가 있을 때만 자동 매핑된다. detail_address에 해당하는 setter는 없다.
② 오답. parameterType은 SQL에 전달될 파라미터 타입이며 이름 변환과 관계없다.
③ 오답. 대소문자를 바꿔도 밑줄은 사라지지 않는다.
④ 정답. application.properties에 mybatis.configuration.map-underscore-to-camel-case=true를 설정하거나, resultMap에서 column과 property를 직접 매핑한다. 컬럼에 alias를 주는 방법도 있다.

### 16. ②

① 오답. foreach는 OR 조건이 아니라 open, separator, close로 IN 절을 만든다.
② 정답. where 태그가 WHERE를 붙이고, open에 지정한 문자열 뒤에 각 item을 separator로 구분한 뒤 close를 붙인다.
③ 오답. where 태그는 하위 내용이 있으면 앞에 WHERE를 붙인다.
④ 오답. separator로 지정한 쉼표가 각 item 사이에 들어간다.

### 17. ④

① 오답. choose는 여러 조건 중 처음 만족한 하나만 적용한다.
② 오답. otherwise는 모든 when이 거짓일 때만 적용된다.
③ 오답. when이 하나라도 참이면 otherwise는 적용되지 않는다.
④ 정답. 첫 번째 when의 title 조건이 참이므로 그것만 적용되고, mno 조건과 otherwise는 무시된다.

### 18. ①

① 정답. #{}는 PreparedStatement의 ?를 대체하는 값 바인딩이라 SQL 문장 자체는 바꾸지 않으며 SQL Injection에 안전하다.
② 오답. 문자열을 그대로 치환해 문장 자체를 재구성할 수 있는 것은 ${} 표기이다.
③ 오답. #{}는 값을 바인딩하므로 SQL Injection을 방지한다.
④ 오답. 컬럼명·테이블명 같은 구조를 바꾸는 데에는 #{}를 쓸 수 없다.

## E. AOP, Interceptor, 요청 흐름

### 19. ③

① 오답. 횡단 관심 코드를 모듈화한 메서드는 advice이다. target은 AOP가 적용될 핵심 비즈니스 로직 빈이다.
② 오답. advice 적용 대상을 결정하는 표현식은 pointcut이다. join point는 advice가 동작하는 지점으로, Spring에서는 메서드 실행 시점으로 제한된다.
③ 정답. weaving은 aspect를 비즈니스 로직 코드에 적용하는 행위 자체이다.
④ 오답. aspect는 모듈화된 횡단 관심사의 추상적 명칭으로 하나 이상의 advice로 구성된다.

### 20. ②

① 오답. postHandle과 afterCompletion은 역순으로 호출된다.
② 정답. preHandle은 등록 순서인 A → B로, postHandle과 afterCompletion은 역순인 B → A로 호출된다.
③ 오답. preHandle은 등록된 순서대로 호출된다.
④ 오답. postHandle은 컨트롤러 실행 이후에 호출된다.

### 21. ④

① 오답. Filter는 WAS 수준에서 DispatcherServlet에 도달하기 전에 동작한다.
② 오답. HandlerMapping으로 호출할 컨트롤러를 찾은 뒤 인터셉터의 preHandle이 실행된다.
③ 오답. HandlerMapping은 DispatcherServlet이 요청을 받은 뒤 사용한다.
④ 정답. 사용자 요청 → Filter → DispatcherServlet → HandlerMapping → HandlerInterceptor → Controller → HandlerInterceptor(후처리) → ViewResolver → View → HTTP 응답 순서이다.

# PART 2. 단답형 정답 및 해설

## F. 핵심 개념 단답형

### 22.

**정답: @Builder.Default**

해설: @Builder는 내부적으로 모든 필드를 기본값(null, 0 등)으로 초기화하므로, 필드에 지정한 초기값을 유지하려면 @Builder.Default를 붙인다.

### 23.

**정답: Assertion (Assertions)**

해설: Assertion은 메서드 호출 결과가 예상한 값과 같은지 판단하는 문장이다. JUnit 5는 Assertions 클래스로 assertEquals, assertTrue 등을 제공한다.

### 24.

**정답: @BeforeAll, @AfterAll**

해설: 두 어노테이션은 테스트 인스턴스와 관계없이 클래스 단위로 한 번 실행되므로 static으로 선언한다. @BeforeEach, @AfterEach는 각 테스트 전후에 실행된다.

### 25.

**정답: ㉠ SET, ㉡ , (쉼표)**

해설: prefix는 처리 후 내용이 있으면 앞에 붙일 문자열이고, suffixOverrides는 내용의 맨 뒤에 해당 문자열이 있으면 삭제한다. 따라서 SET을 붙이고 마지막 쉼표를 지우는 set 태그와 같은 역할을 한다.

### 26.

**정답: ㉠ include, ㉡ refid**

해설: sql 태그로 재사용할 SQL 조각을 선언하고, 참조할 곳에서 include 태그의 refid 속성에 sql의 id를 지정한다.

### 27.

**정답: CDATA (CDATA section)**

해설: <![CDATA[ ... ]]>로 감싸면 내부를 XML로 해석하지 않아 부등호를 그대로 쓸 수 있다. 또는 &lt;, &gt;, &le;, &ge; 같은 치환 문자를 사용한다.

### 28.

**정답: Flash Scope**

해설: RedirectAttributes의 addFlashAttribute로 저장하며, redirect된 요청에서 한 번 사용된 뒤 사라진다. Flash Scope로 전달할 수 없는 경우에는 Fall Back으로 query string을 사용한다.

### 29.

**정답: DataAccessException**

해설: 스프링은 JDBC의 SQLException 같은 기술별 예외를 DataAccessException 계층으로 변환해 전파한다. 이 덕분에 Controller와 Service는 데이터 접근 기술에 종속되지 않는다.

### 30.

**정답: @AfterThrowing**

해설: @AfterReturning은 정상 완료 시, @After는 결과와 관계없이 완료 시, @AfterThrowing은 예외 발생 시에만 동작한다. @Around는 타겟 메서드 호출 전과 후 모두를 감싼다.

# PART 3. 서술형 모범답안 및 해설

## G. 비교 서술형

### 31.

**모범답안:**
① 동작 수준과 가로채는 대상: Filter는 WAS(서블릿 컨테이너) 수준에서 동작하며 DispatcherServlet에 도달하기 전에 웹 요청·응답 자체를 가로챈다. Interceptor는 Spring MVC 수준에서 DispatcherServlet 이후에 동작하며 컨트롤러 호출 전후(preHandle, postHandle, afterCompletion)를 가로채고, HttpServletRequest·Response, 컨트롤러 객체, ModelAndView, Exception을 받을 수 있다. AOP는 스프링의 프록시 기반으로 동작하며 메서드 호출 자체를 가로챈다.
② 적합한 상황: Filter는 인코딩 처리나 보안 검사처럼 웹 요청 자체를 막거나 변형하고 싶을 때 쓴다. Interceptor는 로그인 여부 확인, 권한 체크, 성능 측정처럼 컨트롤러로 가기 전에 검사하거나 컨트롤러에 부가 작업이 필요할 때 쓴다. AOP는 로깅·트랜잭션처럼 Service, DAO 같은 비즈니스 로직에 공통 부가 기능을 분리해 붙이고 싶을 때 쓴다.

해설: 세 가지의 동작 계층(WAS / Spring MVC / 프록시·메서드)과 대표 용도를 각각 하나 이상 쓰면 된다.

### 32.

**모범답안:** 첫째, query string은 URL 뒤에 파라미터를 붙여 전달하는 방법으로 간단하지만 URL이 지저분해지고 값이 노출되며 문자열만 보낼 수 있다. RedirectAttributes의 일반 속성도 이 방식으로 전달된다. 둘째, session에 저장하는 방법은 객체도 전달할 수 있지만, 단발성 데이터라면 사용 후 직접 지워야 하는 관리 부담이 있다. 셋째, Flash Scope는 RedirectAttributes의 addFlashAttribute로 저장하며 redirect가 완료될 때까지만 유지되는 일회성 스코프라, 한 번 사용된 뒤 자동으로 사라져 URL이 깔끔하고 별도 삭제가 필요 없다. 범위는 request < flash < session이다.

해설: 세 방법 각각의 전달 방식과 단점(URL 노출·문자열 제한 / 수동 삭제 부담 / 일회성 자동 삭제)을 비교하면 된다.

## 시험 직전 핵심 요약

- Spring 주요 특징: POJO 기반의 DI, AOP, PSA / Spring Boot는 설정 자동화 템플릿
- Slf4j는 로깅 Facade, 구현체는 Logback·Log4j, 레벨은 trace < debug < info < warn < error
- F.I.R.S.T: Fast, Independent, Repeatable, Self-Validating, Timely / Given-When-Then
- @BeforeAll, @AfterAll은 static / @SpringBootTest는 통합 테스트
- @Configuration + @Bean = 명시적 DI, @Component + @ComponentScan + @Autowired = 묵시적 DI
- 클래스 레벨 @RequestMapping은 경로 prefix
- @ModelAttribute: 기본 생성자 → setter → Model에 카멜 케이스 이름으로 추가
- Flash Scope: redirect 완료 시까지 유지, request < flash < session
- MyBatis: namespace는 인터페이스 전체 이름, id는 메서드 이름, #{}는 값 바인딩
- 동적 SQL: if, choose(하나만), where·trim, foreach(IN 절), set(마지막 쉼표 제거), sql·include
- 부등호는 CDATA 또는 &lt; 치환
- Interceptor 여러 개: preHandle은 등록 순, postHandle·afterCompletion은 역순
- 요청 흐름: Filter → DispatcherServlet → HandlerMapping → Interceptor → Controller → ViewResolver → View
