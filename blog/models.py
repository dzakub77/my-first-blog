from django.db import models
from django.utils import timezone
# dokumentacja django - wiecej o polach modelu
class Post(models.Model): #models.Model oznacza ze nasz obiekt Post jest modelem Django. Dzieki temu Django wie ze ma go przychowywac w bazie danych
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #to jest odnosnik do innego moodelu
    title = models.CharField(max_length=200) # tak definiujemy tekst z ograniczona liczba znakow
    text = models.TextField() # TextField() nadaje sie do dluzszych tekstow bez ograniczen
    created_date = models.DateTimeField( # data i godzina
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # matoda publikująca wpis
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title