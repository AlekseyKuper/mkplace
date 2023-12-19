# import django
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mkplace.settings")
# django.setup()

from rest_framework.test import APITestCase
from django.urls import reverse
from place.models import Things
from place.serializers import ThingsSerializer
from rest_framework import status



class ThingsApiTestCase(APITestCase):
    def test_get_list(self):
        thing1 = Things.objects.create(name='Тыква', price=15)
        thing2 = Things.objects.create(name='Баклажан', price=21)

        response = self.client.get(reverse('thing_api_list'))

        serial_data = ThingsSerializer([thing1, thing2], many=True).data
        serial_data = {'thing_list': serial_data}

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serial_data, response.data)