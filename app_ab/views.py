from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from app_ab.models import Person, Address, Phone, Email, Group


class AddPerson(View):

    def get(self, request):
        return render(request, 'add_person.html', {})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        photo = request.POST.get('photo')
        if (first_name, last_name, description, photo) is not None:
            Person.objects.create(first_name=first_name, last_name=last_name, description=description, photo=photo)
            return render(request, 'person.html', {'first_name': first_name})
            # return HttpResponseRedirect('/new/')
        else:
            return HttpResponse('Enter a new contact\'s first name and last name')


def show_person(request, id):
    person = get_object_or_404(Person, id=id)
    # person = Person.objects.get(id=id)
    return render(request, 'person.html', {'person': person})

def delete_person(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return HttpResponseRedirect('/')

class EditPerson(View):

    def get(self, request, id):
        person = get_object_or_404(Person, id=id)
        return render(request, 'edit_person.html', {'person': person})

    def post(self, request, id):
        person = get_object_or_404(Person, id=id)
        if 'first_name' in request.POST:
            person.first_name = request.POST['first_name']
        if 'last_name' in request.POST:
            person.last_name = request.POST['last_name']
        if 'description' in request.POST:
            person.description = request.POST['description']
        if 'photo' in request.POST:
            person.photo = request.POST['photo']
        person.save()
        return render(request, 'edit_person.html', {'person': person})
        # return HttpResponseRedirect('/')


class PersonList(View):

    def get(self, request):
        persons = Person.objects.all().order_by('last_name')
        return render(request, 'person_list.html', {'persons': persons})


def add_address(request, id):
    if request.method == 'GET':
        person = get_object_or_404(Person, id=id)
        return render(request, 'add_address.html', {'person': person})

    elif request.method == 'POST':
        person = get_object_or_404(Person, id=id)

        city = request.POST.get('city')
        street = request.POST.get('street')
        house_no = request.POST.get('house_no')
        flat_no = request.POST.get('flat_no')
        person.person_address.create(city=city, street=street, house_no=house_no,
                                  flat_no=flat_no, person=person)

        return HttpResponseRedirect('/show/{}'.format(id))

class EditAddress(View):

    def get(self, request, person_id, id):
        person = get_object_or_404(Person, id=person_id)
        address = person.person_address.get(id=id)
        return render(request, 'edit_address.html', {'person': person, 'address': address})

    def post(self, request, person_id, id):
        person = get_object_or_404(Person, id=person_id)
        address = person.person_address.get(id=id)
        if 'city' in request.POST:
            address.city = request.POST['city']
        if 'street' in request.POST:
            address.street = request.POST['street']
        if 'house_no' in request.POST:
            address.house_no = request.POST['house_no']
        if 'flat_no' in request.POST:
            address.flat_no = request.POST['flat_no']
        address.save()
        return render(request, 'edit_address.html', {'person': person, 'address': address})

def delete_address(request, person_id, address_id):
    person = get_object_or_404(Person, id=person_id)
    address = person.person_address.get(id=address_id)
    address.delete()
    return HttpResponseRedirect('/show/{}'.format(person_id))


def add_phone(request, id):
    if request.method == 'GET':
        person = get_object_or_404(Person, id=id)
        return render(request, 'add_phone.html', {'person': person})

    elif request.method == 'POST':
        person = get_object_or_404(Person, id=id)

        phone_no = request.POST.get('phone_no')
        no_type = request.POST.get('no_type')
        person.person_phone.create(phone_no=phone_no, no_type=no_type, person=person)

        return HttpResponseRedirect('/show/{}'.format(id))

class EditPhone(View):

    def get(self, request, person_id, id):
        person = get_object_or_404(Person, id=person_id)
        phone = person.person_phone.get(id=id)
        return render(request, 'edit_phone.html', {'person': person, 'phone': phone})

    def post(self, request, person_id, id):
        person = get_object_or_404(Person, id=person_id)
        phone = person.person_phone.get(id=id)
        if 'phone_no' in request.POST:
            phone.phone_no = request.POST['phone_no']
        if 'no_type' in request.POST:
            phone.no_type = request.POST['no_type']
        phone.save()
        return render(request, 'edit_phone.html', {'person': person, 'phone': phone})

def delete_phone(request, person_id, phone_id):
    person = get_object_or_404(Person, id=person_id)
    phone = person.person_phone.get(id=phone_id)
    phone.delete()
    return HttpResponseRedirect('/show/{}'.format(person_id))


def add_email(request, id):
    if request.method == 'GET':
        person = get_object_or_404(Person, id=id)
        return render(request, 'add_email.html', {'person': person})

    elif request.method == 'POST':
        person = get_object_or_404(Person, id=id)

        email = request.POST.get('email')
        email_type = request.POST.get('email_type')
        person.person_email.create(email=email, email_type=email_type, person=person)

        return HttpResponseRedirect('/show/{}'.format(id))

class EditEmail(View):

    def get(self, request, person_id, id):
        person = get_object_or_404(Person, id=person_id)
        email = person.person_email.get(id=id)
        return render(request, 'edit_email.html', {'person': person, 'email': email})

    def post(self, request, person_id, id):
        person = get_object_or_404(Person, id=person_id)
        email = person.person_email.get(id=id)
        if 'email' in request.POST:
            email.email = request.POST['email']
        if 'no_type' in request.POST:
            email.email_type = request.POST['email_type']
        email.save()
        return render(request, 'edit_email.html', {'person': person, 'email': email})

def delete_email(request, person_id, email_id):
    person = get_object_or_404(Person, id=person_id)
    email = person.person_email.get(id=email_id)
    email.delete()
    return HttpResponseRedirect('/show/{}'.format(person_id))

