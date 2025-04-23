from django.shortcuts import render, HttpResponse
from gestionAccount.account_management import personal_collection
from django.contrib.auth.models import User
from authentication.connexion_decorator import require_connexion

# Create your views here.

@require_connexion("personal_collection.add_w")
def persColl_add_webpage(request):
    if request.method == 'POST':

        book_id = request.POST.get('bookID')

        response = personal_collection.add(request.user,book_id)

        if response['success']:
            return render(request,
                          'personal_collection/add/webpage.html',
                          {
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
                          "added" : False,
                          })


def persColl_view_webpage(request):
    response = personal_collection.view(request.user)
    books = response["books"]

    return render(
        request,
        "personal_collection/view/all_in_one_page.html",
        {
            "books":books,
        }
    )