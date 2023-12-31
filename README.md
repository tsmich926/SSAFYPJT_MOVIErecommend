# final_pjt

# 웹사이트 이름:MOVIESCAPE

# Description
### <방탈출 컨셉의 영화 추천 웹사이트>
단서를 찾아 방을 탈출하는 방탈출처럼 웹사이트에서 취향에 맞는 영화를 추천받아
지루한 일상을 탈출하기를 바라는 마음에서 만들었습니다.


# 목표서비스 구현 및 실제구현정도
95%
목표서비스: 영화의 청각적 시각적 요소뿐 아니라 사용자들의 다양한 경험과
이야기를 공유할 수 있는 커뮤니티를 만들고자 했습니다.

선택장르와 좋아요한 배우와 감독을 기반으로 영화를 추천하여 최대한
유저의 취향에 맞는 영화를 추천하고자 다각도적으로 노력했습니다.


## 팀원 : <손임현, 황수아>

# 팀원정보 및 역할분담

## 손임현(팀장)
  -백엔드 시스템 담당
  협업도구 및 컨벤션 담당
  데이터 베이스 설계
  추천 알고리즘 설계
  API
  -기획 및 디자인
  컨셉 설계
  기술 스택조사
  피그마를 이용한 기본 UI설계


## 황수아  (팀원)
  -프론트엔드 담당
  일정관리
  프론트엔드 초기설정
  페이지레이아웃 설계
  세부기능
  
  -기획 및 디자인
  컨셉 디자인
  레퍼런스 수집


# 전체 일정

<img src="./schedulegant.PNG">





# 기능

알고리즘을 활용한 영화 추천
-유저가 좋아요한 영화 줄거리나 키워드의 유사도를 판별하여 비슷한 영화를 추천
-유저가 좋아요한 배우나 감독이 출연한 영화를 바탕으로 추천

전체 리뷰와 상세 리뷰페이지 구성
전체리뷰: 커뮤니티에서 
 
상세리뷰: MovieDetail을 볼 수 있는 페이지에서 리뷰를 작성하고 다른 사람들이 작성한 리뷰를 볼 수 있도록 함

전체 리뷰: 특정 영화를 선택해서  커뮤니티 페이지에 영화에 대한 후기뿐 아니라 자유로운 주제로 게시글을 올릴 수 있도록 함





(현재 2023.05.22기준)

[완료]

-컨셉설정
-서비스 기능 구현 목록 작성
-ERD 작성 및 FIxture data 작성
-UX&UI 프로토타입 작성(수기)

[수정중]
-프론트엔드 제작
-백엔드 모델,url,serializer작성

[미완료]
-추천알고리즘 만들기


--------------------------------------
(현재  2023.05.25기준)

[전체 완료]

-컨셉설정
-서비스 기능 구현 목록 작성
-ERD 작성 및 FIxture data 작성
-UX&UI 프로토타입 작성(수기)
-프론트엔드 제작
-백엔드 모델,url,serializer작성
-추천알고리즘 만들기


# 화면구성

<라우터>

### Home
HomeView 

### Movie
MovieDetailView 
MovieListView 
GenreListView 

### Human
HumanListView 
ActorDetailView 
DirectorDetailView

### Review
ReviewListView 
CreateReviewView 
ReviewDetailView 

### Recommend
RecommendView

### Account
LoginView 
SignUpView
UserDetailView 
MyDetailView

# 프론트엔드 기능 체크리스트

## 영화 목록 페이지 (MovieListView):
영화 목록을 조회하여 표시
각 영화에 대한 기본 정보 (제목, 포스터 이미지 등) 표시
영화를 클릭하면 해당 영화의 상세 페이지로 이동 (MovieDetail)


## 영화 상세 페이지 (MovieDetail):
선택한 영화의 상세 정보 표시 (제목, 포스터 이미지, 개봉일, 줄거리 등)
영화에 대한 리뷰 작성 기능 제공
다른 사람들이 작성한 리뷰 목록 표시
영화 추천 페이지 

## 영화 추천 페이지 (Recommendation):
유저의 선호도를 바탕으로 알고리즘을 활용해 유사한 영화 추천
유저가 좋아요한 영화의 줄거리나 키워드를 분석하여 유사한 영화를 추천
유저가 좋아하는 배우나 감독이 출연한 영화를 추천


## 커뮤니티(ReviewListView):
커뮤니티 형식으로 영화에 대한 후기 및 자유로운 주제의 게시글 작성 기능 제공
다른 사용자들이 작성한 리뷰 목록 표시
특정 영화를 선택하여 해당 영화에 대한 리뷰를 작성가능

## 출연진 목록 페이지 (ActorListView):
영화에 출연한 배우와 감독 목록 표시
각 배우를 클릭하면 해당 배우의 상세 정보 페이지로 이동
배우에 하트를 눌러 추후 해당 배우가 출연한 영화를 추천 받을 수 있음.

# ERD
<img src="./erd_readme.png">

# UX/UI Figma
<img src="./UX_UI_Figma.png">



# 서비스 대표기능

## 영화 검색기능
영화를 검색하면 프로필과 포스터가 자동완성으로 
출력된다. 출력된 영화 중 하나를 클릭하면
영화Detailview로 갈 수 있다.

## 프로필 뽑기 기능
단어를 검색하면 그 단어에 맞는
사진이 나오게 되고 그 사진을
프로필로 설정가능

## 인피니티 스크롤
무한하게 스크롤을 내릴 수 있음.


## 장르목록 선택가능
여러가지 장르중 장르를 선택하여 영화를 추천받을 수 있음

## 직관적인 UI
화면 구성이 직관적임.


# 서비스 기능 목록

### 로그인/로그아웃/회원가입

### 유저 팔로우

### 마이페이지 조회

### TMDB 자료 추출 및 DB화


### 영화 메인페이지
-선호하는 장르기반의 영화 추천 

영화 페이지를 출력하기전 유저가 선호장르를 선택할 수 있도록 함.

/범죄/ 스릴러 /공포 /미스터리/

/모험 /판타지/ SF/

/액션/ 서부/ 전쟁/

/가족 /애니메이션/ TV영화/

/역사/다큐멘터리/로맨스/코미디/드라마/

총 18개의 장르중 관심 있는
장르를 선택하면 비슷한 장르의 영화를 추천
-전체-를 선택하여 전체 영화를 출력하게 할 수도 있음.

인피니티 스크롤을 구현하여 마음에 드는 영화를 찾을때까지
끊임없이 스크롤을 내릴 수 있도록 함


### 단일 영화 페이지 조회
 세부 영화 정보표현, 영화 트레일러 영상,
 출연 영화배우와 감독을 볼 수 있으며 영화를 좋아요 하여
 자신의 페이지 목록에 담을 수 있다.
 
 영화에 대한 댓글 목록이 출력되어 다른 사람들이 영화에 대해 
 어떤 평가를 내렸는지 알 수 있다.

 ### 리뷰 생성/삭제
영화에 대한 리뷰를 게시판에 생성하고 삭제

 ### 댓글 생성/삭제
 다른 유저의 리뷰에 댓글을 달 수 있으며 삭제도 가능

 ### 다른 유저의 페이지확인 및 팔로우
 다른 유저가 좋아요한 배우나 영화를 보고 취향을 파악 할 수 있으며
 팔로우하여 친분을 쌓을 수 있음

### 배우& 감독목록
인피니트 스크롤을 구현하여 취향에 맞는 감독과 영화배우를 좋아요 할 수 있도록 함.

### 추천기능
좋아요한 장르와 배우,감독을 통해 유저의 취향에 맞는 영화를 추천.


# 느낀점

이번 프로젝트는 처음으로 일주일 동안 중규모 프로젝트를 진행했습니다.  그러나 이번 프로젝트를 통해 Git을 이용한 협업을 처음으로 경험하면서 어려움이 많았습니다. 특히, 동일한 파일에서 작성한 코드가 충돌하여 병합 충돌 상황이 자주 발생했습니다. 이러한 문제를 해결하기 위해 GitHub의 병합 창에서 직접 수정하거나, 한 사람이 먼저 올린 코드를 기준으로 다시 가져와 병합하는 방법을 사용했습니다.
앞으로 개발자로 성장하기 위해서는 Git을 이용한 협업 과정이 필수적입니다. 이번 프로젝트에서 수많은 시행착오를 통해 Git을 이용한 협업의 흐름을 익힐 수 있었으며, GitHub의 organization 기능을 이용한 협업도 처음에는 어려웠지만 점차 익숙해지고 편리한 기능임을 깨달았습니다. 앞으로 2학기 프로젝트를 진행하면서 이번 경험을 바탕으로 협업 프로젝트를 더욱 원활하게 진행할 수 있을 것입니다.

이번 프로젝트는 일주일 동안 진행되었으며, Vue를 사용하여 프론트엔드를 구성하는 작업을 수행했습니다. 프로젝트 진행 중 컴포넌트 구성과 작업에 많은 어려움을 겪었습니다. 부모 요소의 정보를 자식 컴포넌트로 전달하거나 렌더링 과정에서 이를 고려하는 것이 복잡하여 예상보다 많은 시간을 소요하게 되었습니다. 추후에는 이 부분을 보강하여 개선해야 할 것으로 판단됩니다. 또한, CSS의 transition과 animation을 구현하는 과정도 복잡하여 충분히 구현하지 못한 점이 아쉬웠습니다. 그러나 위치와 배치에 대한 고민과 경험을 많이 쌓을 수 있어서 정말로 다행으로 생각합니다.

백엔드를 구성하는 과정에서 ERD를 그려보고 화면설계를 통해 어떻게 웹 페이지를 만들지 고민했습니다. 구성하는 과정 중에 화면설계를 하기 위해 어떠한 데이터가 필요한지 분류를 해야했고 필요한 데이터를 넣을 모델을 설계해야 했습니다. 이러한 과정을 진행하며 백엔드 DB모델링에 익숙해질 수 있었으며, 데이터간의 N:M, 1:N등의 관계에 익숙해질 수 있었습니다. 초기에 ERD 설계를 잘 하고 사용할 URL과 View들을 잘 정리해둔 덕분에 쉽게 데이터에 접근하고 사용할 수 있었습니다. 기초적인 설계가 튼튼해야 프로젝트가 잘 진행된다는 점을 느꼈고, 이후 프로젝트에서도 이번 관통 프로젝트 경험을 바탕으로 설계를 꼼꼼히 하고 프로젝트를 준비해야겠다고 생각했습니다.

