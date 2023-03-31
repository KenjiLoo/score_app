from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScoreSerializer
from .models import Score
from django.shortcuts import render

def score_list(request):
    scores = Score.objects.all()
    context = {'scores': scores, }
    return render(request, 'score_list.html', context)

@api_view(['GET'])
def get_score(request):
    scores = Score.objects.all()
    context = {'scores': scores}
    for score in scores: 
        score.score = score.score/25
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)