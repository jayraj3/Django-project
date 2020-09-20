from django.http import HttpResponse



def sessfun(request) :
    oldval = request.COOKIES.get('dj4e_cookie', '4dc3ed26')
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    response = HttpResponse('view count='+str(num_visits)+ str(oldval))
    response.set_cookie('dj4e_cookie', '4dc3ed26', max_age=1000)
    return response

