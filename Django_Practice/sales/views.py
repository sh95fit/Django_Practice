from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

from .models import CustomID, Sale, Person

from .forms import SaleInputForm, SaleModelForm

from django.core.mail import send_mail


def Homepage(request):
    # customer = CustomID.objects.all()
    # context = {
    #     "MenuName": "Noodle",
    #     "Price": "10,000 won",
    #     "Customer": customer
    # }
    # return render(request, "sales/index.html", context)
    return render(request, "sales/index.html")


def SalesList(request):
    sales = Sale.objects.all()

    sale_context = {
        "key": sales
    }

    return render(request, "sales/sales_list.html", sale_context)


def SalesDetail(request, pk):
    sale = Sale.objects.get(id=pk)
    detail_context = {
        "info": sale
    }
    # return HttpResponse(f"Detail Page - {sale.first_name} {sale.last_name}")
    return render(request, "sales/sales_detail.html", detail_context)


def SaleInput_1(request):
    # print(request.POST)   # 폼에 의해 입력 후 전송된 정보 확인

    # 유효성 확인되면 DB에 저장
    form = SaleInputForm()

    if request.method == "POST":
        form = SaleInputForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)  # cleaned_data를 통해 필요한 정보들만 추려낼 수 있다
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            person = Person.objects.first()

            Sale.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                person=person
            )

            print("정보가 정상 입력되었습니다.")

            return redirect("/sales")

    context = {
        "form": form
    }

    return render(request, "sales/sales_input.html", context)


def SaleInput(request):
    # print(request.POST)   # 폼에 의해 입력 후 전송된 정보 확인

    # 유효성 확인되면 DB에 저장
    form = SaleModelForm()

    if request.method == "POST":
        form = SaleModelForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)  # cleaned_data를 통해 필요한 정보들만 추려낼 수 있다

            # ModelForm을 쓰면 아래 절차를 생략할 수 있다
            form.save()

            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # person = form.cleaned_data['person']

            # Sale.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     person=person
            # )

            print("정보가 정상 입력되었습니다.")

            return redirect("/sales")

    context = {
        "form": form
    }

    return render(request, "sales/sales_input.html", context)


def SaleUpdate_1(request, pk):
    sales = Sale.objects.get(id=pk)
    form = SaleInputForm()

    if request.method == "POST":
        form = SaleInputForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            person = Person.objects.first()

            sales.first_name = first_name
            sales.last_name = last_name
            sales.age = age
            sales.person = person

            sales.save()

            return redirect("/sales")

    context = {
        "sales": sales,
        "form": form,
    }

    return render(request, "sales/sales_update.html", context)


def SaleUpdate(request, pk):
    sales = Sale.objects.get(id=pk)

    # instance를 지정하여 pk가 일치하는 고객 정보를 form으로 지정하여 해당 값을 수정하도록 처리
    form = SaleModelForm(instance=sales)

    if request.method == "POST":
        form = SaleModelForm(request.POST, instance=sales)
        if form.is_valid():
            form.save()

            return redirect("/sales")

    context = {
        "sales": sales,
        "form": form,
    }

    return render(request, "sales/sales_update.html", context)


def SaleDelete(request, pk):
    sale = Sale.objects.get(id=pk)
    sale.delete()

    return redirect("/sales")


#################################################################
# 클래스를 이용한 뷰


class HomepageView(generic.TemplateView):
    template_name = "sales/index.html"


class SalesInputView(generic.CreateView):
    template_name = 'sales/sales_input.html'
    form_class = SaleModelForm

    def get_success_url(self):
        return reverse("Sales:List")

    def form_valid(self, form):
        send_mail(
            subject="New Information Create",
            message="Go Homepage",
            from_email="admin@practice.com",  # 송신하는 자
            recipient_list=["test@test.com"]  # 수신하는 자
        )
        return super(SalesInputView, self).form_valid(form)

    # 기본적으로 Template에서 form으로 받도록 되어 있다 (다른 명칭 적용 X)


class SalesListView(generic.ListView):
    template_name = "sales/sales_list.html"
    queryset = Sale.objects.all()
    context_object_name = "key"


class SalesDetailView(generic.DetailView):
    template_name = "sales/sales_detail.html"
    queryset = Sale.objects.all()
    context_object_name = "info"


class SalesUpdateView(generic.UpdateView):
    template_name = 'sales/sales_update.html'
    queryset = Sale.objects.all()
    form_class = SaleModelForm
    context_object_name = "sales"

    def get_success_url(self):
        return reverse("Sales:List")


class SalesDeleteView(generic.DeleteView):
    template_name = "sales/sales_delete.html"
    queryset = Sale.objects.all()

    def get_success_url(self):
        return reverse("Sales:List")
