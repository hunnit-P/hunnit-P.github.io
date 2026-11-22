# PART 1. 객관식 21문제

## A. Spring 핵심 원리와 IoC/DI 컨테이너

### 1.

프레임워크와 라이브러리의 차이에 대한 설명으로 가장 적절한 것은?

① 라이브러리는 프레임워크가 정한 실행 흐름 안에서 개발자 코드를 호출한다.
② 프레임워크는 실행 흐름을 제어하고 개발자 코드를 필요 시점에 호출한다.
③ 프레임워크를 쓰면 개발자가 main에서 모든 객체 생성 순서를 직접 정한다.
④ 라이브러리와 프레임워크는 제어권 측면의 차이가 없고 규모만 다르다.

### 2.

Spring의 3대 핵심 특징에 대한 설명으로 옳지 않은 것은?

① IoC/DI: 객체 생성과 의존관계 연결을 개발자 대신 컨테이너가 관리한다.
② AOP: 로깅·트랜잭션 같은 공통 관심사를 핵심 로직에서 분리해 모듈화한다.
③ PSA: 하부 기술이 바뀌어도 일관된 추상화 API로 같은 방식의 코드를 쓴다.
④ 세 특징 모두 객체가 특정 기술 클래스를 상속하도록 강제하는 방식이다.

### 3.

POJO(Plain Old Java Object)에 대한 설명으로 가장 적절한 것은?

① 특정 환경이나 기술에 종속되지 않은 순수한 자바 객체를 말한다.
② HttpServlet을 상속해 웹 요청을 직접 처리하는 객체를 말한다.
③ 스프링 인터페이스를 구현해야만 컨테이너가 관리할 수 있는 객체이다.
④ 상태를 가질 수 없도록 설계된 불변 객체만을 한정해서 부르는 말이다.

### 4. ★★

다음 설정 클래스로 스프링 컨테이너를 생성했을 때 "call memberRepository"가 출력되는 횟수와 그 이유로 옳은 것은?

@Configuration
public class AppConfig {
    @Bean
    public MemberRepository memberRepository() {
        System.out.println("call memberRepository");
        return new MemoryMemberRepository();
    }
    @Bean
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }
    @Bean
    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository());
    }
}

① 3번, @Bean 메서드를 자바 코드로 호출할 때마다 새 객체를 만들기 때문이다.
② 2번, 다른 @Bean 메서드에서 호출한 횟수만큼만 실행되기 때문이다.
③ 1번, CGLIB 프록시가 이미 등록된 빈을 컨테이너에서 꺼내 주기 때문이다.
④ 0번, @Bean 메서드는 첫 getBean() 호출 시점까지 실행이 미뤄지기 때문이다.

### 5.

싱글톤 스프링 빈의 생명주기 순서로 옳은 것은? (단, 의존관계는 수정자 주입이며 초기화 콜백은 @PostConstruct, 소멸 전 콜백은 @PreDestroy로 지정했다.)

① 빈 생성 → 초기화 콜백 → 의존관계 주입 → 사용 → 소멸 전 콜백 → 종료
② 빈 생성 → 의존관계 주입 → 초기화 콜백 → 사용 → 소멸 전 콜백 → 종료
③ 의존관계 주입 → 빈 생성 → 사용 → 초기화 콜백 → 소멸 전 콜백 → 종료
④ 빈 생성 → 의존관계 주입 → 사용 → 소멸 전 콜백 → 초기화 콜백 → 종료

### 6. ★★

다음 코드의 실행 결과로 옳은 것은?

@Scope("prototype")
@Component
public class PrototypeBean {
    @PostConstruct public void init() { System.out.println("init"); }
    @PreDestroy public void destroy() { System.out.println("destroy"); }
}

AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
PrototypeBean b1 = ac.getBean(PrototypeBean.class);
PrototypeBean b2 = ac.getBean(PrototypeBean.class);
ac.close();

① b1 != b2이고, init은 두 번 호출되지만 destroy는 호출되지 않는다.
② b1 == b2이고, init과 destroy가 각각 한 번씩만 호출된다.
③ b1 != b2이고, init과 destroy가 각각 두 번씩 호출된다.
④ b1 == b2이고, 컨테이너 생성 시점에 init이 한 번만 호출된다.

### 7. ★★

다음과 같이 같은 타입의 빈이 두 개 등록된 상태에서 OrderServiceImpl을 생성할 때 일어나는 일로 옳은 것은?

@Component public class FixDiscountPolicy implements DiscountPolicy { }
@Component public class RateDiscountPolicy implements DiscountPolicy { }

@Component
public class OrderServiceImpl implements OrderService {
    private final DiscountPolicy discountPolicy;
    public OrderServiceImpl(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
}

① 클래스 이름의 알파벳 순서에 따라 FixDiscountPolicy가 자동 주입된다.
② 두 빈이 리스트로 묶여 discountPolicy 파라미터에 함께 주입된다.
③ 마지막에 스캔된 빈이 앞의 빈을 덮어써서 하나만 남은 채 주입된다.
④ NoUniqueBeanDefinitionException이 발생하며 @Qualifier로 해결한다.

## B. Spring Boot, 로깅, 테스트

### 8.

@SpringBootApplication에 대한 설명으로 가장 적절한 것은?

① 이 어노테이션이 붙은 클래스의 상위 패키지 전체를 기본 스캔 범위로 삼는다.
② 자동 구성은 @EnableWebMvc가 담당하며 @SpringBootApplication과 무관하다.
③ @SpringBootConfiguration·@EnableAutoConfiguration·@ComponentScan을 포함한다.
④ 내장 톰캣을 쓰려면 web.xml에 DispatcherServlet을 반드시 직접 등록해야 한다.

### 9. ★

다음 설정과 클래스가 있을 때 외부 설정 바인딩 결과로 옳은 것은?

application.properties
app.mail.host=smtp.ssafy.com
app.mail.retry-count=3

@Component
@ConfigurationProperties(prefix = "app.mail")
public class MailProperties {
    private String host;
    private int retryCount;
    // getter, setter 생략
}

① 완화된 바인딩 규칙에 따라 retry-count 값 3이 retryCount 필드에 바인딩된다.
② 키와 필드명이 하이픈까지 완전히 같아야 하므로 retryCount는 0으로 남는다.
③ prefix를 지정하면 app.mail 하위 값은 @Value로만 읽을 수 있게 제한된다.
④ properties 파일은 바인딩 대상이 아니므로 yml로 바꿔야 값이 주입된다.

### 10. ★★

SLF4J(인터페이스)와 Logback(구현체)을 사용하는 프로젝트의 설정이 다음과 같다. com.ssafy.service.MemberService에서 아래 다섯 줄을 실행했을 때 출력되는 로그로 옳은 것은?

logging.level.root=WARN
logging.level.com.ssafy=DEBUG

log.trace("trace log");
log.debug("debug log");
log.info("info log");
log.warn("warn log");
log.error("error log");

① root 레벨이 우선하므로 WARN, ERROR 두 개만 출력된다.
② 패키지 레벨이 지정되면 TRACE를 포함한 다섯 개 모두 출력된다.
③ 지정한 레벨과 정확히 일치하는 DEBUG 한 개만 출력된다.
④ TRACE를 제외한 DEBUG, INFO, WARN, ERROR 네 개가 출력된다.

### 11. ★

JUnit 5에서 다음 테스트 클래스를 실행했을 때 출력 순서로 옳은 것은? (단, test1 → test2 순서로 실행된다고 가정한다.)

class LifecycleTest {
    @BeforeAll static void beforeAll() { System.out.print("start "); }
    @BeforeEach void beforeEach() { System.out.print("setup "); }
    @Test void test1() { System.out.print("test1 "); }
    @Test void test2() { System.out.print("test2 "); }
    @AfterEach void afterEach() { System.out.print("clean "); }
    @AfterAll static void afterAll() { System.out.print("end "); }
}

① start setup test1 test2 clean end
② start setup test1 clean setup test2 clean end
③ setup start test1 clean setup start test2 clean end
④ start setup test1 clean test2 clean end

## C. Spring AOP와 트랜잭션

### 12.

AOP 핵심 용어에 대한 설명으로 가장 적절한 것은?

① Target은 Advice를 적용할 지점을 골라내는 표현식이다.
② Join Point는 Advice와 Pointcut을 하나로 묶은 모듈이다.
③ Proxy는 Target을 감싸 호출을 가로채고 Advice를 적용한다.
④ Pointcut은 부가기능이 적용되는 핵심 비즈니스 객체 자체이다.

### 13. ★★

다음 포인트컷 표현식에 매칭되는 메서드로 옳은 것은?

execution(* com.ssafy.service..*Service.find*(..))

① com.ssafy.service.member.MemberService.findById(Long id)
② com.ssafy.service.MemberServiceImpl.findAll()
③ com.ssafy.repository.MemberService.findById(Long id)
④ com.ssafy.service.OrderService.saveOrder(Order order)

### 14.

Advice 종류와 실행 제어에 대한 설명으로 가장 적절한 것은?

① @AfterReturning은 대상 메서드에서 예외가 발생해도 항상 실행된다.
② @After는 정상 반환 시에만 실행되며 반환값을 다른 값으로 바꿀 수 있다.
③ @Before는 JoinPoint의 proceed()를 호출해야 대상 메서드가 실행된다.
④ @Around에서 proceed()를 호출하지 않으면 대상 메서드가 실행되지 않는다.

### 15. ★★

다음 메서드에서 orderRepository.save()가 성공한 뒤 IOException이 발생했다. 트랜잭션 처리 결과로 옳은 것은?

@Transactional
public void order(Order order) throws IOException {
    orderRepository.save(order);
    if (paymentFailed) {
        throw new IOException("결제 연동 실패");
    }
}

① 예외가 발생했으므로 롤백되지만 예외는 호출자에게 전달되지 않는다.
② 모든 예외에서 롤백되므로 save된 주문 데이터는 저장되지 않는다.
③ 체크 예외는 기본적으로 커밋되므로 롤백하려면 rollbackFor가 필요하다.
④ IOException은 Error 계열이므로 트랜잭션이 즉시 롤백 처리된다.

## D. Spring MVC와 웹 계층

### 16.

DispatcherServlet 기반 요청 처리 과정을 순서대로 나열한 것은?

가. ViewResolver가 논리 뷰 이름으로 실제 View 객체를 찾는다.
나. HandlerMapping에서 요청 URL을 처리할 핸들러를 조회한다.
다. HandlerAdapter를 통해 컨트롤러 메서드를 실행한다.
라. View가 모델 데이터를 사용해 응답을 렌더링한다.
마. 컨트롤러가 ModelAndView 또는 논리 뷰 이름을 반환한다.

① 다 → 나 → 마 → 가 → 라
② 나 → 다 → 마 → 가 → 라
③ 나 → 가 → 다 → 마 → 라
④ 나 → 다 → 가 → 마 → 라

### 17. ★

다음 요청이 아래 핸들러로 들어왔을 때 바인딩 결과로 옳은 것은?

POST /members/7/posts?notify=true
Content-Type: application/json
{"title": "hello"}

@PostMapping("/members/{memberId}/posts")
public ResponseEntity<Void> write(@PathVariable Long memberId, @RequestParam boolean notify, @RequestBody PostDto dto)

① memberId는 7, notify는 true, dto는 메시지 컨버터가 JSON을 변환해 채운다.
② memberId는 쿼리 스트링에서, notify는 URL 경로에서 값을 꺼내 바인딩한다.
③ @RequestBody는 폼 파라미터를 setter로 하나씩 넣는 @ModelAttribute와 같다.
④ @RequestParam은 기본이 required=false라 notify가 없으면 null로 처리된다.

### 18. ★

다음 컨트롤러 메서드가 실행된 뒤의 동작으로 옳은 것은?

@PostMapping("/members")
public String join(MemberForm form) {
    memberService.join(form);
    return "redirect:/members";
}

① 서버 내부에서 forward되어 브라우저 주소창은 POST 요청 주소 그대로 유지된다.
② 서버가 GET /members 컨트롤러를 직접 호출하므로 같은 요청 객체가 공유된다.
③ redirect:/members는 뷰 이름이므로 ViewResolver가 members.jsp를 렌더링한다.
④ 302 응답과 Location 헤더를 받은 브라우저가 GET /members로 새 요청을 보낸다.

### 19. ★★

HandlerInterceptor의 라이프사이클에 대한 설명으로 가장 적절한 것은?

① preHandle이 false를 반환해도 컨트롤러는 실행되고 postHandle만 생략된다.
② postHandle은 컨트롤러에서 예외가 발생해도 항상 호출되어 모델을 수정한다.
③ afterCompletion은 preHandle 통과 후 예외 여부와 관계없이 마지막에 호출된다.
④ 인터셉터는 DispatcherServlet보다 먼저 실행되어 서블릿 요청 자체를 차단한다.

## E. MyBatis 연동과 동적 SQL

### 20. ★★

다음 매퍼 XML에 name=null, minAge=20을 전달했을 때 실행되는 SQL로 옳은 것은?

<select id="search" resultType="Member">
    SELECT * FROM member
    <where>
        <if test="name != null">AND name = #{name}</if>
        <if test="minAge != null">AND age >= #{minAge}</if>
    </where>
</select>

① SELECT * FROM member WHERE AND age >= ?
② SELECT * FROM member WHERE age >= ?
③ SELECT * FROM member WHERE name = ? AND age >= ?
④ SELECT * FROM member

## F. Spring Security 기초

### 21. ★★

다음 SecurityFilterChain 설정에서 ROLE_USER 권한만 가진 사용자가 로그인한 상태일 때의 설명으로 옳은 것은?

http.authorizeHttpRequests(auth -> auth
    .requestMatchers("/", "/login").permitAll()
    .requestMatchers("/admin/**").hasRole("ADMIN")
    .anyRequest().authenticated());

① /admin/users에 접근하면 인증은 되었지만 인가에 실패해 403 응답을 받는다.
② hasRole("ADMIN")은 권한 문자열이 ADMIN과 정확히 같은지만 비교한다.
③ 로그인하지 않은 사용자도 anyRequest() 규칙으로 /mypage에 접근할 수 있다.
④ 규칙은 아래에서 위로 평가되므로 anyRequest()가 가장 먼저 적용된다.

# PART 2. 단답형 9문제

## G. 핵심 개념 단답형

### 22.

MyBatis에서 매퍼 인터페이스마다 @Mapper를 붙이지 않고, 설정 클래스에 지정한 패키지의 매퍼 인터페이스를 한꺼번에 스캔해 빈으로 등록하는 어노테이션을 쓰시오.

### 23. ★

회원 1명이 여러 게시글을 가지는 1:N 관계를 resultMap으로 매핑하려 한다. 빈칸 ㉠에 들어갈 태그 이름을 쓰시오.

<resultMap id="memberWithPosts" type="Member">
    <id property="id" column="member_id"/>
    <result property="name" column="name"/>
    <㉠ property="posts" ofType="Post">
        <id property="id" column="post_id"/>
        <result property="title" column="title"/>
    </㉠>
</resultMap>

### 24. ★★

다음 매퍼에 name="kim", email=null, id=1을 전달했을 때 실제 실행되는 SQL을 쓰시오. (바인딩 값은 ?로 표기)

<update id="update">
    UPDATE member
    <set>
        <if test="name != null">name = #{name},</if>
        <if test="email != null">email = #{email},</if>
    </set>
    WHERE id = #{id}
</update>

### 25.

Spring Security에서 비밀번호를 단방향 해시로 암호화하는 표준 인터페이스 이름과, encode() 외에 입력 비밀번호와 저장된 해시를 비교할 때 쓰는 메서드 이름을 쓰시오.

### 26. ★

다음 빈칸 ㉠, ㉡, ㉢에 들어갈 용어를 쓰시오.

사용자가 누구인지 확인하는 과정을 ㉠, 확인된 사용자가 특정 자원에 접근할 권한이 있는지 판단하는 과정을 ㉡ 라고 한다. Spring Security는 DispatcherServlet 앞단의 서블릿 ㉢ 체인 위에서 동작하며, 이 체인은 SecurityFilterChain으로 구성된다.

### 27.

SecurityFilterChain에서 hasRole("MANAGER")로 접근 권한을 설정했다. 이 URL에 접근하려면 사용자에게 실제로 부여되어 있어야 하는 권한(GrantedAuthority) 문자열을 쓰시오.

### 28.

스프링 컨테이너에 빈을 요청할 때마다 새로운 인스턴스를 생성해 반환하며, 컨테이너는 생성·의존관계 주입·초기화까지만 관여하는 빈 스코프의 이름을 쓰시오.

### 29.

의존관계 주입 방식 중, 빈을 생성하는 시점(생성자 호출)에 의존관계가 함께 주입되어 필드를 final로 선언할 수 있고 불변성과 누락 방지가 보장되어 권장되는 방식을 쓰시오.

### 30.

@Transactional을 붙인 코드는 데이터 접근 기술을 JDBC에서 JPA로 바꾸어도 수정할 필요가 없다. 이처럼 환경이나 기술 변경과 관계없이 일관된 방식으로 기술을 사용하게 해 주는 Spring의 특징을 영문 약어로 쓰시오.

# PART 3. 서술형 2문제

## H. 비교 서술형

### 31. ★★

Filter와 HandlerInterceptor를 다음 두 관점에서 비교하여 서술하시오. ① 실행 위치(동작 계층) ② 주로 처리하는 대표적인 역할 예시

### 32. ★★

@Controller와 @RestController를 다음 두 관점에서 비교하여 서술하시오. ① 주된 반환 대상(목적) ② @ResponseBody 적용 방식
