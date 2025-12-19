from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
      form = AuthenticationForm(data = request.POST)
      if form.is_valid():
         login(request, form.get_user())
         return redirect('home')
    else:
      form = AuthenticationForm()
    return render(request, 'review_app/login.html', {'form': form})
      

def register_view(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        login(request, form.get_user())
        return redirect('logout')
   else:
     form = UserCreationForm()
   return render(request, 'review_app/landingpage.html', {'form' : form})