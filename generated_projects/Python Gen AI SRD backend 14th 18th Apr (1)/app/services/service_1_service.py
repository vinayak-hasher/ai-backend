from django.core.exceptions import ValidationError

class LeaveApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(LeaveCategory, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.user is None:
            raise ValidationError("User cannot be null")
        if self.category is None:
            raise ValidationError("Category cannot be null")
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date")

    def save(self, *args, **kwargs):
        self.clean()
        super(LeaveApplication, self).save(*args, **kwargs)