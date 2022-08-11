import jwt
from users.models import User
from tools.R import R

def logincheck(*methods):
    def _logincheck(func):
        def wrapper(request,*args,**kwargs):
            token = request.META.get("HTTP_AUTHORIZATION")
            if request.method not in methods:
                return func(request,*args,**kwargs)
            if not token:
                return R.badRequest("no token")
            try:
                key = '895BC687BB08374C1963CFA2DEEF1F7E60A75B76DB4F4FF4D5AA2C2A3BF78891'
                res = jwt.decode(token, key, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return R.badRequest("login again")
            except Exception as e:
                return R.internalServerError("Internal Server Error")
            username = res['username']
            user = User.objects.filter(name = username)
            if not user:
                return R.badRequest("User does not exist")
            request.user = user
            return func(request,*args,**kwargs)
        return wrapper
    return _logincheck