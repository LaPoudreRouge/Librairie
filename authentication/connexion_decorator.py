from django.shortcuts import render




def require_connexion(redirect_url:str):
    """
    check if the user is connected and ask to log in with a redirect.

    :param str redirect_url:
    :return:
    """

    def decorator(func):
        def wrapper(*args,**kwargs):
            request = args[0]
            if request.user.is_authenticated:
                return func(*args,**kwargs)
            else:
                return render(
                    request,
                    "connexion_required_webpage.html",
                    {
                        "redirect_url":redirect_url
                    }
                )
        return wrapper
    return decorator