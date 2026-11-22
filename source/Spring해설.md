# PART 1. 객관식 정답 + 선지별 해설

## A. Spring 핵심 원리와 IoC/DI 컨테이너

### 1. ②

① 오답. 라이브러리는 개발자 코드가 필요할 때 호출하는 도구이며, 실행 흐름의 주도권은 개발자에게 있다.
② 정답. 프레임워크는 전체 실행 흐름(제어권)을 쥐고 개발자가 작성한 코드를 정해진 시점에 호출한다. 이것이 제어의 역전(IoC)이다.
③ 오답. 프레임워크를 쓰면 객체 생성과 호출 순서를 프레임워크가 관리하므로 개발자가 모든 순서를 직접 정하지 않는다.
④ 오답. 핵심 차이는 규모가 아니라 제어 흐름을 누가 가지느냐이다.

### 2. ④

① 오답(옳은 설명). IoC/DI는 객체 생성과 의존관계 연결을 컨테이너가 대신 수행하는 것이다.
② 오답(옳은 설명). AOP는 여러 곳에 흩어지는 공통 관심사를 Aspect로 분리한다.
③ 오답(옳은 설명). PSA는 트랜잭션·캐시 등에서 기술이 바뀌어도 같은 추상화 API를 쓰게 한다.
④ 정답(옳지 않은 설명). Spring의 세 특징은 모두 POJO를 기반으로 하며, 특정 기술 클래스 상속을 강제하지 않는 것이 핵심이다.

### 3. ①

① 정답. POJO는 특정 프레임워크나 기술에 종속되지 않은 순수한 자바 객체이다.
② 오답. HttpServlet을 상속하는 객체는 서블릿 기술에 종속되므로 POJO와 반대 개념이다.
③ 오답. 스프링은 특정 인터페이스 구현 없이 일반 자바 객체를 빈으로 관리할 수 있다.
④ 오답. 상태 유무나 불변 여부는 POJO의 정의 조건이 아니다.

### 4. ③

① 오답. 순수 자바 코드라면 3번 호출되겠지만, @Configuration 클래스는 CGLIB 프록시로 등록되어 그렇게 동작하지 않는다.
② 오답. 직접 호출 횟수와 관계없이 컨테이너가 싱글톤을 보장한다.
③ 정답. @Configuration이 붙으면 스프링이 CGLIB으로 AppConfig를 상속한 프록시를 빈으로 등록한다. 이 프록시는 이미 컨테이너에 memberRepository 빈이 있으면 그것을 반환하므로 메서드 본문은 1번만 실행되고 싱글톤이 보장된다.
④ 오답. 싱글톤 빈은 기본적으로 컨테이너 생성 시점에 즉시 생성된다. 참고로 @Configuration 없이 @Bean만 쓰면 3번 호출되어 싱글톤이 깨진다.

### 5. ②

① 오답. 초기화 콜백은 의존관계 주입이 끝난 뒤 호출되어야 주입된 객체를 사용할 수 있다.
② 정답. 스프링 컨테이너 생성 → 빈 생성 → 의존관계 주입 → 초기화 콜백(@PostConstruct) → 사용 → 소멸 전 콜백(@PreDestroy) → 스프링 종료 순서이다.
③ 오답. 객체가 먼저 만들어져야 수정자 주입을 할 수 있다. 생성자 주입이라면 생성과 주입이 동시에 일어난다.
④ 오답. 초기화 콜백은 사용 전에, 소멸 전 콜백은 컨테이너 종료 직전에 호출된다.

### 6. ①

① 정답. 프로토타입 빈은 getBean() 호출마다 새로 생성되고 그때마다 @PostConstruct가 호출된다. 컨테이너는 생성·주입·초기화까지만 관리하므로 ac.close() 시 @PreDestroy는 호출되지 않는다.
② 오답. 같은 인스턴스를 반환하고 종료 시 destroy가 호출되는 것은 싱글톤 빈의 동작이다.
③ 오답. 인스턴스는 서로 다르지만 소멸 콜백은 컨테이너가 호출하지 않으며, 필요하면 클라이언트가 직접 호출해야 한다.
④ 오답. 프로토타입 빈은 컨테이너 생성 시점이 아니라 요청 시점에 생성된다.

### 7. ④

① 오답. 스프링은 클래스 이름 순서로 후보를 임의 선택하지 않는다.
② 오답. List<DiscountPolicy>나 Map 타입으로 받을 때만 모든 빈이 함께 주입된다.
③ 오답. 서로 다른 빈 이름(fixDiscountPolicy, rateDiscountPolicy)으로 둘 다 등록된다.
④ 정답. 타입으로 조회한 빈이 2개라 NoUniqueBeanDefinitionException이 발생한다. 파라미터에 @Qualifier("fixDiscountPolicy")를 붙여 대상을 지정하거나, @Primary로 우선순위를 주거나, 파라미터 이름을 빈 이름과 맞춰 해결한다.

## B. Spring Boot, 로깅, 테스트

### 8. ③

① 오답. 기본 스캔 범위는 이 어노테이션이 붙은 클래스의 패키지와 그 하위 패키지이다.
② 오답. 자동 구성은 @SpringBootApplication에 포함된 @EnableAutoConfiguration이 담당한다.
③ 정답. @SpringBootApplication은 @SpringBootConfiguration(설정 클래스), @EnableAutoConfiguration(자동 구성), @ComponentScan(컴포넌트 스캔)을 합친 어노테이션이다.
④ 오답. Spring Boot는 내장 톰캣과 DispatcherServlet을 자동 구성하므로 web.xml이 필요 없다.

### 9. ①

① 정답. @ConfigurationProperties는 완화된 바인딩(relaxed binding)을 지원해 retry-count, retry_count, retryCount를 같은 필드로 바인딩한다.
② 오답. 케밥 케이스 키도 카멜 케이스 필드에 바인딩되므로 3이 들어간다.
③ 오답. prefix는 바인딩할 키의 접두사일 뿐 @Value 사용을 제한하지 않는다.
④ 오답. application.properties와 application.yml 모두 외부 설정으로 바인딩된다.

### 10. ④

① 오답. 더 구체적인 패키지 설정(com.ssafy)이 root보다 우선 적용된다.
② 오답. TRACE는 DEBUG보다 낮은 레벨이므로 출력되지 않는다.
③ 오답. 로그 레벨은 지정한 레벨 이상(같거나 더 심각한) 로그를 모두 출력한다.
④ 정답. 레벨 순서는 TRACE < DEBUG < INFO < WARN < ERROR이다. com.ssafy 하위는 DEBUG로 설정되어 DEBUG 이상인 4개가 출력된다. SLF4J는 로깅 퍼사드(인터페이스)이고 Logback이 Spring Boot 기본 구현체이다.

### 11. ②

① 오답. @BeforeEach와 @AfterEach는 테스트 메서드마다 실행된다.
② 정답. @BeforeAll은 클래스당 처음 1번, @BeforeEach와 @AfterEach는 각 테스트 전후, @AfterAll은 마지막 1번 실행된다. 기본 설정에서 @BeforeAll과 @AfterAll은 static 메서드여야 한다.
③ 오답. @BeforeAll은 테스트마다 반복되지 않고 가장 먼저 1번만 실행된다.
④ 오답. test2 전에도 @BeforeEach가 실행되어야 한다.

## C. Spring AOP와 트랜잭션

### 12. ③

① 오답. Advice를 적용할 지점을 골라내는 표현식은 Pointcut이다.
② 오답. Advice와 Pointcut을 묶은 모듈은 Aspect이다. Join Point는 Advice가 적용될 수 있는 실행 지점이며, Spring AOP에서는 메서드 실행 지점만 지원한다.
③ 정답. Proxy는 Target을 감싼 객체로, 클라이언트 호출을 가로채 Advice를 실행한 뒤 Target을 호출한다.
④ 오답. 부가기능이 적용되는 핵심 비즈니스 객체는 Target이다.

### 13. ①

① 정답. service 뒤의 ..은 하위 패키지 포함, *Service는 Service로 끝나는 타입, find*는 find로 시작하는 메서드, 괄호 안 ..은 모든 파라미터를 뜻한다. 반환 타입 *도 모두 허용한다.
② 오답. 클래스 이름이 MemberServiceImpl로 Service로 끝나지 않는다.
③ 오답. 패키지가 com.ssafy.service 하위가 아니다.
④ 오답. 메서드 이름 saveOrder가 find로 시작하지 않는다.

### 14. ④

① 오답. @AfterReturning은 정상 반환 시에만 실행되며, 예외 발생 시에는 @AfterThrowing이 실행된다.
② 오답. @After는 정상·예외와 관계없이 실행되는 finally 성격이며 반환값을 바꿀 수 없다.
③ 오답. proceed()는 @Around의 ProceedingJoinPoint에서만 호출한다. @Before는 Advice가 끝나면 대상 메서드가 자동 실행된다.
④ 정답. @Around는 대상 메서드 실행 여부, 반환값, 예외 처리까지 제어할 수 있으며 proceed()를 호출하지 않으면 대상 메서드가 실행되지 않는다.

### 15. ③

① 오답. 트랜잭션 처리와 별개로 예외는 호출자에게 그대로 전파된다.
② 오답. 기본 롤백 대상은 언체크 예외(RuntimeException)와 Error뿐이다.
③ 정답. IOException은 체크 예외이므로 기본 규칙상 커밋되어 save한 데이터가 남는다. 롤백하려면 @Transactional(rollbackFor = IOException.class)를 지정해야 한다.
④ 오답. IOException은 Exception을 상속한 체크 예외이며 Error 계열이 아니다.

## D. Spring MVC와 웹 계층

### 16. ②

① 오답. 어떤 핸들러를 실행할지 먼저 HandlerMapping으로 찾아야 한다.
② 정답. 요청 → DispatcherServlet → HandlerMapping(핸들러 조회) → HandlerAdapter(컨트롤러 실행) → ModelAndView 반환 → ViewResolver(View 탐색) → View 렌더링 → 응답 순서이다.
③ 오답. 뷰 이름은 컨트롤러 실행 후에 결정되므로 ViewResolver가 먼저 동작할 수 없다.
④ 오답. 컨트롤러가 논리 뷰 이름을 반환해야 ViewResolver가 View를 찾을 수 있다.

### 17. ①

① 정답. @PathVariable은 URL 경로 변수(값 7), @RequestParam은 쿼리 스트링이나 폼 파라미터(값 true), @RequestBody는 HTTP 본문 JSON을 HttpMessageConverter(Jackson)가 객체로 변환해 바인딩한다.
② 오답. 경로 변수와 쿼리 파라미터의 위치를 바꾸어 설명했다.
③ 오답. @ModelAttribute는 요청 파라미터를 객체에 바인딩하고, @RequestBody는 요청 본문을 메시지 컨버터로 읽는다.
④ 오답. @RequestParam의 required 기본값은 true이므로 파라미터가 없으면 400 오류가 발생한다.

### 18. ④

① 오답. 이는 forward의 동작이다. redirect는 브라우저 주소창이 /members로 바뀐다.
② 오답. redirect는 새로운 HTTP 요청이므로 이전 요청의 request 속성은 공유되지 않는다.
③ 오답. redirect: 접두사가 붙으면 ViewResolver가 JSP를 렌더링하지 않고 RedirectView로 처리한다.
④ 정답. 서버는 302 상태 코드와 Location 헤더를 응답하고, 브라우저가 해당 주소로 GET 요청을 다시 보낸다. POST 후 redirect로 새로고침 시 중복 제출을 막는 패턴이 PRG(Post-Redirect-Get)이다.

### 19. ③

① 오답. preHandle이 false를 반환하면 이후 인터셉터와 컨트롤러가 실행되지 않는다.
② 오답. postHandle은 컨트롤러가 정상 처리된 뒤 뷰 렌더링 전에만 호출되며, 예외가 나면 호출되지 않는다.
③ 정답. afterCompletion은 preHandle이 true를 반환한 경우 뷰 렌더링 후 예외 발생 여부와 관계없이 호출되며, 예외 정보를 파라미터로 받을 수 있다.
④ 오답. DispatcherServlet보다 먼저 실행되는 것은 Filter이다. 흐름은 Filter → DispatcherServlet → Interceptor → (AOP 프록시) → Controller이다.

## E. MyBatis 연동과 동적 SQL

### 20. ②

① 오답. where 태그는 내부 내용의 맨 앞에 오는 AND나 OR를 자동으로 제거한다.
② 정답. name이 null이라 첫 if는 제외되고, 두 번째 조건만 남는다. where 태그가 WHERE를 붙이고 앞의 AND를 지운다.
③ 오답. name이 null이므로 name 조건은 포함되지 않는다.
④ 오답. 내부에 남는 조건이 하나라도 있으면 WHERE 절이 생성된다. 조건이 모두 없을 때만 WHERE가 생략된다.

## F. Spring Security 기초

### 21. ①

① 정답. 로그인했으므로 인증은 성공했지만 ROLE_ADMIN 권한이 없어 인가 실패(403 Forbidden)가 된다. 인증 자체가 안 된 경우는 401 또는 로그인 페이지로 이동한다.
② 오답. hasRole("ADMIN")은 자동으로 ROLE_ 접두사를 붙여 ROLE_ADMIN 권한을 검사한다. 접두사 없이 비교하려면 hasAuthority를 쓴다.
③ 오답. anyRequest().authenticated()는 인증된 사용자만 접근하도록 한다.
④ 오답. 규칙은 위에서 아래로 평가되어 처음 일치한 규칙이 적용되므로, 구체적인 경로를 먼저 쓰고 anyRequest()는 마지막에 둔다.

# PART 2. 단답형 정답 및 해설

## G. 핵심 개념 단답형

### 22.

**정답: @MapperScan**

해설: @MapperScan("com.ssafy.mapper")처럼 패키지를 지정하면 하위 매퍼 인터페이스가 모두 빈으로 등록된다. 인터페이스마다 @Mapper를 붙이는 방식도 있다. 구현 클래스는 MyBatis가 프록시로 만들어 주며, XML의 namespace는 인터페이스의 전체 이름, SQL id는 메서드 이름과 일치해야 한다.

### 23.

**정답: collection**

해설: 1:N 관계의 컬렉션 필드(List<Post>)는 collection 태그로 매핑하고, 요소 타입은 ofType으로 지정한다. 1:1 관계는 association 태그와 javaType을 사용한다.

### 24.

**정답: UPDATE member SET name = ? WHERE id = ?**

해설: email이 null이라 두 번째 if는 제외된다. set 태그는 SET 키워드를 붙이고 마지막에 남은 쉼표를 자동으로 제거한다. #{}는 PreparedStatement의 ?로 바인딩되어 SQL Injection을 방지한다.

### 25.

**정답: PasswordEncoder, matches()**

해설: PasswordEncoder는 encode()로 단방향 해시를 만들고 matches(rawPassword, encodedPassword)로 일치 여부를 확인한다. 해시는 복호화할 수 없으므로 비교할 때 다시 인코딩해 검증한다. 대표 구현체는 솔트를 포함하는 BCryptPasswordEncoder이다.

### 26.

**정답: ㉠ 인증(Authentication), ㉡ 인가(Authorization), ㉢ 필터(Filter)**

해설: 인증은 "누구인가", 인가는 "무엇을 할 수 있는가"를 확인한다. Spring Security는 DelegatingFilterProxy → FilterChainProxy → SecurityFilterChain 구조로 서블릿 필터 단계에서 동작하며, 인증 정보는 SecurityContextHolder에 저장된다.

### 27.

**정답: ROLE_MANAGER**

해설: hasRole은 전달한 역할 이름 앞에 ROLE_ 접두사를 자동으로 붙여 검사한다. hasRole에 "ROLE_MANAGER"를 직접 넣으면 오류가 나며, 접두사 없이 그대로 비교하려면 hasAuthority를 사용한다.

### 28.

**정답: prototype (프로토타입 스코프)**

해설: @Scope("prototype")로 지정한다. 기본 스코프인 singleton은 컨테이너 시작부터 종료까지 1개 인스턴스를 유지하지만, prototype은 요청마다 새 인스턴스를 만들고 이후 관리는 클라이언트에 맡기므로 @PreDestroy가 호출되지 않는다.

### 29.

**정답: 생성자 주입**

해설: 생성자 주입은 빈 생성과 동시에 한 번만 주입되어 불변을 보장하고, final 필드로 주입 누락을 컴파일 시점에 잡을 수 있다. 생성자가 하나면 @Autowired를 생략할 수 있다. 수정자 주입과 필드 주입은 빈 생성 이후에 의존관계가 주입된다.

### 30.

**정답: PSA (Portable Service Abstraction, 서비스 추상화)**

해설: @Transactional은 PlatformTransactionManager라는 추상화를 사용하므로 JDBC(DataSourceTransactionManager)에서 JPA(JpaTransactionManager)로 바꿔도 비즈니스 코드는 그대로이다.

# PART 3. 서술형 모범답안 및 해설

## H. 비교 서술형

### 31.

**모범답안:**
① 실행 위치: Filter는 서블릿 스펙에 속해 서블릿 컨테이너(WAS) 레벨에서 DispatcherServlet에 요청이 도달하기 전과 응답이 나간 후에 동작한다. HandlerInterceptor는 Spring MVC에 속해 DispatcherServlet 이후, 컨트롤러 호출 전(preHandle)·후(postHandle)와 뷰 렌더링 완료 후(afterCompletion)에 동작한다. 요청 흐름은 Filter → DispatcherServlet → Interceptor → Controller 순서이다.
② 대표 역할: Filter는 스프링과 무관하게 모든 요청에 적용할 문자 인코딩 설정, CORS 처리, XSS 방어, 요청·응답 로깅, Spring Security 인증 처리 등에 쓰인다. Interceptor는 핸들러 정보와 스프링 빈을 활용할 수 있어 로그인 여부(세션) 확인, 권한 체크, 공통 모델 데이터 추가, 컨트롤러 실행 시간 측정 등에 쓰인다.

해설: "Filter는 서블릿 컨테이너 레벨에서 DispatcherServlet 앞, Interceptor는 스프링 MVC 레벨에서 DispatcherServlet과 컨트롤러 사이"라는 위치 차이와 각각의 대표 예시를 하나 이상 쓰면 된다. 참고로 AOP는 컨트롤러뿐 아니라 서비스 등 스프링 빈의 메서드 단위로 적용된다.

### 32.

**모범답안:**
① 주된 반환 대상: @Controller는 주로 뷰(View)를 반환하는 컨트롤러로, 메서드가 반환한 문자열을 논리 뷰 이름으로 보고 ViewResolver가 JSP·Thymeleaf 같은 화면을 찾아 HTML을 렌더링한다. @RestController는 REST API용 컨트롤러로, 반환 객체(데이터)를 JSON이나 문자열 형태로 HTTP 응답 본문에 직접 담는다.
② @ResponseBody 적용 방식: @Controller에서 데이터를 반환하려면 해당 메서드마다 @ResponseBody를 직접 붙여야 한다. @RestController는 @Controller와 @ResponseBody를 합친 어노테이션이라 클래스 레벨에서 모든 메서드에 @ResponseBody가 자동 적용되며, 반환값은 ViewResolver 대신 HttpMessageConverter를 거쳐 응답 본문에 작성된다.

해설: "@Controller는 뷰 반환, @RestController는 데이터(JSON) 반환"과 "@RestController = @Controller + @ResponseBody로 모든 메서드에 자동 적용"이라는 두 포인트가 들어가면 된다.

## 시험 직전 핵심 요약

- 프레임워크는 제어 흐름을 쥐고 내 코드를 호출하고(IoC), 라이브러리는 내 코드가 호출한다.
- Spring 3대 특징: IoC/DI, AOP, PSA (모두 POJO 기반)
- @Configuration + @Bean → CGLIB 프록시로 싱글톤 보장
- 생명주기: 생성 → 의존관계 주입 → @PostConstruct → 사용 → @PreDestroy → 종료 / prototype은 @PreDestroy가 호출되지 않음
- 같은 타입 빈 2개 → NoUniqueBeanDefinitionException → @Qualifier / @Primary
- @SpringBootApplication = @SpringBootConfiguration + @EnableAutoConfiguration + @ComponentScan
- 로그 레벨: TRACE < DEBUG < INFO < WARN < ERROR (설정 레벨 이상 출력)
- JUnit 5: @BeforeAll/@AfterAll(1번, static), @BeforeEach/@AfterEach(테스트마다)
- @Transactional: 언체크 예외·Error는 롤백, 체크 예외는 커밋 (rollbackFor로 변경)
- 요청 흐름: Filter → DispatcherServlet → Interceptor → AOP → Controller
- redirect: 302 + Location → 브라우저가 새 GET 요청 (PRG 패턴)
- MyBatis: @MapperScan, where/set 태그는 앞의 AND·뒤의 쉼표 제거, 1:N은 collection
- Spring Security: 인증(Authentication)과 인가(Authorization), hasRole은 ROLE_ 자동 접두사, 비밀번호는 PasswordEncoder(BCrypt)
