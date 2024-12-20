from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Room
from .models import Message



def widget_chat(request):
    # Yazışma sayfasının içeriği
    return render(request, 'widget_chat.html')

def c_index(request):
    users=User.objects.all().exclude(username=request.user)

    return render(request, "chat/c_index.html", {"users":users})

# def c_index(request):
#     return render(request, "chat/c_index.html",)


def start_chat(request, username):
    second_user=User.objects.get(username=username)
    try:
        room=Room.objects.get(first_user=request.user, second_user=second_user)
    except Room.DoesNotExist:
        try:
            room=Room.objects.get(second_user=request.user, first_user=second_user)
        except Room.DoesNotExist:
            room=Room.objects.create(first_user=request.user, second_user=second_user)
    
    
    return redirect("room",room.id)



def room(request, room_name):
    users=User.objects.all().exclude(username=request.user)
    room=Room.objects.get(id=room_name)
    messages=Message.objects.filter(room=room)
    
    return render(request, "chat/roomv2.html", {
                                                "room_name": room_name,
                                                "room": room,
                                                "users":users,
                                                "messages": messages
                                                })