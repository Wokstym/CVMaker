from django.contrib.auth.models import User
from djongo import models


class ContactInfo(models.Model):
    city = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    phone = models.CharField(max_length=254)
    github = models.CharField(max_length=254)
    linkedin = models.CharField(max_length=254)
    personal_website = models.CharField(max_length=254)
    email = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.email


class Address(models.Model):
    street_number = models.CharField(max_length=254)
    street = models.CharField(max_length=254)
    zip = models.CharField(max_length=254)
    city = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.street_number


class University(models.Model):
    name = models.CharField(max_length=254)
    address = models.EmbeddedField(model_container=Address)


class Education(models.Model):
    start = models.CharField(max_length=254)
    end = models.CharField(max_length=254)
    field_of_study = models.CharField(max_length=254)
    degree = models.CharField(max_length=254)
    faculty = models.CharField(max_length=254)
    university = models.ArrayField(model_container=University)

    class Meta:
        abstract = True

    def str(self):
        return self.field_of_study


class Experience(models.Model):
    start = models.CharField(max_length=254)
    end = models.CharField(max_length=254)
    company = models.CharField(max_length=254)
    position = models.CharField(max_length=254)
    description = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.company


class Skills(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.name


class Interests(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.name


class Organizations(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.name


class Cv(models.Model):
    contact_info = models.ArrayField(model_container=ContactInfo)
    education = models.ArrayField(model_container=Education)
    experience = models.ArrayField(model_container=Experience)
    skills = models.ArrayField(model_container=Skills)
    languages = models.ArrayField(model_container=Languages)
    interests = models.ArrayField(model_container=Interests)
    projects = models.ArrayField(model_container=Projects)
    organizations = models.ArrayField(model_container=Organizations)
    description = models.CharField(max_length=254)

    class Meta:
        abstract = True

    def str(self):
        return self.description


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)
    current_cvs = models.ArrayField(
        model_container=Cv
    )

    objects = models.DjongoManager()
