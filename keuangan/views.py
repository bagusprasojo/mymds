from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

# Create your views here.
@login_required(login_url = 'login')
def dashboard_keuangan(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'penerimaan_spp':150000,
        'tunggakan_spp':60000,
        'userprofile':userprofile,
    }
    return render(request, 'keuangan/dashboard_keuangan.html', context)