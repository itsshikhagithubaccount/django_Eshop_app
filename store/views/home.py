from django.shortcuts import render,redirect,HttpResponse
from store.models.product import Product,Post1
from store.models.category import Category
from store.serializers import Post1Serializer,ProductSerializer
from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated




class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart :
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1

            else:
                cart[product] =1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('homepage')

    def get(self , request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
            # set pagination
            p = Paginator(Product.get_all_products(),2)
            page = request.GET.get('page')
            products = p.get_page(page)

        data = {}
        data['products'] = products
        data['categories'] = Category.get_all_categories()

        print('you are', request.session.get('email'))
        return render(request, 'index.html', data)


def search(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains=query)
    params = {'products': products}
    return render(request,'search.html',params)
    # return HttpResponse('this is search')


class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        qs = Post1.objects.all()
        post = qs.first()
        serializer = Post1Serializer(post)
        # serializer = Post1Serializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = Post1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)





# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }
#     return JsonResponse(data)