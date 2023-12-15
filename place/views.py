from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Things, Suplier
from .forms import Thingsform, SuplierForm, RegistrationForm, LoginForm
from .utils import Default_value
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'place/index.html')

def show_things(request):
    context = {'title': 'Список предложений'}

    things_list = Things.objects.all()
    # context['things_list'] = things_list

    paginator = Paginator(things_list, 1)
    page_num = request.GET.get('page', 1)

    page_objects = paginator.get_page(page_num)
    context['things_list'] = page_objects

    if request.method == "GET":
        things_id = request.GET.get('id', 5)
        try:
            thing_one = Things.objects.get(pk=things_id)
        except:
            pass
        else:
            context['thing_one'] = thing_one
            context['name'] = request.GET.get('name', 'None')

    elif request.method == "POST":
        things_id = request.POST.get('id', 5)
        try:
            thing_one = Things.objects.get(pk=things_id)
        except:
            pass
        else:
            context['thing_one'] = thing_one
            context['name'] = request.POST.get('name', 'None')


    return render(request,
                  context=context,
                  template_name='place/show_things.html')
@permission_required('place.add_things')
def add_thing(request):
    if request.method == "POST":
        context = dict()
        context['name'] = request.POST.get('name')
        context['description'] = request.POST.get('description')
        context['price'] = request.POST.get('price')
        context['date_expired'] = request.POST.get('date_expired')
        context['photo'] = request.POST.get('photo')

        Things.objects.create(
            name=context['name'],
            description=context['description'],
            price=context['price'],
            date_expired=context['date_expired'],
            photo=context['photo'],
        )

        # return render(request, 'place/thing_info.html', context=context)
        return HttpResponseRedirect('/place/show_things/')
    else:
        thingsform = Thingsform()
        context = {'form': thingsform}
        return render(request, 'place/add_thing.html', context=context)

@login_required()
def thing_detail(request, thing_id):
    # thing = Things.objects.get(pk=thing_id)
    thing = get_object_or_404(Things, pk=thing_id)
    # context['thing_item'] = thing
    return render(request, 'place/thing_info.html', {'thing_item': thing})

class SuplierListView(ListView, Default_value):
    model = Suplier
    template_name = 'place/suplier/suplier_show.html'
    context_object_name = ('suplier_show')
    extra_context= {'title': "Лист поставщиков"}

    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        print(context)
        context['title']='Поставщики'
        # Dv = Default_value()
        # Dv.add_title_context(context=context, title_name='Страница поставщиков')
        # context['info']='Пидоры ушлые'
        context=self.add_title_context(context=context, title_name='Страница поставщиков')
        return context

    def get_queryset(self):
        return Suplier.objects.filter(exist=True).order_by("title")


class SuplierDetailView(DetailView):
    model = Suplier
    template_name = 'place/suplier_detail.html'
    context_object_name = ('one_suplier')
    extra_context = {'title': 'Описание поставщика'}
    pk_url_kwarg = 'suplier_id'

class SuplierCreateView(CreateView):
    model = Suplier
    form_class = SuplierForm
    template_name = ('place/suplier/suplier_add.html')

    context_object_name = 'form'
    success_url = reverse_lazy('show_suplier')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class SuplierUpdateView(UpdateView):
    model = Suplier
    form_class = SuplierForm
    template_name = ('place/suplier/suplier_edit.html')

    context_object_name = 'form'
    success_url = reverse_lazy('show_suplier')

    @method_decorator(permission_required('place.change_suplier'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SuplierDeleteView(DeleteView):
    model = Suplier
    success_url = reverse_lazy('show_suplier')

    @method_decorator(permission_required('place.delete_suplier'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'place/auth/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            login(request, user)
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            print(user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'place/auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('log_in')