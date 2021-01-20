from django.db import models


# Create your models here.
class BankRate(models.Model):
    date = models.DateTimeField()

    nbrb_EUR = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nbrb_USD = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nbrb_RUB = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    alfa_EUR_sell = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alfa_EUR_buy  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alfa_USD_sell = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alfa_USD_buy  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alfa_RUB_sell = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    alfa_RUB_buy  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    belarus_EUR_sell = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    belarus_EUR_buy  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    belarus_USD_sell = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    belarus_USD_buy  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    belarus_RUB_sell = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    belarus_RUB_buy  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Banks rates for {self.date}"
