from django.contrib import admin
from socialregistration.models import (FacebookProfile, TwitterProfile, FoursquareProfile,
    OpenIDProfile, OpenIDStore, OpenIDNonce)

admin.site.register([FacebookProfile, TwitterProfile, FoursquareProfile, OpenIDProfile, OpenIDStore, OpenIDNonce])


