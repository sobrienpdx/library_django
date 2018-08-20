from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book


def index(request):
	if request.user.is_authenticated:
		username = request.user.username
	else: username = "x"
	book_list = Book.objects.all()
	result = ""
	context = {'book_list': book_list, 'search_result': result, "username": username}
	print("hello!")
	return render(request, 'library_app/index.html', context)


def search_books(request):
	if request.method == 'GET':
		print("you called search_book")
		search_query = request.GET['search_box']
		searched_books = []
		titles = Book.objects.filter(title__icontains=search_query)
		first_names =Book.objects.filter(author__first_name__icontains=search_query)
		last_names = Book.objects.filter(author__last_name__icontains=search_query)
		searched_books.extend(titles.union(first_names, last_names))
		# searched_book.append(Book.objects.filter(author=search_query))
		print(f'the book you looked for is {searched_books}')
		context = {'book_list': searched_books}
		return render(request, 'library_app/index.html', context)


def checkout(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			username = request.user.username
			for book in request.POST:
				print(book)
				if book.startswith('book_'):
					book_id = book[5:]
					print(book_id)
					booky = Book.objects.get(id=book_id)
					if booky.checked_out_to_whom == "":
						booky.checked_out_to_whom=username
						booky.save()
					else: return HttpResponse(f'{booky.title} is already checked out to someone else. Nice try, hacker!')
					print(f'you checked out {booky}')
			return redirect('library_app:my_checkouts')
			return HttpResponse(f'so far it works. you can do it! PS the username was {username}')
		else:
			return HttpResponseRedirect('library_project:accounts/logout')


def my_checkouts(request):
	if request.user.is_authenticated:
		username = request.user.username
		my_checkouts = Book.objects.filter(checked_out_to_whom=username)
		print(my_checkouts)
		context = {'my_checkouts': my_checkouts, 'username': username}
		return render(request, 'library_app/my_checkouts.html', context)
	else:
		return HttpResponse('checkouts! oh yeah!')

def return_books(request):
	for book in request.POST:
		print(book)
		if book.startswith('book_'):
			book_id = book[5:]
			print(book_id)
			booky = Book.objects.get(id=book_id)
			booky.checked_out_to_whom=""
			booky.save()
			return redirect('library_app:my_checkouts')
	return HttpResponse('get ye back to the library')
