from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Score
from .serializers import ScoreSerializer

class GetScoreTests(APITestCase):
    def setUp(self):
        self.user1 = Score.objects.create(user_id='user1', score=50)
        self.user2 = Score.objects.create(user_id='user2', score=75)

    def test_api_endpoint(self):
        url = reverse('get_score')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_api_output(self):
        url = reverse('get_score')
        response = self.client.get(url)
        scores = Score.objects.all()
        for score in scores:
            score.score = score.score / 25
        serializer = ScoreSerializer(scores, many=True)
        self.assertEqual(response.data, serializer.data)
