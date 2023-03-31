# Student's Result Announcement App 👨‍🏫 
This app is created as a take-home coding challenge by Pacer. The following tasks are requirements that are in the challenge, and these are my attempts to meet these requirements. 

The idea of this app is to simply display the results of students. A simple app like this is made in hopes to maintain simplicity and effectiveness of the answers.


## Task 1  👨‍💻 
```
Create a simple Python Django app that has the following features:
- a backend API endpoint called get_score with a simple dummy formula that could
be anything e.g. result = input + 1
- a PostgreSQL database that the backend API uses to log the user ID and the score
- demonstrate that the endpoint is behaving as expected (how do we test it? how can
we prove that it is working as expected?)
```
Solution 💡
1. Make a model called `Score` with attributes `user_id` (string) and `score` (float)
2. In the 'views.py' file, create the `get_score` API with a GET method
    ```
    @api_view(['GET'])
    def get_score(request):
        scores = Score.objects.all()
        context = {'scores': scores}
        for score in scores: 
            score.score = score.score/25
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
    ``` 
3. In the 'urls.py' file, allow the API to be accesed by the url "url/api/get_score" 
    ```
    path('api/get_score/', get_score, name='get_score'),
    ```
4. In the 'test.py' file, a unit test is written to check if the API is working. The tests can be carried out using the command    `python manage.py test voting_app ` in the terminal, in the 'score_app' folder. 
    ``` 
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
    ```


## Task 2  👨‍💻 
```
Create a simple admin panel where operations staff can use to manage the database:
- a non engineer should be able to view the SQL tables, and search/make queries
- even better if the staff can edit the entries too
```


## Task 3  👨‍💻 



## Bonus Task: Deploy to Cloud ☁️
https://www.youtube.com/watch?v=bE8UllxfFC8



## Bonus Task: Open-ended 🌈


------ It was initially intended to be a voting app. However, this result's app is simpler to build and answers the requirements in a way that is simple and clear.