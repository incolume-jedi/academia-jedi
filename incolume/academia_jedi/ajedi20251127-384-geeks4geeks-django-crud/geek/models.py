"""Models for geek."""

from django.db import models


# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
    """Models."""

    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    # renames the instances of the model with their title name
    def __str__(self):
        """Dundler str."""
        return self.title
