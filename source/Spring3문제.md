# PART 1. 객관식 21문제

## A. Spring 주요 특징과 로깅

### 1.

Spring의 주요 특징을 한 줄로 표현할 때 빈칸에 들어갈 말로 옳은 것은?

POJO 기반의 ________

① IoC, MVC, JPA
② DI, ORM, PSA
③ DI, AOP, PSA
④ AOP, JDBC, POJO

### 2.

DI(Dependency Injection)에 대한 설명으로 가장 적절한 것은?

① 의존성을 외부에서 주입받아, 의존 대상이 바뀌어도 사용하는 객체는 바뀌지 않는다.
② 객체가 필요한 의존성을 new로 직접 생성해 객체 간 결합도를 높이는 방식이다.
③ 어떤 로직을 핵심 관점과 부가 관점으로 나누어 각각 모듈화하는 방식이다.
④ 복잡한 기술을 특정 환경에 종속되지 않게 추상화된 레이어로 제공한다.

### 3.

다음 중 PSA(Portable Service Abstraction)의 예로 가장 적절한 것은?

① 로깅 코드를 Aspect로 분리해 여러 서비스 메서드에 공통 적용한다.
② 생성자 파라미터로 Repository 구현체를 외부에서 주입받아 사용한다.
③ 특정 인터페이스 구현 없이 평범한 자바 클래스로 빈을 작성한다.
④ JPA든 MyBatis든 @Transactional로 같은 방식의 트랜잭션을 처리한다.

### 4. ★

로그 레벨을 info로 설정했을 때 출력되지 않는 로그 레벨만 모두 고른 것은?

① debug, info
② trace, debug
③ warn, error
④ trace

## B. Bean과 DI, Spring Boot

### 5.

Bean과 스프링 컨테이너에 대한 설명으로 가장 적절한 것은?

① Bean은 개발자가 new로 생성해 생명주기를 직접 관리하는 객체이다.
② Spring은 Bean을 기본적으로 요청마다 새로 만드는 방식으로 관리한다.
③ Bean은 Spring이 생성·관리하는 객체이며, Spring을 Bean의 Container라 한다.
④ Bean으로 등록하려면 Spring이 제공하는 클래스를 반드시 상속해야 한다.

### 6.

명시적 DI에 사용하는 어노테이션에 대한 설명으로 가장 적절한 것은?

① @Configuration은 클래스 레벨, @Bean은 메서드 레벨에 선언하며 빈 이름은 메서드명이다.
② @Bean은 클래스 레벨에 선언하며 빈 이름은 반환 타입의 클래스명이 된다.
③ @Configuration은 메서드 레벨에 선언하며 빈의 이름을 지정하는 데 쓴다.
④ 명시적 DI는 @Component와 @ComponentScan만으로 빈을 등록하는 방식이다.

### 7. ★★

다음과 같이 Washer 타입 빈이 두 개 있을 때의 설명으로 옳은 것은?

@Component public class SWasher implements Washer { }
@Component public class LWasher implements Washer { }

@Component
public class WasherUser {
    @Autowired
    private Washer washer;
}

① 먼저 선언된 SWasher 빈이 자동으로 선택되어 washer에 주입된다.
② 타입이 같으면 나중에 스캔된 LWasher가 항상 우선해서 주입된다.
③ @Autowired는 이름 기반이므로 washer라는 이름의 빈을 새로 생성한다.
④ 타입 충돌이 발생하므로 @Qualifier("sWasher")로 주입할 빈을 한정한다.

### 8.

@SpringBootApplication이 내부적으로 포함하는 어노테이션이 아닌 것은?

① @SpringBootConfiguration
② @EnableWebMvc
③ @EnableAutoConfiguration
④ @ComponentScan

## C. Spring MVC

### 9.

@RequestMapping에 대한 설명으로 가장 적절한 것은?

① @RequestMapping은 메서드 레벨에만 선언할 수 있다.
② @GetMapping은 @RequestMapping(method=RequestMethod.POST)의 축약이다.
③ @PostMapping은 @RequestMapping(method=RequestMethod.POST)의 축약이다.
④ 클래스 레벨 @RequestMapping 경로는 메서드 경로 뒤에 suffix로 붙는다.

### 10.

컨트롤러 메서드가 다음 두 값을 반환하는 경우에 대한 설명으로 옳은 것은?

return "member/list";
return "redirect:/member/list";

① "member/list"는 forward로 뷰를 찾고, "redirect:/member/list"는 브라우저가 재요청한다.
② 두 반환값 모두 forward로 처리되어 브라우저 주소창이 바뀌지 않는다.
③ "member/list"는 redirect로 처리되어 브라우저에서 새 요청이 발생한다.
④ redirect: 접두사는 ViewResolver가 JSP 경로 앞에 붙이는 문자열이다.

### 11. ★★

다음 코드 실행 후 /member/detail로 이동할 때의 설명으로 옳은 것은?

@PostMapping("/regist")
public String regist(Member member, RedirectAttributes ra) {
    ra.addAttribute("mno", 7);
    ra.addFlashAttribute("msg", "등록 완료");
    return "redirect:/member/detail";
}

① msg는 query string으로 전달되어 주소창에 msg=등록 완료가 그대로 보인다.
② mno와 msg는 모두 session에 저장되어 직접 삭제하기 전까지 유지된다.
③ addAttribute는 객체를 그대로 보관하므로 문자열이 아닌 값도 전달된다.
④ mno는 ?mno=7로 URL에 붙고, msg는 redirect 후 한 번 쓰이고 사라진다.

### 12.

@ResponseBody에 대한 설명으로 가장 적절한 것은?

① 반환 문자열을 뷰 이름으로 해석해 ViewResolver가 JSP를 찾게 한다.
② 반환 객체를 JSON으로 변환해 HTTP 응답 본문에 담아 반환한다.
③ 요청 본문의 JSON을 DTO로 변환할 때 메서드 매개변수에 붙인다.
④ 클래스에만 붙일 수 있고 개별 메서드에는 붙일 수 없는 어노테이션이다.

## D. MyBatis

### 13.

MyBatis에 대한 설명으로 가장 적절한 것은?

① 내부적으로 Statement만 사용해 매번 SQL 문자열을 직접 이어 붙인다.
② ResultSet 내용을 DTO로 옮기는 코드를 매번 직접 작성해야 한다.
③ 내부적으로 PreparedStatement를 쓰지만 파라미터 설정 코드가 필요 없다.
④ SQL은 반드시 자바 코드 안에 문자열로만 작성해야 실행할 수 있다.

### 14. ★

다음 resultMap에 대한 설명으로 옳은 것은?

<resultMap type="Address" id="addressMap">
    <id column="ano" property="ano"/>
    <association property="member" column="mno" resultMap="com.ssafy.live.model.dao.MemberDao.memberMap"/>
    <result column="detail_address" property="detailAddress"/>
</resultMap>

① 다른 mapper의 resultMap을 재사용하므로 resultMap 값에 namespace를 포함했다.
② column 속성은 Address 객체에서 회원 정보를 담을 자바 속성 이름이다.
③ association은 1:N 관계에서 List 컬렉션을 매핑할 때 사용하는 태그이다.
④ property 속성에는 join 관계에서 사용된 DB 컬럼 이름을 그대로 적는다.

### 15.

collection 태그의 속성에 대한 설명으로 가장 적절한 것은?

① ofType은 연동할 객체의 속성 이름을 지정하는 속성이다.
② columnPrefix는 값이 null이면 컬렉션에 추가하지 않게 한다.
③ notNullColumn은 같은 컬럼명을 구별하기 위한 접두사이다.
④ ofType은 List에 담길 N에 해당하는 객체 타입을 지정한다.

### 16. ★★

다음 매퍼에 name=null, age=null을 전달했을 때 실행되는 SQL로 옳은 것은?

<select id="search" resultType="User">
    SELECT * FROM user
    <trim prefix="where" prefixOverrides="AND|OR">
        <if test="name != null">AND name = #{name}</if>
        <if test="age != null">AND age = #{age}</if>
    </trim>
</select>

① SELECT * FROM user where
② SELECT * FROM user
③ SELECT * FROM user where AND
④ SELECT * FROM user where 1=1

### 17. ★★

다음 매퍼에 name="kim", age=null, tel="010", id=1을 전달했을 때 실행되는 SQL로 옳은 것은?

<update id="update">
    update user
    <set>
        <if test="name != null">name=#{name},</if>
        <if test="age != null">age=#{age},</if>
        <if test="tel != null">tel=#{tel},</if>
    </set>
    WHERE id=#{id}
</update>

① update user SET name=?, age=?, tel=? WHERE id=?
② update user SET name=?, tel=?, WHERE id=?
③ update user SET name=?, tel=? WHERE id=?
④ update user name=?, tel=? WHERE id=?

### 18.

MyBatis XML에서 부등호를 처리하는 방법에 대한 설명으로 옳은 것은?

① < 는 &lt;, ≥ 는 &ge;로 치환해서 쓴다.
② < 는 &gt;, > 는 &lt;로 치환해서 쓴다.
③ ≤ 는 &ge;, ≥ 는 &le;로 치환해서 쓴다.
④ CDATA 안에서도 < 는 반드시 &lt;로 바꿔야 한다.

## E. 트랜잭션, AOP, Interceptor

### 19.

@Transactional에 대한 설명으로 가장 적절한 것은?

① Service에서 Connection 객체를 메서드마다 넘겨야 트랜잭션이 유지된다.
② DB 접근 기술과 무관하게 @Service에서 선언적으로 트랜잭션을 처리한다.
③ Controller에는 SQLException이 그대로 전파되어 JDBC 기술에 종속된다.
④ JPA로 기술을 바꾸면 @Transactional 대신 다른 어노테이션을 써야 한다.

### 20. ★★

타겟 메서드가 실행 중 예외를 던졌을 때, 다음 중 실행되는 advice만 모두 고른 것은? (@Around는 제외)

① @Before, @AfterReturning
② @AfterReturning, @AfterThrowing
③ @Before, @After, @AfterReturning
④ @Before, @After, @AfterThrowing

### 21.

Interceptor에 대한 설명으로 가장 적절한 것은?

① preHandle은 화면 처리가 모두 완료된 시점에 호출된다.
② afterCompletion은 컨트롤러 동작 이전에 요청을 가로챈다.
③ DispatcherServlet이 HandlerAdapter를 호출하기 전후에 거친다.
④ WAS 수준에서 DispatcherServlet에 도달하기 전에 동작한다.

# PART 2. 단답형 9문제

## F. 핵심 개념 단답형

### 22.

특정 인터페이스 구현이나 상속 없이, 특정 프레임워크나 라이브러리에 종속되지 않게 작성한 평범한 자바 객체를 무엇이라 하는지 영문 약어로 쓰시오.

### 23.

Slf4j처럼 라이브러리의 복잡한 구조를 단순화해 하나의 인터페이스로 제공하는 디자인 패턴의 이름을 쓰시오.

### 24.

Java 코드의 단위 테스트 자동화를 위한 프레임워크로, @Test·@BeforeEach 등의 어노테이션을 제공하는 것의 이름을 쓰시오.

### 25.

@Autowired로 타입 기반 주입을 할 때 같은 타입의 빈이 여러 개라 충돌하는 경우, 이름 기반으로 주입될 빈을 한정하기 위해 함께 쓰는 어노테이션을 쓰시오.

### 26. ★

MyBatis에서 #{} 표기는 PreparedStatement의 ?를 대체해 값만 바인딩한다. 이와 달리 SQL 문장 자체를 재구성할 수 있는 표기를 쓰시오.

### 27.

여러 조건 중 한 가지만 적용하고 싶을 때 쓰는 choose 태그의 하위 태그 두 가지를 쓰시오. (조건마다 쓰는 태그 ㉠, 모든 조건이 거짓일 때 쓰는 태그 ㉡)

### 28. ★

trim 태그에서 처리 후 내용의 맨 앞에 지정한 문자열(예: AND, OR)이 있으면 삭제하는 속성의 이름을 쓰시오.

### 29.

advice가 동작하는 지점으로, Spring에서는 메서드 실행 시점으로 제한되는 AOP 용어를 쓰시오.

### 30.

타겟 메서드를 감싸서 메서드 호출 전과 후에 모두 실행되는 advice 어노테이션을 쓰시오.

# PART 3. 서술형 2문제

## G. 개념 서술형

### 31. ★★

Spring의 주요 특징인 DI, AOP, PSA를 각각 설명하고, 이 세 가지가 POJO와 어떤 관계인지 서술하시오.

### 32. ★★

사용자의 요청이 들어와 HTTP 응답이 나가기까지의 Spring MVC 처리 흐름을 Filter부터 순서대로 서술하고, 각 단계의 역할을 간단히 쓰시오.
