from django.contrib import admin
from django.contrib import admin
import nested_admin

from discussion.models import DiscussionThread, Reply, Attachment, Tag

class AttachmentInline(nested_admin.NestedStackedInline):
    model = Attachment
    extra = 1

class ReplyInline(nested_admin.NestedStackedInline):
    model = Reply
    inlines = [AttachmentInline]
    extra = 1

class DiscussionThreadAdmin(nested_admin.NestedModelAdmin):
    inlines = [ReplyInline]
    extra = 1

admin.site.register(DiscussionThread, DiscussionThreadAdmin)
admin.site.register(Tag)