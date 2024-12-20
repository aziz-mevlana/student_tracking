from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import Profile
    

@login_required
def verify_account(request):
    if request.user.profile.is_verified:
        return redirect("home")
    
    if request.method == "POST":
        entered_code = request.POST.get("verification_code")
        correct_code = request.user.profile.token
        
        if entered_code == correct_code:
            request.user.profile.is_verified = True
            request.user.profile.save()
            return redirect('home')  # Doğrulama tamamlandığında anasayfaya yönlendir
        
        else:
            return render(request, 'verification.html', {
                "error_message": "Geçersiz doğrulama kodu. Lütfen tekrar deneyin."
            })
    return render(request, 'verification.html')




def login_request(request):
    if request.user.is_authenticated:#? Kullanici giris yapmis ise login paneline eriesemesin anasayfaya gitsin
        return redirect("home")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect ("verify_account")
        else:
            return render(request, "account/login.html", {
                "error": "Kullanıcı adı veya şifre hatalı"
            })
        
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:#? Kullanici giris yapmis ise register paneline eriesemesin anasayfaya gitsin
        return redirect("home")
    
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(email=email).exists():
                return render(request, "account/register.html", 
                {
                    "error": "Email zaten alınmış",
                    "email" : email,
                })
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                profile = Profile.objects.get(user=user)  # 'user' burada bir User nesnesidir
                token = profile.token  # Profile nesnesindeki token alanına erişim
                
                send_mail(
                            "Subject here",
                            "Here is the {}.".format(token),
                            "aziz-alim@hotmail.com",
                            [user.email],
                            fail_silently=False,
                          )
                return redirect("login")
        else:
            return render(request, "account/register.html", 
            {
                "error": "Şifreler eşleşmiyor",
                "email" : email,
            })
    
    
    
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")



def profile_request(request):
    return render(request, "account/profile.html")