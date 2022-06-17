from django.test import TestCase
import unittest
import shutil
from GamePLAY.models import League, Team
from SneakyPitch import settings


class LeagueTestCase(TestCase):
    def setUp(self):
        League.objects.create(league_name='diga')


    def test_league_creation(self):
        kwachu = League.objects.get(league_name='diga').id
