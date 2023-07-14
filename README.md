# 서비스 소개
![KakaoTalk_Photo_2023-07-15-04-02-36](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/4ee01c5b-3d5e-4a4e-ac2e-d11cda967d41)
```
무사히 귀가하고 싶은 그레텔! 과연 그녀는 집에 무사히 귀가할 수 있을까..?
안전 귀가를 원하는 그레텔을 위한 서비스, 내 귀가 캔디
꿀팁! 초행길도 안전성을 검색할 수 있습니다!
```

**내 귀가 캔디**는 헨젤과 그레텔에서 영감을 얻어, 캔디를 떨어트려 무사히 집에 도착한다는 컨셉의 서비스입니다.

자신의 이동 좌표를 맵에 캔디 모양으로 기록하여 주변들에게 내 이동 경로를 공유할 수 있습니다. 내 위치를 기반으로 다른 사람이 작성한 주변 골목길 정보를 수집해서 골목길 위험도를 판단할 수 있습니다. 그 외에도 다양한 안전정보를 제공합니다.

![KakaoTalk_Photo_2023-07-15-04-02-29](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/da3222e7-2a0a-4a7a-b86c-7016d02cf191)

### 팀원 소개

| 김채현                                                       | 김소영                                                       | 박상아                                                       | 양수빈                                                       | 이지원                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![채현](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/76d715f6-dc2f-46cc-8b4e-f62dc4238880) | ![소영](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/dc7f43d7-150d-4aed-8ab4-fbed5bd946c8) | 
![상아님](https://github.com/42wekey/42wekey-front/assets/86940801/a36cba41-5e09-43d9-81ea-25a6a7333fe1) | ![수빈](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/8c411af0-e36d-431d-8b02-2cde773d5f03) | ![지원](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/d8d11df2-d901-4c0a-8253-1d58c0b4c699) |
| 기획 및 디자인<br />프론트엔드                               | 프론트엔드                                                   | 프론트엔드                                                   | 백엔드                                                       | 백엔드                                                       |
| • 현위치 반경 내 경찰서,치안센터 카카오 지도에 마커 출력 <br />• 지역을 검색창에 입력하면 해당 지역의 경찰서, 치안센터 지도에 마커 출력 <br />• 현위치 반경 내 골목길 안전성 평가글 지도에 마커 출력 및 목록 조회 <br />• 사용자가 클릭한 위치의 값 다음 페이지에 전송 및 받아오기 | • 상단바 구현 <br />• 골목길 상세페이지 구현 <br />• 대처 요령 페이지 구현 | • 로그인 페이지 구현 <br />• 헤더, 푸터 구현 <br />• 골목길 작성페이지 구현<br /> • 사이렌 페이지 구현 | • 베이스 템플릿 및 static 관리 <br />• 카카오 회원가입 및 로그인 구현 <br />• 골목길 전체페이지 마커 반경 내의 게시글 조회 <br />• 골목길 상세페이지 게시글 및 댓글 조회, 작성 구현 <br />• 로그인 페이지, 골목길 페이지 라우팅 | • 헤더 타이틀 구현 <br />• 대처요령 페이지 조회 및 정렬 구현 <br />• 골목길 페이지 수정 및 삭제 구현 |

### 기술 스택

![여기톤-기술스택-001 (1)](https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/0505883d-699f-4fea-92bf-baf49bae0007)

### 📁 폴더구조

```
📂 2023-Herethon-15
└─ candy
 ├─ candy # project
 ├─ marker # 골목길 앱
 ├─ post # 대처요령, 사이렌 앱
 ├─ static # img, css 파일
 ├─ templates # 뼈대 템플릿
 ├─ user # 사용자 앱
 └─ manage.py
 
```

### 실행 방법

```
$ cd candy 
$ pip install -r requirements.txt
$ python manage.py runserver
```

---

### 🧷 <a href="https://bininote.notion.site/1aeaaeccf1a74b3bb7c0c4551d248d28?pvs=4">기능명세서</a>

<img width="1061" alt="스크린샷 2023-07-14 오후 11 13 58" src="https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/3d58e65e-bc7f-4628-a47e-1144915e0a2d">

### 🧷 <a href="https://www.figma.com/file/6Gk1iueT95cX6VsiNMRpb0/%EB%82%B4-%EA%B7%80%EA%B0%80-%EC%BA%94%EB%94%94?type=design&node-id=1-3&mode=design&t=HkaXFcr1CzPqSGa9-0">와이어 프레임 및 디자인</a>

<img width="794" alt="스크린샷 2023-07-14 오후 11 19 17" src="https://github.com/2023-HERETHON/2023-Herethon-15/assets/86940801/6dc75e29-6e81-4920-ac43-8e5aadac7b6a">
