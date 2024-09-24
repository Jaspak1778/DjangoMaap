from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from ilmoitukset.models import Ad 
from ilmoitukset.forms import AdForm
from .forms import SearchForm  # Import the search form
from django.contrib.auth.decorators import login_required


# Ilmoitusten luonti formi
class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'contact_info', 'image']


# Kotinäkymä johon tuodaan kannasta ilmoitukset
def home(request):
    ads = Ad.objects.all().order_by('-created_at')  
    search_form = SearchForm(request.GET)

    if request.GET.get('query'):  
        if search_form.is_valid(): 
            query = search_form.cleaned_data['query']
            if query:  
                ads = ads.filter(title__icontains=query)  

    return render(request, 'home.html', {'ads': ads, 'search_form': search_form})


 # Luo ilmoitus
@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('home')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})


# Katsele omia ilmoituksia
@login_required
def my_ads(request):
    user_ads = Ad.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_ads.html', {'ads': user_ads})


# Muokkaa omia ilmoituksia
@login_required
def edit_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)  
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('my_ads')  
    else:
        form = AdForm(instance=ad)  
    return render(request, 'edit_ad.html', {'form': form, 'ad': ad})


# Poista ilmoitus
@login_required
def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id, user=request.user)  
    if request.method == 'POST':
        ad.delete()
        return redirect('my_ads')  

    return render(request, 'delete_ad_confirm.html', {'ad': ad})
