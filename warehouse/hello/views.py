from django.shortcuts import render, redirect
from .models import Employee, Storage
import requests
from .forms import *
from django.core.cache import cache


def index(request):
    return render(request, 'hello/index.html')


def edit(request):
    return render(request, 'hello/edit.html')


def search(request):
    return render(request, 'hello/search.html')


def edit_storage(request):
    return render(request, 'hello/edit_storage.html')


def edit_packinglist(request):
    return render(request, 'hello/edit_packinglist.html')


def edit_salesinvoice(request):
    return render(request, 'hello/edit_salesinvoice.html')


def edit_2(request):
    return render(request, 'hello/edit_2.html')


def edit_inventory(request):
    return render(request, 'hello/edit_inventory.html')


def show_storage(request):
    storage = Storage.objects.order_by('name')
    storage_list = []
    for st in storage:
        storage_info = {
            'number': st.number,
            'name': st.name,
            'phone': st.phone
        }
        storage_list.append(storage_info)

    context = {'info': storage_list}

    return render(request, 'hello/show_storage.html', context)


def search_list(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Inventory.objects.filter(name=name) and name != '':
            cache.set('3', name)
            return redirect('search_2_list')

    form = FindInventoryForm
    context = {'form': form}

    return render(request, 'hello/search_list.html', context)


def search_2_list(request):
    name = cache.get('3')
    inventory = Inventory.objects.filter(name=name)
    id = inventory[0].id
    pack_list = []
    sales_list = []
    packinglist = PackingList.objects.filter(inventory_id=id)
    for st in packinglist:
        packinglist_info = {
            'date': st.date,
            'amount': st.amount
        }
        pack_list.append(packinglist_info)

    salesinvoice = SalesInvoice.objects.filter(inventory_id=id)
    for st in salesinvoice:
        sales_info = {
            'date': st.date,
            'amount': st.amount
        }
        sales_list.append(sales_info)

    context = {'pack': pack_list, 'sales': sales_list, 'name': name, }
    return render(request, 'hello/search_2_list.html', context)


def search_inventory(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        number = request.POST.get('number')
        if Storage.objects.filter(number=number) and Inventory.objects.filter(type=type):
            cache.set('4', type)
            cache.set('5', number)
            return redirect('search_2_inventory')

    form_1 = FindStorageForm
    form_2 = SearchInventory
    context = {'form_1': form_1, 'form_2': form_2}

    return render(request, 'hello/search_inventory.html', context)


def search_2_inventory(request):
    type = cache.get('4')
    number = cache.get('5')
    inventory = Inventory.objects.filter(type=type)
    storage = Storage.objects.filter(number=number)
    id_inventory_list = []
    name = []
    for i in inventory:
        subj = i.id
        id_inventory_list.append(subj)

    for i in inventory:
        name.append(i.name)

    id_storage = storage[0].id

    packing_sum = 0
    sales_sum = 0

    for i in id_inventory_list:
        x = PackingList.objects.filter(inventory_id=i, storage_id=id_storage)
        y = SalesInvoice.objects.filter(inventory_id=i, storage_id=id_storage)
        for j in x:
            packing_sum += j.amount
        for j in y:
            sales_sum += j.amount

    amount = packing_sum - sales_sum

    context = {'name': name, 'amount': amount, 'type': type, 'number': number}
    return render(request, 'hello/search_2_inventory.html', context)


def find_storage(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        if Storage.objects.filter(number=number) and number != '':
            cache.set('1', number)
            return redirect('find_2_storage')

    form = FindStorageForm
    context = {'form': form}

    return render(request, 'hello/find_storage.html', context)


def find_packinglist(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        if PackingList.objects.filter(id=pid) and pid != '':
            cache.set('6', pid)
            return redirect('find_2_packinglist')

    return render(request, 'hello/find_packinglist.html')


def find_salesinvoice(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        if SalesInvoice.objects.filter(id=pid) and pid != '':
            cache.set('7', pid)
            return redirect('find_2_salesinvoice')

    return render(request, 'hello/find_salesinvoice.html')


def find_inventory(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Inventory.objects.filter(name=name) and name != '':
            cache.set('2', name)
            return redirect('find_2_inventory')

    form = FindInventoryForm
    context = {'form': form}

    return render(request, 'hello/find_inventory.html', context)


def find_2_storage(request):
    storage_list = []
    num = cache.get('1')
    storage = Storage.objects.filter(number=num)
    for st in storage:
        storage_info = {
            'number': st.number,
            'name': st.name,
            'phone': st.phone
        }
        storage_list.append(storage_info)

    if request.method == 'POST':
        req_number = request.POST.get('number')
        req_name = request.POST.get('name')
        req_phone = request.POST.get('phone')
        obj = Storage.objects.get(number=num)
        obj.number = req_number
        obj.name = req_name
        obj.phone = req_phone
        obj.save()

    form = EditStorage
    context = {'info': storage_list, 'form': form}
    return render(request, 'hello/find_2_storage.html', context)


def find_2_inventory(request):
    inventory_list = []
    name = cache.get('2')
    inventory = Inventory.objects.filter(name=name)
    for st in inventory:
        inventory_info = {
            'name': st.name,
            'type': st.type
        }
        inventory_list.append(inventory_info)

    if request.method == 'POST':
        req_name = request.POST.get('name')
        req_type = request.POST.get('type')
        obj = Inventory.objects.get(name=name)
        obj.name = req_name
        obj.type = req_type
        obj.save()

    form = EditInventory
    context = {'info': inventory_list, 'form': form}
    return render(request, 'hello/find_2_inventory.html', context)


def find_2_packinglist(request):
    message = ''
    packing_info = {}
    pid = cache.get('6')
    packing = PackingList.objects.filter(id=pid)

    employee_list = Employee.objects.all()
    empl_name = []
    for i in employee_list:
        empl_name.append(i.name)

    inventory_list = Inventory.objects.all()
    inv_name = []
    for i in inventory_list:
        inv_name.append(i.name)

    storage_list = Storage.objects.all()
    storage_number = []
    for i in storage_list:
        storage_number.append(i.number)

    for st in packing:
        employee_id = st.employee_id
        employee = Employee.objects.get(id=employee_id)
        inventory_id = st.inventory_id
        inventory = Inventory.objects.get(id=inventory_id)
        storage_id = st.storage_id
        storage = Storage.objects.get(id=storage_id)
        packing_info = {
            'amount': st.amount,
            'date': st.date,
            'inventory': inventory.name,
            'employee': employee.name,
            'storage': storage.number
        }

    id = packing[0].id

    if request.method == 'POST':
        req_amount = request.POST.get('amount')
        req_date = request.POST.get('date')

        name_employee = request.POST.get('name_employee')
        name_inventory = request.POST.get('name_inventory')
        number = request.POST.get('number')
        eid = Employee.objects.get(name=name_employee).id
        iid = Inventory.objects.get(name=name_inventory).id
        sid = Storage.objects.get(number=number).id

        if req_amount == '' or req_date == '' or name_inventory == '' or name_employee == '' or number == '':
            message = 'заполните все поля'
        else:
            obj = PackingList.objects.get(id=id)
            obj.amount = req_amount
            obj.date = req_date
            obj.inventory_id = iid
            obj.employee_id = eid
            obj.storage_id = sid
            obj.save()

    context = {'message': message, 'info': packing_info, 'employee_list': employee_list, 'inventory_list': inventory_list, 'storage_number': storage_number}
    return render(request, 'hello/find_2_packinglist.html', context)


def find_2_salesinvoice(request):
    message = ''
    sales_info = {}
    pid = cache.get('7')
    sales = SalesInvoice.objects.filter(id=pid)

    employee_list = Employee.objects.all()
    empl_name = []
    for i in employee_list:
        empl_name.append(i.name)

    inventory_list = Inventory.objects.all()
    inv_name = []
    for i in inventory_list:
        inv_name.append(i.name)

    storage_list = Storage.objects.all()
    storage_number = []
    for i in storage_list:
        storage_number.append(i.number)

    for st in sales:
        employee_id = st.employee_id
        employee = Employee.objects.get(id=employee_id)
        inventory_id = st.inventory_id
        inventory = Inventory.objects.get(id=inventory_id)
        storage_id = st.storage_id
        storage = Storage.objects.get(id=storage_id)
        sales_info = {
            'amount': st.amount,
            'date': st.date,
            'inventory': inventory.name,
            'employee': employee.name,
            'storage': storage.number
        }

    id = sales[0].id

    if request.method == 'POST':
        req_amount = request.POST.get('amount')
        req_date = request.POST.get('date')

        name_employee = request.POST.get('name_employee')
        name_inventory = request.POST.get('name_inventory')
        number = request.POST.get('number')
        eid = Employee.objects.get(name=name_employee).id
        iid = Inventory.objects.get(name=name_inventory).id
        sid = Storage.objects.get(number=number).id

        if req_amount == '' or req_date == '' or name_inventory == '' or name_employee == '' or number == '':
            message = 'заполните все поля'
        else:
            obj = SalesInvoice.objects.get(id=id)
            obj.amount = req_amount
            obj.date = req_date
            obj.inventory_id = iid
            obj.employee_id = eid
            obj.storage_id = sid
            obj.save()

    context = {'message': message, 'info': sales_info, 'employee_list': employee_list, 'inventory_list': inventory_list, 'storage_number': storage_number}
    return render(request, 'hello/find_2_salesinvoice.html', context)


def add_storage(request):
    message = ''
    if request.method == 'POST':
        form = AddStorageForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Запись добавлена'
        else:
            message = 'Форма не корректна'
    form = AddStorageForm()
    context = {'form': form, 'message': message}
    return render(request, 'hello/add_storage.html', context)


def add_packinglist(request):
    message =''
    info = []
    employee_list = Employee.objects.all()
    empl_name = []
    for i in employee_list:
        empl_name.append(i.name)

    inventory_list = Inventory.objects.all()
    inv_name = []
    for i in inventory_list:
        inv_name.append(i.name)

    storage_list = Storage.objects.all()
    storage_number = []
    for i in storage_list:
        storage_number.append(i.number)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        inventory = request.POST.get('name_inventory')
        employee = request.POST.get('name_employee')
        storage = request.POST.get('number')
        if amount == '' or date == '' or inventory == '' or employee == '' or storage == '':
            message = 'Заполните все поля'
        else:
            inv = Inventory.objects.get(name=inventory)
            inv_id = inv.id
            empl = Employee.objects.get(name=employee)
            empl_id = empl.id
            st = Storage.objects.get(number=storage)
            st_id = st.id
            PackingList.objects.create(amount=amount, date=date, inventory_id=inv_id, employee_id=empl_id , storage_id=st_id)

    context = {'message': message, 'info': info, 'employee_list': employee_list, 'inventory_list': inventory_list, 'storage_number': storage_number}
    return render(request, 'hello/add_packinglist.html', context)


def add_salesinvoice(request):
    message = ''
    info = []
    employee_list = Employee.objects.all()
    empl_name = []
    for i in employee_list:
        empl_name.append(i.name)

    inventory_list = Inventory.objects.all()
    inv_name = []
    for i in inventory_list:
        inv_name.append(i.name)

    storage_list = Storage.objects.all()
    storage_number = []
    for i in storage_list:
        storage_number.append(i.number)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        inventory = request.POST.get('name_inventory')
        employee = request.POST.get('name_employee')
        storage = request.POST.get('number')
        if amount == '' or date == '' or inventory == '' or employee == '' or storage == '':
            message = 'Заполните все поля'
        else:
            inv = Inventory.objects.get(name=inventory)
            inv_id = inv.id
            empl = Employee.objects.get(name=employee)
            empl_id = empl.id
            st = Storage.objects.get(number=storage)
            st_id = st.id
            SalesInvoice.objects.create(amount=amount, date=date, inventory_id=inv_id, employee_id=empl_id , storage_id=st_id)

    context = {'message': message, 'info': info, 'employee_list': employee_list, 'inventory_list': inventory_list, 'storage_number': storage_number}
    return render(request, 'hello/add_salesinvoice.html', context)


def add_inventory(request):
    message = ''
    if request.method == 'POST':
        form = AddInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Запись добавлена'
        else:
            message = 'Форма не корректна'
    form = AddInventoryForm()
    context = {'form': form, 'message': message}
    return render(request, 'hello/add_inventory.html', context)


def delete_inventory(request):
    message = ' '
    if request.method == 'POST':
        name = request.POST.get('name')
        if Inventory.objects.filter(name=name) and name != '':
            Inventory.objects.filter(name=name).delete()
            message = 'Запись удалена'
        else:
            message = 'Такой записи нет'

    form = FindInventoryForm
    context = {'form': form, 'message': message}

    return render(request, 'hello/delete_inventory.html', context)


def delete_storage(request):
    message = ' '
    if request.method == 'POST':
        number = request.POST.get('number')
        if Storage.objects.filter(number=number) and number != '':
            Storage.objects.filter(number=number).delete()
            message = 'Запись удалена'
        else:
            message = 'Такой записи нет'

    form = FindStorageForm
    context = {'form': form, 'message': message}

    return render(request, 'hello/delete_storage.html', context)


def delete_packinglist(request):
    message = ' '
    if request.method == 'POST':
        pid = request.POST.get('pid')
        if PackingList.objects.filter(id=pid) and pid != '':
            PackingList.objects.filter(id=pid).delete()
            message = 'Запись удалена'
        else:
            message = 'Такой записи нет'

    context = {'message': message}

    return render(request, 'hello/delete_packinglist.html', context)


def delete_salesinvoice(request):
    message = ' '
    if request.method == 'POST':
        pid = request.POST.get('pid')
        if SalesInvoice.objects.filter(id=pid) and pid != '':
            SalesInvoice.objects.filter(id=pid).delete()
            message = 'Запись удалена'
        else:
            message = 'Такой записи нет'

    context = {'message': message}

    return render(request, 'hello/delete_packinglist.html', context)
