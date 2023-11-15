from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribeForm

def subscribe(request):
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe = subscribe_form.save()
            messages.success(request, 'You have successfully subscribed!')
            # Optionally, you can clear the form after successful submission
            subscribe_form = SubscribeForm()
    else:
        subscribe_form = SubscribeForm()

    template = 'templates/includes/footer.html'
    
    context = {
        'subscribe_form': subscribe_form,
    }

    return render(request, 'templates/includes/footer.html', {'form': form})