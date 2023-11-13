"""from django.shortcuts import render, redirect
from .forms import SubscribeForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribe_success')
    else:
        form = SubscribeForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})

def subscribe_success(request):
    return render(request, 'newsletter/subscribe_success.html')"""