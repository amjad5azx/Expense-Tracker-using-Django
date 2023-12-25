from django.db import models
from django.contrib.auth.models import User

class ExpenseSource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Expense Source - {self.source_name}"


class ExpenseItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(ExpenseSource, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s {self.source.source_name} - {self.item_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update total_amount in the corresponding Expense object
        expense = Expense.objects.get(user=self.user, source=self.source)
        expense.total_amount -= self.price
        expense.save()

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(ExpenseSource, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username}'s {self.source.source_name} Expense"

    def save(self, *args, **kwargs):
        # Calculate spent_amount based on the total sum of amounts of items for the source
        total_spent_amount = ExpenseItem.objects.filter(user=self.user, source=self.source).aggregate(models.Sum('price'))['price__sum'] or 0
        self.spent_amount = total_spent_amount
        super().save(*args, **kwargs)