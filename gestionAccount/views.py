from django.shortcuts import render, HttpResponse
from gestionAccount.account_management import personal_collection
from django.contrib.auth.models import User

# Create your views here.

def persColl_add_webpage(request):
    if request.user.is_authenticated:

        if request.method == 'POST':

            book_id = request.POST.get('bookID')

            response = personal_collection.add(request.user,book_id)

            if response['success']:
                return render(request,
                              'personal_collection/add/webpage.html',
                              {
                                  "connected":True,
                                  "added" : True,
                                  "book_id": book_id,
                                  "account_name":request.user.username,
                                  "account_id": request.user.id
                              })

            else:
                return HttpResponse(f"Error {response['error']}")

        else:
            return render(request,
                              'personal_collection/add/webpage.html',
                              {
                              "connected": True,
                              "added" : False,
                              })

    else:
        return render(request,
                      'personal_collection/add/webpage.html',
                      {
                          "connected": False,
                      })
