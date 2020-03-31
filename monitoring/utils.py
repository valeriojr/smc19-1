from .models import ActionLog

def create_log(request, action, model):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    user = request.user
    ActionLog(action = action, model = model, user = user, ip = ip).save()