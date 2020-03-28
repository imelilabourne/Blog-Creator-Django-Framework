from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.decorators import login_required
from .models import Post, Profile, ProductPic, TravelPic, FoodPic
from user.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from base.forms import ProductPicForm, TravelPicForm, FoodPicForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

@login_required
def home(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('base:base-home') 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': Post.objects.all(),
        'productpics': ProductPic.objects.all()
    }
    return render(request, 'base/home.html', context)

@login_required
def gallery(request):
    context = {
        'posts': Post.objects.all(),
        'productpics': ProductPic.objects.all()
    }
    return render(request, 'base/gallery.html', context)

@login_required
def travel(request):
    context = {
        'posts': Post.objects.all(),
        'travelpics': TravelPic.objects.all()
        # 'productpics': ProductPic.objects.all()
    }
    return render(request, 'base/travel.html', context)

class PostListView(ListView):
    model = ProductPic
    template_name = 'base/gallery.html'
    # context_object_name = 'productpics'

    def get_context_data(self, **kwargs):
        product = ProductPic.objects.filter(user=self.request.user)

        context = super().get_context_data(**kwargs)
        context['productpics'] = product
        return context

class PostDetailView(DetailView):
    model = ProductPic
    template_name = 'base/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = ProductPic
    template_name = 'base/post_form.html'
    form_class = ProductPicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url ='/gallery'

class PostUpdateView(LoginRequiredMixin,UpdateView, UserPassesTestMixin):
    model = ProductPic
    template_name = 'base/post_form.html'
    form_class = ProductPicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        productpic = self.get.object()
        if self.request.user == productpic.user:
            return True
        return False
    
    success_url ='/gallery'

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductPic
    template_name = 'base/post_confirm_delete.html'
    
    success_url ='/gallery'


# for travels
class TravelListView(ListView):
    model = TravelPic
    template_name = 'base/travel.html'
    # context_object_name = 'productpics'

    def get_context_data(self, **kwargs):
        product = TravelPic.objects.filter(user=self.request.user)

        context = super().get_context_data(**kwargs)
        context['travelpics'] = product
        return context

class TravelDetailView(DetailView):
    model = TravelPic
    template_name = 'base/travel_detail.html'

class TravelCreateView(LoginRequiredMixin,CreateView):
    model = TravelPic
    template_name = 'base/travelpost_form.html'
    form_class = TravelPicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url ='/travel/'

class TravelUpdateView(LoginRequiredMixin,UpdateView, UserPassesTestMixin):
    model = TravelPic
    template_name = 'base/travelpost_form.html'
    form_class = TravelPicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        travelpic = self.get.object()
        if self.request.user == travelpic.user:
            return True
        return False
    success_url ='/travel/'
class TravelDeleteView(LoginRequiredMixin,DeleteView):
    model = TravelPic
    template_name = 'base/travelpost_confirm_delete.html'
    
    success_url ='/travel/'


# For Food Pictures
class FoodListView(ListView):
    model = FoodPic
    template_name = 'base/food.html'
    # context_object_name = 'productpics'

    def get_context_data(self, **kwargs):
        product = FoodPic.objects.filter(user=self.request.user)

        context = super().get_context_data(**kwargs)
        context['foodpics'] = product
        return context

class FoodDetailView(DetailView):
    model = FoodPic
    template_name = 'base/food_detail.html'

class FoodCreateView(LoginRequiredMixin,CreateView):
    model = FoodPic
    template_name = 'base/foodpost_form.html'
    form_class = FoodPicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url ='/food/'

class FoodUpdateView(LoginRequiredMixin,UpdateView, UserPassesTestMixin):
    model = FoodPic
    template_name = 'base/foodpost_form.html'
    form_class = FoodPicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Foodpic = self.get.object()
        if self.request.user == Foodpic.user:
            return True
        return False
    success_url ='/food/'
class FoodDeleteView(LoginRequiredMixin,DeleteView):
    model = FoodPic
    template_name = 'base/foodpost_confirm_delete.html'
    
    success_url ='/food'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer