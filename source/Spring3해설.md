# PART 1. 객관식 정답 + 선지별 해설

## A. Spring 주요 특징과 로깅

### 1. ③

① 오답. IoC는 DI와 관련된 개념이지만 MVC, JPA는 Spring의 주요 특징이 아니다.
② 오답. ORM은 JPA 같은 기술의 개념이며 Spring의 주요 특징에 포함되지 않는다.
③ 정답. Spring의 주요 특징은 POJO 기반의 DI, AOP, PSA이다.
④ 오답. JDBC는 데이터 접근 기술이고, POJO는 세 특징의 기반이다.

### 2. ①

① 정답. DI는 의존성을 외부에서 주입받아 사용하는 것으로, 의존성이 변해도 의존하는 객체는 변할 필요가 없어 유지보수성이 높아진다.
② 오답. 객체가 의존성을 직접 생성하는 것은 DI와 반대이며 결합도를 높인다.
③ 오답. 핵심·부가 관점으로 나누어 모듈화하는 것은 AOP이다.
④ 오답. 환경에 종속되지 않는 추상화 레이어를 제공하는 것은 PSA이다.

### 3. ④

① 오답. 공통 관심사를 Aspect로 분리하는 것은 AOP의 예이다.
② 오답. 구현체를 외부에서 주입받는 것은 DI의 예이다.
③ 오답. 평범한 자바 클래스로 작성하는 것은 POJO의 예이다.
④ 정답. 데이터 접근 기술이 JPA든 MyBatis든 트랜잭션 처리 방식이 동일한 것이 대표적인 PSA의 예이다.

### 4. ②

① 오답. info는 설정 레벨과 같으므로 출력된다.
② 정답. 레벨 순서는 trace → debug → info → warn → error이며, info로 설정하면 info 이상만 출력되어 trace와 debug는 출력되지 않는다.
③ 오답. warn과 error는 info보다 높은 레벨이므로 출력된다.
④ 오답. debug도 info보다 낮은 레벨이므로 출력되지 않는다.

## B. Bean과 DI, Spring Boot

### 5. ③

① 오답. Bean의 생성과 생명주기는 개발자가 아니라 Spring이 관리한다.
② 오답. Spring은 Bean을 기본적으로 싱글톤 형태로 관리한다.
③ 정답. Bean은 Spring Framework가 생성·관리하는 자바 객체이며, Spring은 Bean의 생명주기를 관리하므로 Bean의 Container라고 부른다.
④ 오답. Bean은 POJO로 작성하며 특정 클래스 상속이 필요 없다.

### 6. ①

① 정답. @Configuration은 Java 기반 설정 파일을 만들기 위해 클래스 레벨에, @Bean은 메서드 레벨에 선언하며 메서드 이름이 빈 이름이 된다.
② 오답. @Bean은 메서드 레벨에 선언한다.
③ 오답. @Configuration은 클래스 레벨에 선언한다. 빈 이름은 @Bean의 name 속성으로 바꿀 수 있다.
④ 오답. @Component와 @ComponentScan을 쓰는 것은 묵시적 DI이다.

### 7. ④

① 오답. 선언 순서로 자동 선택되지 않는다.
② 오답. 스캔 순서로 우선순위가 정해지지 않는다.
③ 오답. @Autowired는 타입 기반으로 주입하며 빈을 새로 생성하지 않는다.
④ 정답. 같은 타입 빈이 두 개라 타입 충돌이 발생한다. @Qualifier로 이름 조건을 추가해 주입할 빈을 한정한다.

### 8. ②

① 오답(포함됨). @SpringBootConfiguration은 설정 클래스임을 나타낸다.
② 정답(포함되지 않음). @EnableWebMvc는 @SpringBootApplication에 포함되지 않는다.
③ 오답(포함됨). @EnableAutoConfiguration은 자동 구성을 담당한다.
④ 오답(포함됨). @ComponentScan은 컴포넌트 스캔을 담당한다.

## C. Spring MVC

### 9. ③

① 오답. @RequestMapping은 클래스 레벨과 메서드 레벨 모두에 선언할 수 있다.
② 오답. @GetMapping은 method=RequestMethod.GET의 축약이다.
③ 정답. @PostMapping은 @RequestMapping의 method를 POST로 지정한 것과 같다.
④ 오답. 클래스 레벨 경로는 모든 메서드 요청 경로의 prefix가 된다.

### 10. ①

① 정답. 일반적인 형태로 뷰 이름을 전달하면 forward로 처리되고, redirect: 키워드를 붙이면 redirect로 처리되어 브라우저가 새 요청을 보낸다.
② 오답. redirect: 접두사가 있으면 redirect로 처리되어 주소창이 바뀐다.
③ 오답. 접두사 없이 뷰 이름만 반환하면 forward이다.
④ 오답. redirect: 는 redirect 처리를 지시하는 키워드이며 JSP 경로가 아니다.

### 11. ④

① 오답. addFlashAttribute로 넣은 값은 query string이 아니라 Flash Scope로 전달된다.
② 오답. session에 넣은 것처럼 계속 유지되지 않는다. Flash 값은 일회성이다.
③ 오답. addAttribute는 query string으로 전달되므로 문자열 형태의 데이터만 보낼 수 있다.
④ 정답. addAttribute는 query string으로 URL 뒤에 붙고, addFlashAttribute는 redirect가 완료될 때까지만 저장되어 한 번의 요청 후 사라진다.

### 12. ②

① 오답. 문자열을 뷰 이름으로 해석하는 것은 @ResponseBody가 없을 때의 동작이다.
② 정답. @ResponseBody를 사용하면 반환값이 JSON으로 변환되어 응답 본문으로 전달된다.
③ 오답. 요청 본문의 JSON을 DTO로 바꾸는 것은 @RequestBody이다.
④ 오답. 메서드에 붙일 수 있으며 클래스에 붙이면 모든 메서드에 적용된다.

## D. MyBatis

### 13. ③

① 오답. MyBatis는 내부적으로 PreparedStatement를 사용한다.
② 오답. 매핑 규칙을 한 번 작성하면 ResultSet을 DTO에 저장하는 코드가 필요 없다.
③ 정답. PreparedStatement를 사용하지만 파라미터를 설정하는 코드를 직접 작성할 필요가 없다.
④ 오답. 전통적으로 XML에서 SQL을 관리하며 어노테이션으로도 작성할 수 있다.

### 14. ①

① 정답. resultMap 속성은 다른 resultMap을 재사용할 때 쓰며, 다른 mapper에 있다면 namespace를 포함해 지정한다.
② 오답. 연동할 객체의 속성 이름은 property이다. column은 join 관계에서 사용된 컬럼 이름이다.
③ 오답. association은 1:1 관계에 쓰고, 1:N 관계의 List는 collection으로 매핑한다.
④ 오답. property에는 자바 객체의 속성 이름을 적는다.

### 15. ④

① 오답. 연동할 객체의 속성 이름은 property로 지정한다.
② 오답. null일 때 컬렉션에 추가하지 않게 하는 속성은 notNullColumn이다.
③ 오답. 같은 컬럼명을 구별하기 위한 접두사는 columnPrefix이다.
④ 정답. ofType은 List에 담길 N에 해당하는 객체 타입을 지정한다.

### 16. ②

① 오답. trim은 처리 후 내용이 있을 때만 prefix를 붙인다.
② 정답. 두 if가 모두 거짓이라 내용이 없으므로 where도 붙지 않는다.
③ 오답. 내용이 없으므로 AND도, where도 생성되지 않는다.
④ 오답. 1=1은 매퍼에 작성되지 않은 조건이다.

### 17. ③

① 오답. age가 null이므로 age 조건은 포함되지 않는다.
② 오답. set 태그가 맨 마지막 컬럼의 쉼표를 제거한다.
③ 정답. name과 tel만 남고, set 태그가 SET을 붙이고 마지막 쉼표를 지운다.
④ 오답. set 태그가 SET 키워드를 생성한다.

### 18. ①

① 정답. < 는 &lt;, > 는 &gt;, ≤ 는 &le;, ≥ 는 &ge;로 치환한다.
② 오답. < 와 > 의 치환 문자가 서로 바뀌었다.
③ 오답. ≤ 와 ≥ 의 치환 문자가 서로 바뀌었다.
④ 오답. CDATA 섹션 안은 XML로 해석되지 않으므로 부등호를 그대로 쓸 수 있다.

## E. 트랜잭션, AOP, Interceptor

### 19. ②

① 오답. @Transactional을 쓰면 Connection을 전달하지 않아도 된다.
② 정답. @Transactional은 DB 접근 기술과 무관한 선언적 트랜잭션 처리이며, @Service에서 사용한다.
③ 오답. Controller에는 SQLException 대신 DataAccessException이 전파된다.
④ 오답. 기술이 바뀌어도 같은 @Transactional을 사용한다(PSA).

### 20. ④

① 오답. @AfterReturning은 메서드가 성공했을 때만 실행된다.
② 오답. 예외가 발생하면 @AfterReturning은 실행되지 않는다.
③ 오답. 예외 상황에서는 @AfterReturning 대신 @AfterThrowing이 실행된다.
④ 정답. @Before는 메서드 실행 전에, @After는 결과와 상관없이, @AfterThrowing은 예외를 던졌을 때 실행된다.

### 21. ③

① 오답. preHandle은 지정된 컨트롤러 동작 이전에 가로챈다. 화면 처리 완료 시점은 afterCompletion이다.
② 오답. afterCompletion은 화면 처리가 완료된 시점에 처리된다.
③ 정답. Interceptor는 DispatcherServlet이 HandlerAdapter를 호출하기 전·후 등에 거치는 일종의 필터이다.
④ 오답. WAS 수준에서 DispatcherServlet 도달 전에 동작하는 것은 Filter이다.

# PART 2. 단답형 정답 및 해설

## F. 핵심 개념 단답형

### 22.

**정답: POJO (Plain Old Java Object)**

해설: POJO는 특정 인터페이스 구현이나 상속이 필요 없는 일반적인 자바 클래스이다. 가독성과 유지보수성이 좋고 단위 테스트가 쉽다.

### 23.

**정답: Facade 패턴 (퍼사드 패턴)**

해설: Slf4j는 Simple Logging Facade for Java의 약자로, Logback·Log4j 같은 구현체를 하나의 인터페이스로 감싸 제공한다.

### 24.

**정답: JUnit**

해설: JUnit은 Java 단위 테스트 자동화 프레임워크이며, JUnit 5에서 @BeforeAll과 @AfterAll은 반드시 static으로 선언한다.

### 25.

**정답: @Qualifier**

해설: @Qualifier는 이름 기반으로 주입될 빈을 한정하며 @Autowired와 함께 사용한다. 참고로 생성자 자체에는 붙일 수 없지만, 생성자의 파라미터에는 붙일 수 있다.

### 26.

**정답: ${} 표기**

해설: #{}는 값만 바인딩하므로 SQL 구조를 바꾸지 못하고 SQL Injection에 안전하다. 반면 이 표기는 문자열을 그대로 치환해 문장 자체를 재구성할 수 있지만 SQL Injection에 주의해야 한다.

### 27.

**정답: ㉠ when, ㉡ otherwise**

해설: choose 안의 when 중 처음으로 조건을 만족한 하나만 적용되고, 모두 거짓이면 otherwise가 적용된다.

### 28.

**정답: prefixOverrides**

해설: prefixOverrides="AND|OR"처럼 지정하면 맨 앞의 AND나 OR를 지운다. 뒤쪽 문자열을 지우는 속성은 suffixOverrides이고, 내용이 있을 때 앞뒤에 붙이는 속성은 prefix와 suffix이다.

### 29.

**정답: Join Point (조인 포인트)**

해설: advice가 동작하는 지점이며 Spring AOP에서는 메서드 실행 시점으로 제한된다. advice를 적용할 대상을 결정하는 표현식은 pointcut이다.

### 30.

**정답: @Around**

해설: @Around는 타겟 메서드를 감싸 호출 전과 후에 모두 실행되며, 메서드 실행 여부와 반환값까지 제어할 수 있다.

# PART 3. 서술형 모범답안 및 해설

## G. 개념 서술형

### 31.

**모범답안:** DI(의존성 주입)는 객체가 필요한 의존성을 직접 만들지 않고 외부에서 주입받아 사용하는 것으로, 의존성이 변하더라도 의존하는 객체는 변할 필요가 없어 유지보수성이 높아진다. AOP(관점 지향 프로그래밍)는 로직을 핵심 관점과 부가 관점으로 나누어 로깅·트랜잭션 같은 횡단 관심사를 분리·모듈화하고 필요한 곳에 적용해 핵심 로직에 집중하게 한다. PSA(이식 가능한 서비스 추상화)는 복잡한 기술을 특정 환경에 종속되지 않게 추상화된 레이어로 제공하는 것으로, JPA든 MyBatis든 @Transactional로 같은 방식의 트랜잭션을 처리하는 것이 예이다. 이 세 특징은 모두 POJO를 기반으로 하므로, 개발자는 특정 인터페이스 구현이나 상속 없이 평범한 자바 객체를 만들기만 하면 DI, AOP, PSA를 적용받을 수 있다.

해설: 세 특징의 정의와 예시, 그리고 "POJO 기반"이라는 관계를 함께 쓰면 된다.

### 32.

**모범답안:** ① 사용자 요청이 들어오면 먼저 Filter가 WAS 수준에서 요청을 가로채 처리한다. ② DispatcherServlet이 요청을 받아 스프링에 진입한다. ③ HandlerMapping이 요청을 처리할 Controller를 찾는다. ④ HandlerInterceptor의 preHandle이 Controller 호출 전에 요청을 검사·전처리한다. ⑤ Controller가 요청을 처리하며, 필요하면 Service와 DAO를 호출한다. ⑥ HandlerInterceptor가 응답을 후처리한다. ⑦ ViewResolver가 뷰 이름을 실제 View 객체로 변환한다. ⑧ View가 렌더링된다. ⑨ HTTP 응답이 사용자에게 전달된다.

해설: Filter → DispatcherServlet → HandlerMapping → HandlerInterceptor → Controller(→ Service → DAO) → HandlerInterceptor → ViewResolver → View → HTTP 응답 순서와 각 단계의 역할을 쓰면 된다.

## 시험 직전 핵심 요약

- POJO 기반의 DI, AOP, PSA
- Slf4j는 Facade 패턴, 구현체는 Logback·Log4j / trace → debug → info → warn → error
- 명시적 DI: @Configuration(클래스) + @Bean(메서드, 메서드명이 빈 이름)
- 묵시적 DI: @Component + @ComponentScan + @Autowired(타입 기반), 충돌 시 @Qualifier(이름 기반)
- @GetMapping = @RequestMapping(method=RequestMethod.GET)
- 뷰 이름만 반환하면 forward, redirect: 를 붙이면 redirect
- addAttribute는 query string(문자열만), addFlashAttribute는 일회성 Flash Scope
- association은 1:1, collection은 1:N(ofType, columnPrefix, notNullColumn)
- trim의 prefix·suffix는 붙이기, prefixOverrides·suffixOverrides는 지우기
- 부등호: &lt; &gt; &le; &ge; 또는 CDATA
- @Transactional은 @Service에서, Controller에는 DataAccessException이 전파
- 예외 발생 시 실행되는 advice: @Before, @After, @AfterThrowing
