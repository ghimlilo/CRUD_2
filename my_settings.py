SECRET_KEY = 'django-insecure-w7i63*eplysjl-n=yrzo6mb7cyem5z939agvmgj%kp30*43td='

DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.mysql',
     'NAME': 'CRUD_2',  	# mysql database 생성시 작성한 이름
     'USER': 'root',
     'PASSWORD': 'rkskekfk13A!',	# mysql database 생성시 작성한 패스워드
     'HOST': '127.0.0.1',
     'PORT': '3306',
     'OPTIONS': {'charset': 'utf8mb4'}
 }
}
