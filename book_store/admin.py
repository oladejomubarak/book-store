from django.contrib import admin


class BookStoreAdminSite(admin.AdminSite):
    site_header = "Book store site"
    site_title = "Book store"
    index_title = "Book Store Admin Interface"
    logout_template = "my_logged_out.html"
