import datetime
import jwt
from django.conf import settings
from ..models import Users





def authCheck(request):
    authorization = request.META.get('HTTP_AUTHORIZATION', None)
    if authorization == None:
        return 'Authentication credentials were not provided.'
    else:
        authorization = authorization.replace('JWT ','')
        token = Users.objects.filter(token=authorization)
        if len(token) > 0:
            for uId in token:
                userId = uId.user_id
            return userId
        else:
            return 'Authentication token invalid'

def checkSuperAdmin(userId):
    checkUser =Users.objects.filter(id=userId)
    if len(checkUser) == 1 : 
        getUser = Users.objects.get(id=userId)
        user_type = getUser.user_type 

        if str(user_type) == "SUPERADMIN" :  
            return "SUPERADMIN"
        else :
            msg = "You don'nt have enough rights"
            print(msg)        
            return msg
    else :
        return "Invalid user"