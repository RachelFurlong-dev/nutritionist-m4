from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscribeForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed!')
            return redirect('subscribe_success')
        else:
            messages.error(request, 'Invalid email address. Please try again.')
    else:
        form = SubscribeForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})

def subscribe_success(request):
    return render(request, 'newsletter/subscribe_success.html')