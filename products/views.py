from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Product
from .forms import ProductForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

class ProductListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        blocked_users = BlockList.objects.filter(blocker=self.request.user).values_list('blocked_id', flat=True)
        return Product.objects.exclude(author__in=blocked_users)

    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        return self.request.user == self.get_object().author

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        return self.request.user == self.get_object().author

@login_required
def my_products(request):
    products = Product.objects.filter(author=request.user)
    return render(request, 'products/my_products.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def chat_view(request):
    if request.method == "POST":
        # 메시지 저장 로직은 생략
        return redirect('chat')
    return render(request, 'products/chat.html')

@login_required
def report_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        reason = request.POST.get("reason")
        # 신고 내용 저장 로직은 생략
        return redirect('product_detail', pk=pk)
    return render(request, 'products/report.html', {'product': product})

@login_required
def transfer_view(request):
    if request.method == "POST":
        receiver = request.POST.get("receiver")
        amount = request.POST.get("amount")
        # 실제 송금 로직 생략
        return redirect('product_list')
    return render(request, 'products/transfer.html')

from .models import BlockList

@login_required
def block_user(request, user_id):
    target = User.objects.get(pk=user_id)
    if target != request.user:
        BlockList.objects.get_or_create(blocker=request.user, blocked=target)
    return redirect('product_list')

@login_required
def unblock_user(request, user_id):
    BlockList.objects.filter(blocker=request.user, blocked__id=user_id).delete()
    return redirect('product_list')