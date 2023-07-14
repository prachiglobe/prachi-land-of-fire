from django.shortcuts import redirect, render, HttpResponse
from .models import Book

# Create your views here.

# FBV-- Function based views

def welcome_page(request):   #http request
    # return HttpResponse("welcome to the library Application")
    return render(request, "welcome.html")

import datetime
def show_all_books(request):
    books = Book.objects.filter(is_active=True)# get only active data
    return render(request, "showbooks.html" , {"allbooks": books,"today":datetime.datetime.now()})

def show_single_book(request, bid):
    try:
        book_obj = Book.objects.get(id=bid)
    except Book.DoesNotExist:
        return HttpResponse("Book does not exixt...!")
    return render(request=request, template_name="bookdetails.html", context={"book":book_obj})

def common_var(req):
       final_dict = req.POST
       book_name = final_dict.get("nm")
       book_price = final_dict.get("prc")
       book_qty = final_dict.get("qty")
       book_is_pub = final_dict.get("ispub")
       return book_name, book_price, book_qty, book_is_pub


def add_single_book(request):
    if request.method == "POST":
       book_name, book_price, book_qty, book_is_pub = common_var(request)
       if book_is_pub == "YES":
           is_pub = True
       else:
           is_pub = False
        
       Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub)
       return redirect("show_books")

    elif request.method == "GET":
        return render(request, "addbook.html")

    
def edit_single_book(request, bid):
    book_obj =Book.objects.get(id=bid)
    if request.method == "GET":
     return render (request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        book_name, book_price, book_qty, book_is_pub = common_var(request)
        if book_is_pub == "YES":
           is_pub = True
        else:
           is_pub = False
        
        book_obj.name= book_name
        book_obj.price= book_price
        book_obj.qty= book_qty
        book_obj.is_published= is_pub
        book_obj.save()
        return redirect("show_books")



def delete_single_book(request, bid):
    book_obj =Book.objects.get(id=bid)
    book_obj.delete()
    return redirect("show_books")

def soft_delete_single_book(request, bid):
    book_obj =Book.objects.get(id=bid)
    book_obj.is_active= False
    book_obj.save()
    return redirect("show_books")

# -------------------------------------------------------------------------

from .forms import GeeksForm, BookForm, AddressForm

# create your views

def form_view(request):
   if request.method == "POST":
      print("in post request")
      data = request
      print(data)
      return HttpResponse("Okay")
   elif request.method == "GET":
    print("get request")
    return render(request, "book_form_test.html", {"bookform": BookForm()})
   
    
   elif request.method == "GET":
       print("get request")


# def form_view(request):
#     # print(GeeksForm())
#     return render(request, "form_text.html", {"form": AddressForm()})




import requests
# GET_SINGLE_STUD_URL = "http://127.0.0.1:8000/api/get-student_2/{}/"
GET_ALL_STUDS = "http://127.0.0.1:8000/api/get-all-students_2/"
# CREATE_STUD = "http://127.0.0.1:8000/api/create-student_2/"



def get_all_student_2(request):
    # response = requests.get(GET_ALL_STUDS)
    response = requests.request("GET", GET_ALL_STUDS)
    python_dict = response.json()
    return render(request, "student_data.html", {"data": python_dict}) 








# <!-- <form method="post"> -->
#     <!-- {% csrf_token %} -->
#     <!-- {{ form|crispy }}
#     <button type="submit" class="btn btn-primary">Submit</button> -->
#   <!-- </form> -->
#   <!-- <div class="form-row">
#      <div class="form-group col-md-6 mb-0">
#        {{ form.email|as_crispy_field }}
#      </div>
#      <div class="form-group col-md-6 mb-0">
#       {{ form.password|as_crispy_field }}
#     </div>
#   </div> 
#   {{ form.address_1|as_crispy_field }}
#   {{ form.address_2|as_crispy_field }}
#   <div class="form-row">
#     <div class="form-group col-md-6 mb-0">
#       {{ form.city|as_crispy_field }}
#     </div>
#     <div class="form-group col-md-4 mb-0">
#       {{ form.state|as_crispy_field }}
#     </div>
#     <div class="form-group col-md-2 mb-0">
#       {{ form.zip_code|as_crispy_field }}
#     </div>
#   </div>
#   {{ form.check_me_out|as_crispy_field }}
#   <button type="submit" class="btn btn-primary">Sign in</button>
# </form> -->




