# Echorous Server Api Docs

**url : [https://echorous.herokuapp.com](https://echorous.herokuapp.com/)**

### overview

- [**https://echorous.herokuapp.com**](https://echorous.herokuapp.com/)
    - **/card**
        - /
        - /{category}
        - /search?word=””&opt=””
    - **/achievement**
        - /
        - category/{success}
        - /{id}
    - **/user**
        - /search
        - /search/{name}
        - /save
        - /achievement
    - **/auth**
        - /register
        - /login
        - /logout

# Schema
    
    Card {
    	int id
    	String image // echorous.herokuapp.com/card/image/{id}.jpg
    	String title
    	int category 
    	// ['일반' : 0,'대기' : 1,'토양': 2,'해양' : 3,'쓰레기' : 4,'우주' : 5,'방사능' : 6]
    	int style 
    	// ['환경' : 0,'경제' : 1,'민심' : 2,'재해' : 3]
    	String description
    	int soil
    	int air
    	int radio
    	int trash
    	int ocean
    	int approval
    	int capital
    	int product
    }
    
    Achievement {
    	int id
    	String name
    	int success // ['성공': 1, '실패' : 0]
    	String description
    	int count // 업적 달성한 사람의 수
    	int soil
    	int air
    	int radio
    	int trash
    	int ocean
    	int approval
    	int capital
    	int product
    	int disaster (0,1)
    	int universe (0,1)
    	int year
    }
    
    User{
    	int id
    	String username
    	int soil
    	int air
    	int radio  
    	int trash 
    	int ocean 
    	int approval 
    	int capital 
    	int product
    	int year 
    	int success
    }
    AchievementList{
    	int id
    	int user_id (foriegn key : User)
    	int achievement_id
    	String username
    }
    AuthUser{
    	int id(auto increment)
    	String login_id(unique=True)
    	String name(not null)
    	bool is_superuser(default=False)
    	bool is_staff(default=False)
    	bool is_active(default=True)
    	Datetime created_at
    	Datetime update_at
    }
    

# **GET**

## card

[https://echorous.herokuapp.com/card](https://echorous.herokuapp.com/card)
### 전체 카드
```  
    https://echorous.herokuapp.com/card
    
    [
        {
            "id": 1,
            "image": "/echorous.herokuapp.com/card/image/1.jpg",
            "title": "방치된 쓰레기",
            "category": 4,
            "style": 0,
            "description": "거리와 공공시설에 방치된 쓰레기가 증가하여 지속적인 토양오염도 및 생물 위험도가 상승합니다",
            "soil": -2,
            "air": 0,
            "radio": 0,
            "trash": -4,
            "ocean": -1,
            "approval": -2,
            "capital": 0,
            "product": 0
        },
        {
            "id": 2,
            "image": "/echorous.herokuapp.com/card/image/2.jpg",
            "title": "태평양 거대 쓰레기 지대",
            "category": 4,
            "style": 0,
            "description": "해양생물(고래, 생선) 멸종 및 개체 수 감소, 해양오염이 증가합니다",
            "soil": 0,
            "air": 0,
            "radio": 0,
            "trash": -2,
            "ocean": -4,
            "approval": -2,
            "capital": 0,
            "product": 0
        }
    ]
```
### 카테고리별 카드 
```
    
    ['일반' : 0,'대기' : 1,'토양': 2,'해양' : 3,'쓰레기' : 4,'우주' : 5,'방사능' : 6]
    
    https://echorous.herokuapp.com/card/{category}
    
    [
        {
            "id": 88,
            "image": "/echorous.herokuapp.com/card/image/88.jpg",
            "title": "기온 역전",
            "category": 1,
            "style": 0,
            "description": "매연으로 인해 지면에 가까운 차가운 공기가 순환하기 않고 계속 바닥에 잠기게 됩니다",
            "soil": 0,
            "air": -3,
            "radio": 0,
            "trash": 0,
            "ocean": 0,
            "approval": 0,
            "capital": 0,
            "product": 0
        },
        {
            "id": 89,
            "image": "/echorous.herokuapp.com/card/image/89.jpg",
            "title": "스모그 사태",
            "category": 1,
            "style": 0,
            "description": "기온 역전 현상이 심화되어 스모그 사태가 발생합니다, 일부의 시민들이 극심한 고통을 호소합니다",
            "soil": 0,
            "air": -7,
            "radio": 0,
            "trash": 0,
            "ocean": 0,
            "approval": -3,
            "capital": 0,
            "product": 0
        }
    ]
 ```
### keyword별 카드
```    
    https://echorous.herokuapp.com/card/search?word=””&opt=””
    
    opt : [0:제목,1:내용,2:둘다]
    
    word없으면 오류남
    
    // url : https://echorous.herokuapp.com/card/search?word=오염&opt=0
    [
        {
            "id": 94,
            "image": "/echorous.herokuapp.com/card/image/94.jpg",
            "title": "오존 오염",
            "category": 1,
            "style": 0,
            "description": "쓰레기 소각장, 탄소 연소, 화학산업 단지의 지속적인 사용으로 오존이 오염됩니다",
            "soil": 0,
            "air": -5,
            "radio": 0,
            "trash": 0,
            "ocean": 0,
            "approval": 0,
            "capital": 0,
            "product": 0
        },
        {
            "id": 95,
            "image": "/echorous.herokuapp.com/card/image/95.jpg",
            "title": "대기오염의 경각심",
            "category": 1,
            "style": 0,
            "description": "WHO의 추정에 따르면 매년 420,0000명이 대기오염으로 사망하고 있다는 사실을 알려 시민들의 경각심을 돋굽니다",
            "soil": 0,
            "air": 0,
            "radio": 0,
            "trash": 0,
            "ocean": 0,
            "approval": 4,
            "capital": 0,
            "product": 0
        }
    ]
 ```   

## achievement

https://echorous.herokuapp.com/achievement

### 모든 업적
https://echorous.herokuapp.com/achievement
```
    
    [	
    	{
            "id": 1,
            "name": "올라운더",
            "success": 1,
            "description": "모든 분야 오염도 15% 미만 달성",
            "count": 0,
            "soil": 15,
            "air": 15,
            "radio": 15,
            "trash": 15,
            "ocean": 15,
            "approval": 0,
            "capital": 0,
            "product": 0,
            "disaster": 0,
            "universe": 0,
            "year": 0
        },
        {
            "id": 2,
            "name": "미래지향적 국가",
            "success": 1,
            "description": "모든 분야 오염도 25%미만 달성 & 지지도 80이상 달성",
            "count": 0,
            "soil": 25,
            "air": 25,
            "radio": 25,
            "trash": 25,
            "ocean": 25,
            "approval": 80,
            "capital": 0,
            "product": 0,
            "disaster": 0,
            "universe": 0,
            "year": 0
        }
    ]
```
    
### 성공/실패 별 업적
https://echorous.herokuapp.com/achievement/category/{success}
success : [성공 : 1, 실패 : 0] 
```   
    [	
    		{
            "id": 9,
            "name": "콜록콜록",
            "success": 0,
            "description": "오염100% 달성 &모든 오염 수치 80% 이상 달성",
            "count": 0,
            "soil": 100,
            "air": 100,
            "radio": 100,
            "trash": 100,
            "ocean": 100,
            "approval": 0,
            "capital": 0,
            "product": 0,
            "disaster": 0,
            "universe": 0,
            "year": 0
        },
        {
            "id": 10,
            "name": "콜록콜록",
            "success": 0,
            "description": "오염100% 달성 &모든 오염 수치 80% 이상 달성",
            "count": 0,
            "soil": 80,
            "air": 80,
            "radio": 80,
            "trash": 80,
            "ocean": 80,
            "approval": 0,
            "capital": 0,
            "product": 0,
            "disaster": 0,
            "universe": 0,
            "year": 0
        }
    ]
```
    
### id별 업적
https://echorous.herokuapp.com/achievement/category/{id}
```    
    
    {
        "id": 1,
        "name": "올라운더",
        "success": 1,
        "description": "모든 분야 오염도 15% 미만 달성",
        "count": 0,
        "soil": 15,
        "air": 15,
        "radio": 15,
        "trash": 15,
        "ocean": 15,
        "approval": 0,
        "capital": 0,
        "product": 0,
        "disaster": 0,
        "universe": 0,
        "year": 0
    }
```
    

### user

https://echorous.herokuapp.com/user

### 유저 전체 상황
http://echorous.herokuapp.com/user/search
```  
    [
        {
            "id": 1,
            "username": "윤성",
            "soil": 50,
            "air": 50,
            "radio": 50,
            "trash": 50,
            "ocean": 50,
            "approval": 50,
            "capital": 50,
            "product": 50,
            "year": 50,
            "success": 0
        }
    ]
```
    
### 세부 유저 상황
http://echorous.herokuapp.com/user/search/{username}
```  
    {
        "User": {
            "id": 1,
            "username": "윤성",
            "soil": 50,
            "air": 50,
            "radio": 50,
            "trash": 50,
            "ocean": 50,
            "approval": 50,
            "capital": 50,
            "product": 50,
            "year": 50,
            "success": 0
        },
        "AchievementArray": [
            {
                "title": "올라운더",
                "description": "모든 분야 오염도 15% 미만 달성",
                "success": 1
            },
            {
                "title": "미래지향적 국가",
                "description": "모든 분야 오염도 25%미만 달성 & 지지도 80이상 달성",
                "success": 1
            }
        ]
    }
```
# POST

### auth
https://echorous.herokuapp.com/auth

### 회원가입
https://echorous.herokuapp.com/auth/register
   
    **request**
    ```
    {
        "login_id":"dbstjd1659",
        "name":"yunsung",
        "password":"1234"
    }
    ```
    
    **response**
    
    json형식 다른 경우에는 400_bad_request 
    
    ```
    "user": {
            "id": 3,
            "password": "pbkdf2_sha256$320000$2bVYYHtUE1t1SosSdAIKVN$xeSh/tDmJWhvJg+MIcPGjto33VG/m+kAI8Fkk4GXjnU=",
            "last_login": null,
            "login_id": "dbstjd1659",
            "name": "yunsung",
            "is_superuser": false,
            "is_staff": false,
            "is_active": true,
            "created_at": "2022-08-20T09:00:16.725162Z",
            "updated_at": "2022-08-20T09:00:16.725196Z",
            "groups": [],
            "user_permissions": []
        },
        "message": "register success",
        "token": {
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwOTkzMjE2LCJpYXQiOjE2NjA5ODYwMTYsImp0aSI6ImUwNzI0YmVkNDMzNjRiY2JiZDgxOGU1NDQ3MGMyMjJiIiwidXNlcl9pZCI6M30.ER2TJF1yVlEKy5OVKggtofL1lRsRL3i7zwowSOtkJIA",
            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTU5MDgxNiwiaWF0IjoxNjYwOTg2MDE2LCJqdGkiOiIxYjlkNWUzMWI4NTQ0YThmOTUyZWEzYWZkZjRkYTk5OCIsInVzZXJfaWQiOjN9.DEi0WJmumo-VWwZ4OU00ZwfU7aDu6asu0CB86fgJH9k"
        }
    }
    ```
    
### 로그인
https://echorous.herokuapp.com/auth/login
    
**request**
    
```
{
    "login_id":"dbstjd0924",
    "password":"1234"
}
```
    
**response**
    
```
    {
        "user": {
            "id": 1,
            "password": "pbkdf2_sha256$320000$PozrwUVG3dHoMOfFZQRGtg$MfL+glCeC7p0Y+OZvN+zUY6+fqHpPP1vrsdBXtkbOBY=",
            "last_login": null,
            "login_id": "dbstjd0924",
            "name": "장윤성",
            "is_superuser": false,
            "is_staff": false,
            "is_active": true,
            "created_at": "2022-08-18T16:40:24.424724Z",
            "updated_at": "2022-08-18T16:40:24.424724Z",
            "groups": [],
            "user_permissions": []
        },
        "message": "login success",
        "token": {
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwOTkzMzM3LCJpYXQiOjE2NjA5ODYxMzcsImp0aSI6IjUyZWI2ZTRjMWIzZjRmNDhiZmRhZDc3ZDlkNWMxYzkwIiwidXNlcl9pZCI6MX0.zdC_W0IuzUfeDWUrzZ_ifh-t-wds3e0-9h3czG_FKnw",
            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTU5MDkzNywiaWF0IjoxNjYwOTg2MTM3LCJqdGkiOiI4YzQ2MDNiNjdlOGI0MzU5OTk2ZDRkYzQ1Nzc5OWY2OCIsInVzZXJfaWQiOjF9.Yn5N6oAIaX0soIJN4TextFxhyHEuzgmkuCsB9Nymj0I"
        }
    }
```
    
## 로그아웃
    
https://echorous.herokuapp.com/auth/logout
**request**
    
```
    {
        "login_id":"dbstjd0924",
        "password":"1234"
    }
```
    
**response**
    
```
    {
        "message": "Logout success"
    }
```
    

## user

https://echorous.herokuapp.com/user

### 유저 현재 상태 저장   
https://echorous.herokuapp.com/user/save    
**request**    
```
    {
        "username":"윤성",
        "soil":50,
        "air":50,
        "radio":50,
        "trash":50,
        "ocean":50,
        "approval":50,
        "capital":50,
        "product":50,
        "year":50,
        "success":0
    }
    
```
**response**
    
이미 저장을 한 상태에서는 update된다.
    
데이터가 올바른 형식으로 들어가지 않은 경우에 error code 400(bad request) 발생
    
```
    // 올바르게 들어갔을 경우
    {
        "username":"윤성",
        "soil":50,
        "air":50,
        "radio":50,
        "trash":50,
        "ocean":50,
        "approval":50,
        "capital":50,
        "product":50,
        "year":50,
        "success":0
    }
```
### 유저 현재 업적 상태 저장
    
https://echorous.herokuapp.com/user/achievement
    
**request**
    
```
    {
        "username":"윤성",
        "user_id":0, // user_id는 아무값이나 넣어주면 된다
        "achievement_id":3
    }
```
    
**response**
    
username이 없는 경우에는 404 not found를 내보낸다.
    
업적이 저장되지 않은 경우에는 400 bad request를 내보낸다.
```
    {
      "id":1
      "user_id":1, // username의 id를 저장해놓는다.
      "achievement_id":3
    }
```
