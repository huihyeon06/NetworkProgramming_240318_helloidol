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
   2. urls
      1. _playgound/_ -> _say_hello()