from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.middleware import csrf
from .forms import ContactForm, SearchForm
from .models import BookContact
from django.template.context_processors import csrf

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/login')
            else:
                return redirect('/signup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout(request):
    return redirect('showLogout')

def showLogout (request):
    t = get_template('registration/logout.html')
    html = t.render()
    response = HttpResponse(html)
    response.delete_cookie('user_name')
    return response

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            t = get_template('a1.html')
            html = t.render({'username':username})
            response = HttpResponse(html)
            response.set_cookie('user_name', username)
            return response
        else:
            return HttpResponse("NOT  Valid User")
    else:
        user_name = request.COOKIES['user_name']
        t = get_template('a1.html')
        html = t.render({'username': user_name})
        return HttpResponse(html)

def getUserFromSessions (request):
    SESSION_KEY = '_auth_user_id'
    BACKEND_SESSION_KEY = '_auth_user_backend'
    from django.contrib.auth import load_backend
    user_id = request.session[SESSION_KEY]
    backend_path = request.session[BACKEND_SESSION_KEY]
    backend = load_backend(backend_path)
    return  backend.get_user(user_id)

def search (request):
    form_class = SearchForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            searchCategoryID  = request.POST.get( 'searchCategory', '')
            category = [
                        'firstName','lastName',
                        'mobile','email',
                        'contactAdress'
            ]
            searchCategory = category[int(searchCategoryID) - 1]
            searchString = request.POST.get('searchString', '')
            if 'user_name' in request.COOKIES:
                user_name = request.COOKIES['user_name']
                tmp = { }
                tmp [searchCategory + '__contains'] = searchString
                tmp['userName'] = user_name
                tmp['is_active'] = 1
                çontacts = { 'contacts': BookContact.objects.filter(**tmp),'username':request.COOKIES['user_name'] }
                t = get_template('contact_list.html')
                html = t.render(çontacts)
                return HttpResponse(html)
    return render(request, 'search_contact.html', {'form': form_class,'username':request.COOKIES['user_name']})

def add(request):
    form_class = ContactForm
    obj = BookContact()
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            firstName  = request.POST.get( 'firstName', '')
            lastName = request.POST.get('lastName', '')
            mobile  = request.POST.get('mobile', '')
            email = request.POST.get('email', '')
            contactAdress = request.POST.get('contactAdress', '')
            if 'user_name' in request.COOKIES:
                user_name = request.COOKIES['user_name']
                obj = BookContact()
                obj.userName = user_name
                obj.firstName = firstName
                obj.lastName = lastName
                obj.mobile = mobile
                obj.email = email
                obj.contactAdress = contactAdress
                obj.is_active = 1
                obj.save()
                t = get_template('add_confirm.html')
                html = t.render({'message':"add",'username':request.COOKIES['user_name']})
                return HttpResponse(html)
    return render(request, 'contact_add.html', {'form': form_class,'username':request.COOKIES['user_name']})

def list(request):
    user_name = request.COOKIES['user_name']
    çontacts = {
                'contacts': BookContact.objects.filter(userName=user_name,is_active=1),
                'username':request.COOKIES['user_name']
    }
    t = get_template('contact_list.html')
    html = t.render(çontacts)
    return HttpResponse(html)


def modify(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        contactAdress = request.POST.get('contactAdress', '')
        çontacts = BookContact.objects.filter().get(userId=id)
        çontacts.firstName = firstName
        çontacts.lastName = lastName
        çontacts.mobile = mobile
        çontacts.email = email
        çontacts.contactAdress = contactAdress
        çontacts.save()
        t = get_template('add_confirm.html')
        html = t.render({'message': "modify",'username':request.COOKIES['user_name']})
        return HttpResponse(html)
    else:
        id = request.GET.get('id', '')
        çontacts =  BookContact.objects.filter().get(userId=id)
        contact = {
            'firstName':çontacts.firstName,
            'lastName':çontacts.lastName,
            'mobile':çontacts.mobile,
            'email':çontacts.email,
            'contactAdress':çontacts.contactAdress,
            'userId':çontacts.userId,
            'csrfmiddlewaretoken': get_or_create_csrf_token(request),
            'username': request.COOKIES['user_name']
        }
        t = get_template('contact_modify.html')
        html = t.render(contact)
        return HttpResponse(html)

def delete(request):
    id = request.GET.get('id', '')
    çontacts = BookContact.objects.filter().get(userId=id)
    çontacts.is_active = 0
    çontacts.save()
    t = get_template('add_confirm.html')
    html = t.render({'message': "delete",'username':request.COOKIES['user_name']})
    return HttpResponse(html)

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_key()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token