from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribeForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed!')
            # Optionally, you can clear the form after successful submission
            form = SubscribeForm()
    else:
        form = SubscribeForm()

    return render(request, 'subscribe/subscribe_form.html', {'form': form})