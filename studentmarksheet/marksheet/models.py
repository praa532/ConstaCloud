from django.db import models

# Create your models here.
class StudentData(models.Model):
    student_name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=20, unique=True)

    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    subject3 = models.CharField(max_length=50)
    subject4 = models.CharField(max_length=50)
    subject5 = models.CharField(max_length=50)

    score_subject1 = models.IntegerField()
    score_subject2 = models.IntegerField()
    score_subject3 = models.IntegerField()
    score_subject4 = models.IntegerField()
    score_subject5 = models.IntegerField()

    image = models.ImageField(upload_to='student_images/')

    student_class = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 13)])

    def total_score(self):
        return (
            self.score_subject1 +
            self.score_subject2 +
            self.score_subject3 +
            self.score_subject4 +
            self.score_subject5
        )

    def __str__(self) -> str:
        return self.student_name