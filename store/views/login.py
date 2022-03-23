from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.pagination import Post
from django.core.paginator import Paginator
# from rest_framework import APIView

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')


            else:
                error_message = 'Email or password invalid !'

        else:
            error_message = 'Email or password invalid !'
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')

# def photo(request):
#         return render(request, 'image.html')




# def post_list(request):
#     all_post = Post.objects.all().order_by('id')
#     paginator = Paginator(all_post, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'page.html', {'page_obj':page_obj})