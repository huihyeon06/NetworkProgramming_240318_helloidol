# helloidol

---

1. startproject helloidol
   1. python -m pip install django~=4.2 (~=는 4.2의 최신버전을 설치 ==는 4.2를 설치 )
      1. pip list (설치된 list를 볼 수 있다)
   2. django-admin startproject helloidol .
   3. [python manage.py migrate] 
      1. 바로 python manage.py migrate runserver 하면 manage.py만들고 runserver함
   4. python manage.py runserver
   5. File => settings => language => django 에 project root와 settings 경로 찾기