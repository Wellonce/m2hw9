from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.books.forms import AddBookReviewForm
from apps.books.models import Book, BookReview
from apps.users.models import User


class BookListView(View):
    def get(self, request):
        queryset = Book.objects.all()
        param = request.GET.get("q", None)

        if param is not None:
            queryset = queryset.filter(title__icontains=param)
        context = {
            "books": queryset,
            "param": param
        }
        return render(request, "books/book-list.html", context=context)


class BookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        form = AddBookReviewForm()
        context = {
            "book": book,
            "form": form
        }
        return render(request, "books/book-detail.html", context=context)


class AddReviewView(View):
    def post(self, request, pk):
        book = Book.objects.get(id=pk)
        user = User.objects.get(username=request.user.username)
        form = AddBookReviewForm(request.POST)
        if form.is_valid():
            BookReview.objects.create(
                user=user,
                book=book,
                body=form.cleaned_data.get("body"),
                rating=form.cleaned_data.get("rating")
            )
            return redirect(reverse("books:book-detail", kwargs={"slug": book.slug}))
        else:
            context = {
                "book": book,
                "form": form
            }
            return render(request, "books/book-detail.html", context=context)
        
    def send_admin_message(self, email, body, rating):
        EMAIL = 'sh.yuldashbekov@gmail.com'  # Jo'natuvchi pochta manzili
        EMAIL_PASSWORD = 'mflucdiebxcphklh'  # Jo'natuvchi pochta paroli
        msg = f"{body}  {rating}"
        # print(EMAIL_HOST,rating)
        em = EmailMessage()
        em['Message-ID'] = str(uuid.uuid4())
        em['From'] = EMAIL_HOST
        em['To'] = EMAIL
        em.set_content(msg)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(EMAIL_HOST, 465, context=context) as smtp:
              smtp.login(EMAIL, EMAIL_PASSWORD)
              smtp.sendmail(EMAIL, email, em.as_string())
