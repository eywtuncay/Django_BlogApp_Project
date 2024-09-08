from django import forms
from django.forms import ValidationError
from .models import Blog
import os

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'  # Blog modelindeki tüm alanları kullan

    # Görselin uzantısını kontrol eden fonksiyon
    def clean_image(self):
        image = self.cleaned_data.get('image')  # Görsel verisini al
        ext = os.path.splitext(image.name)[1].lower()  # Dosyanın uzantısını al. [0] = dosyanın adıdır.  [1] = dosyanın adıdır. 
        valid_extensions = ['.jpg','.png']  # İzin verilen dosya uzantıları
        if ext not in valid_extensions:
            raise ValidationError(f'Yalnızca şu dosya uzantılarına izin veriliyor: {valid_extensions}')
        return image  # Eğer uzantı geçerliyse görseli döndür
