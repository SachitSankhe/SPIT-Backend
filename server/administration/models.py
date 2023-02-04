from django.db import models
import uuid


class Faculty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name


class Committee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    dept_head_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)
    capacity = models.IntegerField()
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    class_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    committee_id = models.ForeignKey(Committee, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
