from django.db import models
class Principal(models.Model):
    descricao_text = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao_text
    objects = models.Manager()


class Submenu(models.Model):
    principal = models.ForeignKey(Principal, on_delete=models.CASCADE)
    descricao_text = models.CharField(max_length=200)

