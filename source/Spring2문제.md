# PART 1. 객관식 21문제

## A. Spring 개요, 로깅, 테스트

### 1.

Spring Boot에 대한 설명으로 가장 적절한 것은?

① Spring과 별개의 프레임워크로 DI 컨테이너를 사용하지 않는다.
② Spring 애플리케이션 개발용 템플릿으로, 설정을 자동화해 준다.
③ XML 설정 파일을 반드시 작성해야 애플리케이션이 실행된다.
④ 웹 애플리케이션이 아닌 경우에는 사용할 수 없는 도구이다.

### 2.

Slf4j(Simple Logging Facade for Java)에 대한 설명으로 가장 적절한 것은?

① 로그를 파일에 직접 기록하는 구현체로 다른 라이브러리와 함께 쓸 수 없다.
② 로그 레벨은 debug, info, error 세 단계만 구분해서 제공한다.
③ System.out.println처럼 레벨 구분 없이 모든 로그를 콘솔에 출력한다.
④ 로깅용 Facade로, Logback·Log4j 구현체를 단순한 인터페이스로 감싼다.

### 3.

좋은 단위 테스트의 원칙 F.I.R.S.T에 대한 설명으로 옳지 않은 것은?

① Fast: 외부 환경과 무관하게 작성해 빠르게 동작해야 한다.
② Independent: 이전 테스트가 남긴 상태에 의존하지 않아야 한다.
③ Repeatable: 실행할 때마다 다른 결과가 나와야 신뢰할 수 있다.
④ Self-Validating: 테스트 자체만으로 성공·실패 검증이 끝나야 한다.

### 4. ★

다음 테스트 코드의 (가)~(다)에 들어갈 Given-When-Then 단계로 옳은 것은?

@Test
void joinTest() {
    // (가)
    Member member = new Member("ssafy", "ssafy@ssafy.com");
    // (나)
    Long memberId = memberService.join(member);
    // (다)
    assertEquals("ssafy", memberService.findOne(memberId).getName());
}

① (가) given, (나) when, (다) then
② (가) when, (나) given, (다) then
③ (가) given, (나) then, (다) when
④ (가) then, (나) when, (다) given

### 5.

@SpringBootTest에 대한 설명으로 가장 적절한 것은?

① 단일 메서드만 격리해서 실행하므로 단위 테스트에 가장 적합하다.
② 스프링 컨테이너 없이 순수 자바 객체만 생성해서 테스트한다.
③ 애플리케이션 전체를 구동하는 통합 테스트용이라 단위 테스트엔 부적합하다.
④ static 메서드에만 붙일 수 있어 테스트 클래스 전체에서 1번만 실행된다.

## B. DI와 Bean 관리

### 6. ★★

다음 코드를 실행했을 때의 결과로 옳은 것은? (단, WasherUser에는 기본 생성자, setter, getter가 있다.)

@Configuration
public class WasherConfig {
    @Bean public SWasher sWasher() { return new SWasher(); }
    @Bean public LWasher lWasher() { return new LWasher(); }
    @Bean(name = "myWasherUser")
    public WasherUser washerUser() {
        WasherUser washerUser = new WasherUser();
        washerUser.setWasher(sWasher());
        return washerUser;
    }
}

ApplicationContext ctx = new AnnotationConfigApplicationContext(WasherConfig.class);
WasherUser user = ctx.getBean(WasherUser.class);
Washer sWasher = ctx.getBean(SWasher.class);
System.out.println(sWasher == user.getWasher());

① 빈 이름이 myWasherUser라서 getBean(WasherUser.class)에서 예외가 발생한다.
② sWasher()가 다시 호출되어 새 객체가 주입되므로 false가 출력된다.
③ setter 주입은 @Bean 메서드 안에서 쓸 수 없어 컴파일 오류가 발생한다.
④ 컨테이너가 같은 sWasher 빈을 주입해 싱글톤이 유지되므로 true가 출력된다.

### 7.

묵시적 DI에 대한 설명으로 가장 적절한 것은?

① @Component는 빈 후보 표시일 뿐이라 @ComponentScan으로 스캔돼야 등록된다.
② @Component를 붙이면 @ComponentScan 없이도 어디서든 즉시 빈으로 등록된다.
③ @Component의 value 속성은 빈 스코프를 지정하며 빈 이름은 바꿀 수 없다.
④ @Autowired는 이름 기반으로 주입하므로 같은 타입 빈이 여러 개여도 문제없다.

### 8.

스테레오타입 어노테이션과 용도의 연결로 옳지 않은 것은?

① @Repository: MVC에서 Model의 DAO 계열 빈
② @Service: 클라이언트 요청을 받아들이는 Controller 계열 빈
③ @Configuration: Java 기반의 메타 정보(설정) 클래스
④ @Component: 다른 스테레오타입에 해당하지 않는 일반 빈

## C. Spring MVC 요청 처리

### 9. ★

다음 컨트롤러에 대한 설명으로 옳은 것은?

@Controller
@RequestMapping("/board")
public class BoardController {
    @GetMapping("/list") public String list() { ... }
    @PostMapping("/write") public String write() { ... }
}

① list 메서드는 GET /list 요청을 처리하며 클래스 레벨 경로는 무시된다.
② write 메서드는 HTTP 메서드와 관계없이 GET과 POST를 모두 처리한다.
③ list는 GET /board/list, write는 POST /board/write 요청을 처리한다.
④ @RequestMapping은 클래스 레벨에만 쓸 수 있고 메서드에는 쓸 수 없다.

### 10. ★★

GET /calc?num1=10&num2=20&num3=plus 요청이 다음 메서드로 들어왔을 때의 결과로 옳은 것은?

@GetMapping("/calc")
@ResponseBody
public Map<String, Integer> calc(@RequestParam Integer num1, @RequestParam Integer num2, @RequestParam("num3") String result)

① num1=10, num2=20이 Integer로 변환되고, result에는 num3 값 plus가 담긴다.
② result라는 이름의 요청 파라미터가 없으므로 result에는 null이 들어간다.
③ @RequestParam은 문자열만 받을 수 있어 Integer 타입에서 오류가 발생한다.
④ 메서드 이름 calc와 같은 이름의 요청 파라미터만 바인딩 대상이 된다.

### 11. ★

다음 메서드에서 @ModelAttribute가 Member 객체를 만드는 과정으로 옳은 것은? (단, Member에는 기본 생성자와 setter가 있다.)

@GetMapping("/regist")
public String regist(@ModelAttribute Member member, Model model) { ... }

① setter 없이 필드에 직접 값을 넣으므로 DTO에는 setter가 필요 없다.
② 생성된 객체는 Model에 추가되지 않아 뷰에서 직접 꺼내 쓸 수 없다.
③ 요청 본문의 JSON을 메시지 컨버터로 읽어 Member 객체를 생성한다.
④ 기본 생성자로 객체를 만들고 setter로 채운 뒤 member 이름으로 Model에 담는다.

### 12.

다음 메서드에 대한 설명으로 옳은 것은?

@GetMapping("/cookie")
@ResponseBody
public Map<String, Object> cookie(@CookieValue String name, @CookieValue int age) { ... }

① 쿠키 값은 항상 String이므로 int age로 선언하면 컴파일 오류가 난다.
② 이름이 name, age인 쿠키 값을 가져오며 int로 자동 형 변환도 된다.
③ @CookieValue를 쓰면 서버가 새 쿠키를 자동으로 생성해 응답에 담는다.
④ 쿠키 대신 이름이 name, age인 요청 파라미터를 찾아 값을 바인딩한다.

### 13. ★★

forward, redirect와 Redirect 시 데이터 전달에 대한 설명으로 가장 적절한 것은?

① 뷰 이름만 반환하면 redirect로 처리되고, forward는 forward: 접두사가 필수다.
② RedirectAttributes로 추가한 일반 속성은 객체 그대로 전달되어 형식 제약이 없다.
③ Flash Scope는 redirect 완료 때까지만 유지되며 request < flash < session 범위다.
④ session에 저장한 값은 redirect 후 자동으로 삭제되므로 따로 지울 필요가 없다.

## D. MyBatis

### 14.

MyBatis mapper 작성 규칙에 대한 설명으로 가장 적절한 것은?

① namespace는 DAO 인터페이스의 전체 이름, id는 연결할 메서드 이름을 쓴다.
② @Mapper 인터페이스는 개발자가 구현 클래스를 직접 작성해 등록해야 한다.
③ SQL의 파라미터는 PreparedStatement처럼 ? 기호를 직접 써서 지정한다.
④ useGeneratedKeys는 조회 결과를 DTO에 자동 매핑할지 정하는 속성이다.

### 15.

DB 컬럼 detail_address를 DTO 필드 detailAddress에 매핑하는 방법으로 가장 적절한 것은?

① 컬럼명과 필드명이 달라도 setter만 있으면 MyBatis가 항상 자동 매핑한다.
② resultType 대신 parameterType을 지정하면 컬럼 이름이 자동으로 변환된다.
③ DB 컬럼명을 대문자로 바꾸면 카멜 케이스 필드에 자동으로 바인딩된다.
④ map-underscore-to-camel-case=true 설정이나 resultMap의 result 태그를 쓴다.

### 16. ★★

다음 매퍼에 titles = ["home", "office"]를 전달했을 때 실행되는 SQL로 옳은 것은? (바인딩 값은 실제 값으로 표기)

<select id="selectUseIn" resultMap="addressMap">
    SELECT * FROM address
    <where>
        <foreach collection="titles" item="title" open="title in (" separator="," close=")">
            #{title}
        </foreach>
    </where>
</select>

① SELECT * FROM address WHERE title = 'home' OR title = 'office'
② SELECT * FROM address WHERE title in ('home','office')
③ SELECT * FROM address title in ('home','office')
④ SELECT * FROM address WHERE title in ('home' 'office')

### 17. ★★

다음 매퍼에 title="seoul", mno=3을 전달했을 때 실행되는 SQL로 옳은 것은?

<select id="dynamicQuery" resultMap="addressMap">
    SELECT * FROM address WHERE 1=1
    <choose>
        <when test="title != null">AND title = #{title}</when>
        <when test="mno != null">AND mno = #{mno}</when>
        <otherwise>AND ano > 0</otherwise>
    </choose>
</select>

① SELECT * FROM address WHERE 1=1 AND title = ? AND mno = ?
② SELECT * FROM address WHERE 1=1 AND ano > 0
③ SELECT * FROM address WHERE 1=1 AND title = ? AND ano > 0
④ SELECT * FROM address WHERE 1=1 AND title = ?

### 18.

MyBatis의 #{} 표기에 대한 설명으로 가장 적절한 것은?

① PreparedStatement의 ?를 대체해 값만 바인딩하고 SQL 구조는 바꾸지 않는다.
② 값을 문자열 그대로 이어 붙이므로 SQL 문장 자체를 재구성할 수 있다.
③ 값을 그대로 이어 붙이므로 SQL Injection 공격에 가장 취약한 방식이다.
④ 컬럼명이나 테이블명처럼 SQL 구조를 동적으로 바꿀 때 주로 사용한다.

## E. AOP, Interceptor, 요청 흐름

### 19.

AOP 기본 용어에 대한 설명으로 가장 적절한 것은?

① target은 횡단 관심 코드를 모듈화한 메서드이다.
② join point는 advice를 적용할 대상을 고르는 표현식이다.
③ weaving은 aspect를 비즈니스 로직 코드에 적용하는 행위이다.
④ aspect는 핵심 비즈니스 로직을 포함한 빈 객체이다.

### 20. ★★

하나의 컨트롤러에 인터셉터 A, B가 A → B 순서로 등록되어 있고, 모든 preHandle이 true를 반환한다. 메서드 호출 순서로 옳은 것은? (preHandle=pre, postHandle=post, afterCompletion=after)

① preA → preB → 컨트롤러 → postA → postB → afterA → afterB
② preA → preB → 컨트롤러 → postB → postA → afterB → afterA
③ preB → preA → 컨트롤러 → postA → postB → afterA → afterB
④ preA → postA → preB → postB → 컨트롤러 → afterB → afterA

### 21.

사용자 요청이 들어와 처리되는 순서로 옳은 것은?

가. Filter
나. DispatcherServlet
다. HandlerMapping
라. HandlerInterceptor의 preHandle
마. Controller
바. ViewResolver

① 나 → 가 → 다 → 라 → 마 → 바
② 가 → 나 → 라 → 다 → 마 → 바
③ 가 → 다 → 나 → 라 → 마 → 바
④ 가 → 나 → 다 → 라 → 마 → 바

# PART 2. 단답형 9문제

## F. 핵심 개념 단답형

### 22. ★

Lombok의 @Builder로 객체를 만들면 필드 초기값이 무시된다. 아래 addresses의 기본값을 유지하려면 ㉠에 들어갈 어노테이션을 쓰시오.

@Builder
public class Member {
    private String name;
    @㉠
    private List<Address> addresses = new ArrayList<>();
}

### 23.

메서드 호출 결과가 예상한 값과 동일한지 판단하는 문장으로, JUnit에서 assertEquals 등을 제공하는 것을 무엇이라 하는지 쓰시오.

### 24.

JUnit 5에서 반드시 static으로 선언해야 하는, 테스트 클래스 전체에서 처음과 마지막에 한 번씩만 실행되는 어노테이션 2개를 쓰시오.

### 25. ★★

다음 trim 태그가 set 태그와 같은 역할을 하도록 빈칸 ㉠, ㉡에 들어갈 값을 쓰시오.

<update id="dynamicUpdate">
    update address
    <trim prefix="㉠" suffixOverrides="㉡">
        <if test="mno != null">mno=#{mno},</if>
        <if test="title != null">title=#{title},</if>
    </trim>
    WHERE ano=#{ano}
</update>

### 26.

자주 쓰는 SQL 조각을 <sql id="select_address">로 선언했다. 이 조각을 다른 쿼리에서 참조할 때 사용하는 태그 이름 ㉠과, 참조할 sql의 id를 지정하는 속성 이름 ㉡을 쓰시오.

### 27.

XML 매퍼에서 부등호 < 를 그대로 쓰면 태그로 해석되는 문제가 있다. &lt; 같은 치환 문자 대신, 내부 문자열을 XML로 해석하지 않도록 감싸는 섹션의 이름을 쓰시오.

### 28.

Redirect가 완료될 때까지만 데이터가 저장되는 Spring 지원 스코프로, 한 번의 요청 후 사라지는 session 스코프라고도 하는 것의 이름을 쓰시오.

### 29.

@Transactional을 사용해 서비스에서 선언적 트랜잭션을 처리할 때, 데이터 접근 기술과 무관하게 Controller까지 전파되는 스프링의 예외 클래스 이름을 쓰시오. (SQLException이 아님)

### 30.

타겟 메서드가 수행 중 예외를 던질 때에만 동작하는 Advice 어노테이션을 쓰시오.

# PART 3. 서술형 2문제

## G. 비교 서술형

### 31. ★★

Filter, Interceptor, AOP를 다음 두 관점에서 비교하여 서술하시오. ① 동작 수준과 가로채는 대상 ② 각각 사용하기 적합한 상황

### 32. ★★

Redirect 시 다음 페이지로 데이터를 전달하는 방법 세 가지(query string, session, Flash Scope)를 각각의 특징이나 단점과 함께 서술하시오.
