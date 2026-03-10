from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        print("---Зберігаємо дані користувача---")
        return redirect('')
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})