from django.contrib import admin

# Register your models here.
from .models import paper,journal,author,reviewer,web,review
admin.site.register(paper)
admin.site.register(journal)
admin.site.register(author)
admin.site.register(reviewer)
admin.site.register(web)
admin.site.register(review)
