import json

from django.http      import JsonResponse
from django.views     import View

from owners.models    import Person, Dog 


# Create your views here.
class OwnersView(View):
    def post(self, request):
        data     = json.loads(request.body)
        # print(data)
        Person.objects.create(
            name     = data['name'],
            email    = data['email'],
            age      = data['age']
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status = 201)

    def get(self, request):
        persons = Person.objects.all()
        dogs = Dog.objects.all()

        results = []
        for person in persons:
            results.append(
                {
                    "person" : person.name,
                    "email"  : person.email,
                    "age"    : person.age,
                    "dog"    : list(dogs.values('name', 'age').filter(person = person.id))
                }
            )
        return JsonResponse({'results':results}, status=200)


class DogsView(View):
    def post(self, request):
        data     = json.loads(request.body)
        dog   = Dog.objects.create(
            name     = data['name'],
            age      = data['age'],
            person = Person.objects.get(name=data['person']),
        )

        return JsonResponse({'MESSAGE':'CREATED'}, status = 201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    "dog"    : dog.name,
                    "age"    : dog.age,
                    "person" : dog.person.name,                    

                }
            )
        return JsonResponse({'results':results}, status=200)

