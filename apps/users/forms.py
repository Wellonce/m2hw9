from django.forms import ModelForm, ImageField, Form, CharField, PasswordInput
from apps.books.models import Book, BookAuthor

from apps.users.models import User


class UserRegisterForm(ModelForm):
    avatar = ImageField()
    password = CharField(max_length=128, widget=PasswordInput)

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("avatar", "username", "first_name", "last_name", "middle_name", "email")


class UserLoginForm(Form):
    username = CharField(max_length=128)
    password = CharField(max_length=128, widget=PasswordInput)


class AddAuthorModelForm(ModelForm):
    avatar = ImageField()
    class Meta:
        model = BookAuthor
        fields = "__all__"


class AddBookModelForm(ModelForm):
    cover = ImageField()
    class Meta:
        model = Book
        fields = "__all__"