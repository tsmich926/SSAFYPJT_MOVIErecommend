# final_pjt

# 웹사이트 이름:MOVIESCAPE

# Description
<방탈출 컨셉의 영화 추천 웹사이트>
단서를 찾아 방을 탈출하는 방탈출처럼 웹사이트에서 취향에 맞는 영화를 추천받아
지루한 일상을 탈출하기를 바라는 마음에서 만들었습니다.


# 모델 구성

[accounts] 

[movies] 


# ERD


# 화면구성

<라우터>
- MovieListView
- MovieDetail
- Recommendation
- ReviewListView
- ActorListView


# 기능

알고리즘을 활용한 영화 추천
-유저가 좋아요한 영화 줄거리나 키워드의 유사도를 판별하여 비슷한 영화를 추천
-유저가 좋아요한 배우나 감독이 출연한 영화를 바탕으로 추천

전체 리뷰와 상세 리뷰페이지 구성
전체리뷰: 커뮤니티에서 
 
상세리뷰: MovieDetail을 볼 수 있는 페이지에서 리뷰를 작성하고 다른 사람들이 작성한 리뷰를 볼 수 있도록 함

전체 리뷰: 특정 영화를 선택해서  커뮤니티 페이지에 영화에 대한 후기뿐 아니라 자유로운 주제로 게시글을 올릴 수 있도록 함


# 전체 일정

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



# 프론트엔드 기능 체크리스트

영화 목록 페이지 (MovieListView):
영화 목록을 조회하여 표시
각 영화에 대한 기본 정보 (제목, 포스터 이미지 등) 표시
영화를 클릭하면 해당 영화의 상세 페이지로 이동 (MovieDetail)


영화 상세 페이지 (MovieDetail):
선택한 영화의 상세 정보 표시 (제목, 포스터 이미지, 개봉일, 줄거리 등)
영화에 대한 리뷰 작성 기능 제공
다른 사람들이 작성한 리뷰 목록 표시
영화 추천 페이지 

영화 추천 페이지 (Recommendation):
유저의 선호도를 바탕으로 알고리즘을 활용해 유사한 영화 추천
유저가 좋아요한 영화의 줄거리나 키워드를 분석하여 유사한 영화를 추천
유저가 좋아하는 배우나 감독이 출연한 영화를 추천


커뮤니티(ReviewListView):
커뮤니티 형식으로 영화에 대한 후기 및 자유로운 주제의 게시글 작성 기능 제공
다른 사용자들이 작성한 리뷰 목록 표시
특정 영화를 선택하여 해당 영화에 대한 리뷰를 작성가능

배우 목록 페이지 (ActorListView):
영화에 출연한 배우 목록 표시
각 배우를 클릭하면 해당 배우의 상세 정보 페이지로 이동
배우에 하트를 눌러 추후 해당 배우가 출연한 영화를 추천 받을 수 있음.

# ERD
![ERD](https://lab.ssafy.com/soh2254/final_pjt/-/blob/master/erd_readme.png)

# UX/UI Figma
![ERD](https://lab.ssafy.com/soh2254/final_pjt/-/blob/master/UX_UI_Figma.png)
