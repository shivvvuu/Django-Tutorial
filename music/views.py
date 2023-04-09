from django.views import generic
from .models import Album
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import UserForm

class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = 'object_list'

    def get_queryset(self):
        return Album.objects.all()
    

class DetailView(generic.DetailView):
    model =Album
    template_name = 'music/detail.html'
    
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'alum_title', 'genre', 'alum_logo']
    
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'alum_title', 'genre', 'alum_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'
    
    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    # process form data 
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            
            user = form.save(commit=False)
            
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            # return User objects if credentials are correct
            user = authenticate(username=username, password=password)
        
            if user is not None:
            
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
            
        return render(request, self.template_name, {'form': form})















# from django.shortcuts import render, get_object_or_404
# from .models import Album, Song
# # from django.http import Http404

# def index(request):
#     all_album = Album.objects.all()
#     context = {
#         'all_album' : all_album,
#     }
#     return render(request, 'music/index.html', context )

# def detail(request, album_id):
#     # try:
#     #     album = Album.objects.get(pk = album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album Does not exist")
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})

# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "You did not selected vaild song!!",
#             })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})
    