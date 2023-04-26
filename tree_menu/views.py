from django.shortcuts import render
from django.views import View


class MainView(View):
    """Main view for tree_menu app. It renders main.html template and used for testing purposes."""
    def get(self, request, *args, **kwargs):
        return render(request, 'tree_menu/main.html', kwargs)
