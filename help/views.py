from django.shortcuts import render

# Create your views here.
def help(response):
    help_screen = {"help_text":"This Is Your Help Desk !"}
    return render(response, 'help/help.html', context = help_screen)