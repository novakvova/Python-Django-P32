
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        # print("---Зберігаємо дані користувача---")
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            messages.success(request, 'Виправте помилки у формі')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})