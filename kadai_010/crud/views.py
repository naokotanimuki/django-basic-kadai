from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

# Create your views here.
class TopView(TemplateView):
  template_name = "top.html"

class ProductListView(ListView):
  model = Product
  paginate_by = 3

# 新規作成画面の作成
class ProductCreateView(CreateView):
  model = Product
  fields = '__all__'

#　商品情報の編集画面を作成
class ProductUpdateView(UpdateView):
  model = Product
  fields = '__all__'
  template_name_suffix = '_update_form'

# 商品情報を削除する画面を作成
class ProductDeleteView(DeleteView):
  model = Product
  success_url = reverse_lazy('list')

# 商品詳細を表示する画面を作成
class ProductDetailView(DetailView):
  model = Product
  template_name_suffix = '_detail'