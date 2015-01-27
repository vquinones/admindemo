from django.contrib.admin.sites import AdminSite


class UserAdmin(AdminSite):
    site_header = 'Yarvis Content Manager'
    #site_title = ugettext_lazy('My site admin')
    # Text to put in each page's <h1>.
    #site_header = ugettext_lazy('User Admin Site for Yarvis')
    #index_title = ugettext_lazy('Yarvis Content Manager')
    #login_form =  UserAdminAuthenticationForm

    def has_permission(self, request):
        return request.user.is_staff

