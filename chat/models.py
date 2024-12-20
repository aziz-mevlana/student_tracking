import uuid

from django.db import models
from django.contrib.auth.models import User

# message model, room model


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_user=models.ForeignKey(User,related_name="room_first",on_delete=models.CASCADE, null=True) #!null olmamali
    second_user=models.ForeignKey(User,related_name="room_second",on_delete=models.CASCADE, null=True) #!null olmamali
# class ChatUser(models.Model): #?Grup Konusmasi icin sonradan duzenlenebilir
#     user = models.ForeignKey(User, related_name="chat_user", verbose_name="Kullanıcı", on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, related_name="chat_users", verbose_name="Oda", on_delete=models.CASCADE)

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", verbose_name="Kullanıcı", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="messages", verbose_name="Oda", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Mesaj İçerği")
    created_date = models.DateTimeField(auto_now_add=True)
    what_is_it=models.CharField(max_length=50,null=True)
    
    def get_short_date(self):
        return str(self.created_date.hour)+":"+str(self.created_date.minute)