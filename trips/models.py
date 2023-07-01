from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)               #標題
    content = models.TextField(blank=True)                 #內文
    photo = models.URLField(blank=True)                    #照片網址
    location = models.CharField(max_lenth=100)             #地點
    created_at = models.DateTimeField(auto_now_add=True)   #建立時間

    #CharField -- 字串欄位，適合像 title、location 這種有長度限制的字串。
    #TextField -- 適合放大量文字的欄位
    #URLField -- URL 設計的欄位
    #DateTimeField -- 日期與時間的欄位，使用時會轉成 Python datetime 型別

    #max_length=100 -- 標題不可以超過 100 個字元
    #blank=True -- 非必填欄位（表單驗證時使用），預設所有欄位都是 blank=False
    #auto_now_add=True -- 物件新增的時間。若想設成物件修改時間，則用 auto_now=True