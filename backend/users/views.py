from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            # data in dictionary
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data["username"], password=data["password"]
            )
            user.save()

            token = Token.objects.create(user=user)
            return JsonResponse({"token": str(token), "status": 201})
        except IntegrityError:
            return JsonResponse(
                {"error": "Имя пользователя занято выберете другое имя"}
            )
    else:
        return JsonResponse({"message": "Используйте POST запрос для регистрации"})
