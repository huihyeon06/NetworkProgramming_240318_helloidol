# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2 (~=는 4.2의 최신버전을 설치 ==는 4.2를 설치 )
      1. pip list (설치된 list를 볼 수 있다)
   2. django-admin startproject _helloidol_ .
   3. [python manage.py migrate] 
      1. 바로 python manage.py migrate runserver 하면 manage.py만들고 runserver함
   4. python manage.py runserver
   5. File => settings => language => django 에 project root와 settings 경로 찾기
2. startapp _playground_
   1. Terminal
      1. python manage.py startapp _playground_
   2. helloido/settings.py
      1. 'playgournd', in INSTALLED_APPS
3. playgound/
   - 정보 전달 : urls -> views -> (models -> ) templates
   - 코드 작성 : (models -> ) views -> templates -> urls
   1. views
      1. _say_hello()_
      2. _say_hello_html()_
      3. _say_bye_html()_
   2. urls
      1. _playground/hello/_ -> _say_hello()
      2. _playground/hello_html/_ -> _say_hello_html()_
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, playground/urls
      1. _playground/_ -> _hello/_ -> _say_hello()_
      2. _playground/_ -> _hello_html/_ -> _say_hello_html()_
      3. _playground/_ -> _bye_html/_ -> _say_bye_html()_
---
5. startapp 투바투
   1. Terminal
      1. python manage.py startapp 투바투
   2. helloidol/settings.py
      1. '투바투', in INSTALLED_APPS
   3. 투바투/
      1. views
         1. ~~show_수빈()~~
         2. ~~show_태현()~~
         3. ~~show_연준()~~
         4. ~~show_범규()~~
         5. ~~show_휴닝()~~
         6. -> templates에 context 전달
         7. 정보를 하나로 묵고, 거기서 꺼내오자
         8. show_멤버()
         9. image link -> image file(static)
         10. show_멤버리스트()
      2. templates/투바투/
         1. ~~수빈.html~~
            1. title : 투바투 - 수빈
            2. h1 : 투바투
            3. h2 : 수빈
            4. img : 수빈 프로필 사진
               1. border-radius: 50%;
         2. ~~연준.html~~
         3. 멤버.html
            1. group_name, name, img_src
            2. {% load static %} <img src="{% static img_src %}">
         4. 멤버리스트.html
      3. urls
         1. ~~투바투/ -> 수빈/ -> show_수빈()~~
         2. ~~투바투/ -> 태현/ -> show_태현()~~
         3. ~~투바투/ -> 연준/ -> show_연준()~~
         4. ~~투바투/ -> 범규/ -> show_범규()~~
         5. ~~투바투/ -> 휴닝/ -> show_휴닝()~~
         6. 투바투/ -> <멤버>/ -> show_멤버(멤버)
         7. 투바투/ -> 멤버리스트/ -> show_멤버리스트()
      4. static/투바투/images/
         1. 치이카와.jpg, 수빈.png, 연준.png