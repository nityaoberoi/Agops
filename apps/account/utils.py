from django.contrib.auth.models import User


def generate_user(email, password=None):
    username = email
    if not password:
        user = User.objects.create(username=username,
                                    email=email)
    else:
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
    return user
