from django.contrib import admin
from .models import Profile, Section, Block, PortfolioType, Portfolio, VisitorMessage

admin.site.register(Profile)
admin.site.register(Section)
admin.site.register(Block)
admin.site.register(PortfolioType)
admin.site.register(Portfolio)
admin.site.register(VisitorMessage)
