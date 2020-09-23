from django.shortcuts import render , redirect , get_object_or_404
from .models import Profile
# Create your views here.
def profile_list(request):
    profile_list = Profile.objects.all()
    context = {'profile_list':profile_list} 
    return render (request , 'Profile.html' , context)

def profile_detail(request,id):
    profile_detail = Profile.objects.get(id=id)
    context = {'profile_detail':profile_detail}
    return render(request , 'details_std.html' , context)

def del_profile(request , pk):
    del_profile = get_object_or_404(pk=pk)
    del_profile.delete()
    return redirect('home:profile_list')
    return render(request , 'Profile.html' , {'del_profile':del_profile},)
