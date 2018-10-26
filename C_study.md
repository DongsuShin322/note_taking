기계어 : 0과 1로 이루어진 언어 - 하드웨어 직접 통제

어셈블리어 : 기계어를 프로그래머가 좀 더 이해하기 쉽게 ex) LDA or ADD 

-------------------------------------------------- low level language : 어려워서 생산성이 낮다

컴파일러 : 소스파일(고급언어) ----> 목적파일(기계어)

어셈블러 : 어셈블리언어 ----> 기계어



링커 : 목적파일 + 라이브러리 ----> 실행파일 ex) .exe or .com

로더 : 실행파일 ----> 메모리

디버거 : 오류수정

에디터 : 프로그래밍 언어 내용 편집

---------------------------------------------------- IDE(통합개발환경) : 위와 같은 기능 모두 제공



Vim으로 C 프로그래밍 후 gcc로 컴파일 후 실행하기

1. name.c 로 코드 작성 후 저장
2. gcc -o name_execute name.c
3. name_execute 실행




C 언어 함수 구성

1. return type
2. function_name
3. argument

main 함수 - 프로그램이 시작되는 지점 / 반드시 하나 존재!!



#  Chapter 1

출력함수 - printf( " ~~ \n")

세미콜론(;) 으로 마무리



# Chapter 2 

주석(comment) - 여러 줄에 걸친 주석( /*  */)과 한 줄 짜리 주석( // )



변수 선언 (type, name, value)  ex) int myAge = 18;  

변수는 자료값을 저장하는 공간 (type에 따라 RAM에 할당되는 공간 크기 결정)

printf("myAge : %d\n", myAge);

%d : 정수 / %i : 기본은 정수지만 앞에 0이나 0x가 붙으면 8진수 혹은 16진수로 저장

%f : float / %lf : double / %c : 문자 / \t : Tab 공백

%o : 8진수 / %x : 16진수 / %s : 문자열 



# Chapter 3

함수 시작 부분에 변수 선언되어야 함!



오버플로우(overflow) : 저장할 수 있는 범위의 수보다 크거나 작을 때 발생!

​	signed int에서 overflow발생하면 순환한다.



상수(constant number) : 수정할 수 없는 수 ex) const double PI = 3.14;

정수형 자료형 : short(2 byte) -> int(2 or 4 byte) -> long(4 byte)

문자형 : char(1 byte)

실수 - 부동소수형 : float(4 byte) -> double(8 byte) 

ex) float c = 3.14F;

​	printf(" %20.18f "); - 소수점을 포함하여 출력폭을 20으로 + 소수점 아래 18자리



저장공간 크기 확인 : ex) sizeof (x) 

자료형 재정의 : ex) typedef int myint; -- 새로운 자료형 myint를 int처럼 사용 가능



# Chapter 4

(#)include <*.h> - stdio.h / math.h / string.h / time.h 등등 헤더파일을 컴파일 전 수행

(#)define PI 3.141592 - 기호상수를 문자열로 대체

(#)define SQUARE(x) ( (x) * (x) ) - 인자를 이용하여 매크로 정의



입력함수 - scanf()

​	ex) int age, height;

​		scanf("%d %d", &age, &height); --> age와 height 주소 찾아가서 정수 값을 할당하라



출력함수 - printf()

​	ex) printf("%05d", 30); --> 출력폭 5, 우측정렬, 0으로 빈칸 채움

​		printf("%-5.2f", 3.1); --> 출력폭5, 소수점아래 2자리, 좌측정렬

​		printf(" \" %s \" \n ", "대한민국"); --> 



char c = getchar() or int i = getchar(); --> 문자 또는 상수 하나 입력받음

putchar(c) or putchar(i); --> 입력받은 하나의 문자 또는 상수를 출력



# Chapter 5

!= 같지않다 (C언어 : True -> 1 / False -> 0)

++a : 증가 후 식 실행 / a++ : 식 실행 후 증가



단축평가(short circuit evaluation)

&& 와 || 논리 연산할 때 앞에 것에 따라 뒤의 것 실행 안함

​	ex) int a = 10, b = 20;

​		(a++ == 11) && (b++ == 20); --> b++ 실행 안되므로 이후에도 b는 여전히 20임



조건식 ? True 실행 : False 실행

​	ex) max = (x > y) ? x : y 



비트연산과 이동

&(AND) / |(OR) / ^(XOR) / ~(Complement)

7 << 2 : 7을 왼쪽으로 2비트 이동 / 7 >> 2 : 7을 오른쪽으로 2비트 이동



형 변환

ex) double result;

​	result = (double) 9 / (double) 2 --> 4.5 저장

​	result = 9 /2 --> 4.0 저장



저장장소 크기 - sizeof()결과 값은 byte 단위 정수

ex) int myAge = 10;

​	printf("%d\n", sizeof (myAge)); 



# Chapter 6

조건문 : if(조건) --> 콜론(:) 없음

switch문 : expression의 값이 case의 값과 일치하는 것을 처리

ex) switch (expression)

{

​	case value1:

​		statement1;

​		break;

​	default :

​		statement;

​		break;

}



반복문 : for, while, do while

ex) for (초기화; 조건검사; 증감연산){} --> 1. 초기화 2. 조건검사 3. 몸체실행 4. 증감연산

​	while (조건문){} --> 1.조건검사 2. 몸체실행

​	do {} while (조건문); --> 무조건 한번은 실행 / 마지막에 세미콜론(;) 꼭 써줄 것!

for 문에서 초기화 부분과 증감연산 부분을 콤마를 이용하여 여러 개의 문장 기술 가능

​	ex) for (sum = 0, i = 1; i <= 10; sum += i, i++);



continue문 : 아래 문장들 수행하지 않고 증감연산 / 조건검사로 넘어감!!

무한반복 : for ( ; ; ) 또는 while (1)



# Chapter 7

1. 함수원형 ex) int add(int a, int b); --> 함수호출 전에 함수원형 쓸 것, 세미콜론(;)으로 마무리
2. 함수호출 ex) int main(void) { sum = add(3,5); }
3. 함수구현 ex) int add(int a, int b){ ... }



난수발생 

-- #include <stdlib.h> --> rand() 함수 이용 위해 헤더 파일 추가

-- #include <time.h> --> seed 위해 헤더 파일 추가

ex) long seed;

​	seed = time(NULL); 

​	srand(seed); --> 시간을 seed로 주어서 매번 다른 난수 발생하도록

​	rand() % n; --> 0부터 n-1 범위의 난수 발생 ( rand() % n + 1 으로 하여 1부터 n 사이의 난수 발생)



# Chapter 8

배열(array) : 동일한 유형 / 유형 이름[크기] ex) int score[10] --> index : 0 ~ N-1

int a[4] = {1,2,3,4}; 로 초기화 가능

int a[] = {1,2,3,4}; 인 경우 배열의 크기는 4로 자동 결정

int a[10] = {1,2}; 인 경우 나머지는 모두 0으로 초기화 됨



문자열 : 문자 배열 이용!! ex) char s[] = " C Language! ";

​		마지막 문자를 NULL 문자로 인식하므로 배열크기 = 문자의 수 + 1 

​		ex) char s[4] = "abc";  <====>  char s[4] = {'a', 'b', 'c', '\0'};

문자열 출력하는 방법 2가지 ex) char lang[] = "C Language!"

1. printf("%s", lang); --> 문자열 출력이므로  %s 사용

2. for (i=0; lang[i]; i++) --> 마지막 문자를 제외하고는 Null이 아니므로 그 전까지 수행

   {	printf("%c", lang[i]);	} --> 문자 출력이므로 %c 사용

문자열을 입력으로 받을 때

1. 공백 포함안하는 경우  

   ex) char input[30];

   ​	scanf("%s", input); --> 정수나 문자와 달리 & 붙이지 않는다.

2. 공백 포함하는 문자열 받는 경우--> %[ ] 안에 ^\n 넣는다.

   ex) char input[80];

   ​	scanf("%[^]", input); [^]뒤에 나오는 것 나오면 stop! 이므로 ^\n 넣으면 됨

   ​	printf("%s", input); 



실수 5개 입력 받아서, 배열에 넣기

ex) double x[5];

​	int i;

​	for (i=0; i<5; i++)

​	{

​		scanf("%lf", &x[i]);

​	}

원소 갯수 구하기 --> sizeof (x) / sizeof(x[0]) : 배열 전체의 크기를 한 칸의 크기로 나눔 --> 칸의 갯수



# Chapter 9

전역변수 키워드 : extern

정적변수 키워드 : static --> 프로그램 실행되면 메모리에 할당되고, 프로그램 종료시까지 메모리에 남아있다. 오직 한번만 초기화 됨 (즉, 블록이 종료해도 메모리에 남아있음)



# Chapter 10

주소(Address) : 저장공간 위치 나타내는 주소 값 on 메모리(1 byte씩 증가하며, 주로 16진수로 표시) 

​	ex) 0x00000000 ... 0x3FFFFFFF

%p : 주소값 (16진수 unsigned int형) / %u : unsigned int형!



포인터 변수 : 주소 값을 저장하는 변수 ex) int *ptr; --> int형은 4 byte

포인터 변수 초기화 : int *ptr = NULL; --> 0번지 주소값을 의미하므로 아무 변수도 가르키고 있지 않음

​	ex) int i =3;	

​		int *ptr;		<====> int *ptr = &i;

​		ptr = &i; (i의 주소값을 포인터 변수 ptr에 저장)

*(포인터 변수) = 포인터 변수가 가르키는 변수 자체 

​	ex) *ptr == i 	/	 *ptr = *ptr + 1 <==> i = i + 1

int *ptr = (int *) 30; --> ptr 내부 값이 int형 주소값 30을 가짐, 즉 30 + 4 만큼의 주소를 참조



배열과 포인터

ex) int point[] = {95,66,76}

​	point == &point[0] --> 배열이름은 배열 첫번째 원소의 주소값

​	*point == point[0] --> *배열이름은 배열 첫번째 원소 값

​	*(point+i) == point[i]



포인터의 포인터

ex) int i = 10;

​	int *ptri = &i;

​	int **dpi = &ptri;

​	i == *ptri == **dpi



다차원 배열 포인터

ex) int tAry[2].[3] = { {1,2,3},{4,5,6}} 

​	tAry == &tAry[0] --> 배열이름은 배열 첫번째 열의 주소값 (*tAry == tAry[0])

​	tAry[0] == &tAry[0].[0] --> 첫번째 원소의 주소값 (*tAry[0]==tAry[0].[0])

​	**tAry == tAtry[0].[0]



# Chapter 11

문자 배열 출력 방법 2가지

​	ex) char c2[] = "C language"

​		char *c4 = "C language"

1. 배열 이용

   ​	while(c2[i] != '\0'){}

2. 포인터 이용

   ​	while(*(c4+i) != '\0'){}



문자열 함수

1. strcmp("ab","ad") : 사전순으로 비교해서 오름차순이면 음수, 같으면 0, 내림차순이면 양수
2. strlen(" ") : NULL 제외한 문자열 길이 반환
3. strcat("my","name") : 문자 연결
4. strstr() : 문자열 찾아서 주소값 반환
5. strtok() : 구분자 기준으로 토큰 추출



# Chapter 12

구조체(structure) : 함수는 없고 멤버 변수들만 존재 / 초기화 X

정의시 : struct book(구조체 이름)

{ int pages;

​	char edition;

​	char title[50];

};

사용 시 : struct book mybook; (struct book이 자료 유형)

mybook = {10, 'A', "Love is you"}; 로 초기화 (초기화 안하면 기본 값)

구조체 멤버 접근 : mybook.pages = 200;



구조체 포인터

​	ex) struct univ ku = {"한국대학교", "서울시 서초구", 5000};	

​		struct univ *ptr = &ku;

구조체 멤버 참조 : ptr -> name or (*ptr).name



열거형(enum) : 각 element가 상수에 대응

ex) enum day7 {sum, mon, tue, wed, thu, fri, sat} --> 순서대로 0부터 6까지 (지정하는 것도 가능)

​	typedef enum day7 day;

​	day today = fri;





