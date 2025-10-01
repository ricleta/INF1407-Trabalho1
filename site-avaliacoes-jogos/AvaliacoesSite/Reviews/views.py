from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Review
from .forms import ReviewForm
from django.contrib.auth.models import Group

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

def home_page(request):
    '''
    View for the home page of the reviews section.
    '''
    return render(request, 'Reviews/index.html')

class ReviewListView(LoginRequiredMixin, ListView):
    """
    View to display a list of reviews created by the logged-in user.

    Only authenticated users in the 'Reviewers' group can access this page.
    """
    model = Review
    context_object_name = 'reviews'
    template_name = 'Reviews/listaReviews.html'

    def get_queryset(self):
        """
        Filters the reviews to show only the ones created by the current user.
        """
        return self.model.objects.filter(user=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        """
        Checks for user authentication and group membership before allowing access.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='Reviewers').exists():
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a new review.

    Only authenticated users in the 'Reviewers' group can create a review.
    The view automatically associates the review with the logged-in user.
    """
    model = Review
    form_class = ReviewForm
    template_name = 'Reviews/criaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def dispatch(self, request, *args, **kwargs):
        """
        Checks for user authentication and group membership before allowing access.
        """
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.groups.filter(name='Reviewers').exists():
            return HttpResponseRedirect(reverse('home-page'))
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
        Passes the current user to the form for custom validation.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Overrides the form_valid method to associate the logged-in user with the new review.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing review.

    A user can only update their own reviews.
    """
    model = Review
    form_class = ReviewForm
    template_name = 'Reviews/atualizaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def get_queryset(self):
        """
        Restricts the query to reviews owned by the current user.
        """
        return self.model.objects.filter(user=self.request.user)
    
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting an existing review.

    A user can only delete their own reviews.
    """
    model = Review
    template_name = 'Reviews/deletaReview.html'
    success_url = reverse_lazy('Reviews:lista-reviews')
    
    def get_queryset(self):
        """
        Restricts the query to reviews owned by the current user.
        """
        return self.model.objects.filter(user=self.request.user)
