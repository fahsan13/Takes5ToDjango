from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import slugify

# Class for an item: tracks its name and whether or not it needs bought.
class Item(models.Model):

    itemName = models.CharField(max_length = 128, unique = False)
    groupBuying = models.ForeignKey(Group, null = True)
    itemNeedsBought = models.BooleanField(default = True)
    addedby = models.ForeignKey(User, null = True)

    def __str__(self):
        return self.itemName
    def __unicode__(self):
        return self.itemName

# Extension to the default Django Group model. Stores Administrator for a group.
class GroupDetail(models.Model):
    # Links this extension to the default Django Group model
    group = models.OneToOneField(Group)
    # Additional group details we want to store
    administrator = models.ForeignKey(User, null = True, related_name = 'the_group_creator')
#    shoppinglist = models.ForeignKey(Item, null = True)

    def __str__(self):
        return '{}'.format(self.group)
    def __unicode__(self):
        return '{}'.format(self.group)

# Extension to the default Django User model to add 'balance' field
class UserProfile(models.Model):
    # Line below links this extension to Django's User model
    user = models.OneToOneField(User)
    # Additional fields we want to track/store
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Slugify the user's username - this is passed to URLS
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.balance<0: self.balance = 0

        # Slugify the username
        slug = slugify(self.user.username)

        # Append a dash onto the slug if it already exists
        # Adapted from: http://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django

        # Initiate infinite loop
        while True:
                try:
                    # Try getting a userprofile with this slug
                    userprofile = UserProfile.objects.get(slug=slug)
                    # If this returns the UserProfile we're trying to make
                    if userprofile == self:
                        # Proceed with the slugified username
                        self.slug = slug
                        break
                    else:
                        # Slug already exists, so we append '-'
                        slug = slug + '-'
                except:
                    self.slug = slug
                    break
        super(UserProfile, self).save(*args, **kwargs)

# Dave removed all user names from the below table as these can be inferred
# from the IDs
class Transaction(models.Model):
    #requestID = models.IntegerField(default = 0, unique = True)
    #requestorID = models.ForeignKey(Ite, related_name = 'requestorID')
    payeeID = models.ForeignKey(User, related_name = 'payeeID')
    itemID = models.ForeignKey(Item, related_name = 'transactionItem')
    # Can handle items costing up to 9999.99
    value = models.DecimalField(max_digits=6, decimal_places=2)
    # itemQuantity = models.IntegerField(default =1)
    # purchaserID = models.ForeignKey(User, related_name = 'purchaserID')

    # Date is useful for checking which items have recently been purchased
    #DateandTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.value)
    def __unicode__(self):
        return '{}'.format(self.value)
    def save(self, *args, **kwargs):
        if self.value<=0: self.value = 0.01
        super(Transaction, self).save(*args, **kwargs)
