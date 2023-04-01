# Student's Result Announcement App 👨‍🏫 
This app is created as a take-home coding challenge by Pacer. The following tasks are requirements that are in the challenge, and these are my attempts to meet these requirements. 

The idea of this app is to simply display the results of students. A simple app like this is made in hopes to maintain simplicity and effectiveness of the answers.


## Task 1  👨‍💻 
Create a simple Python Django app that has the following features:
- a backend API endpoint called get_score with a simple dummy formula that could
  be anything e.g. result = input + 1
- a PostgreSQL database that the backend API uses to log the user ID and the score
- demonstrate that the endpoint is behaving as expected (how do we test it? how can
  we prove that it is working as expected?)
    
Solution 💡
1. Make a model called `Score` with attributes `user_id` (string) and `score` (float)
2. In the **'views.py'** file, create the `get_score` API with a GET method
    ```python
    @api_view(['GET'])
    def get_score(request):
        scores = Score.objects.all()
        context = {'scores': scores}
        for score in scores: 
            score.score = score.score/25
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
    ``` 
3. In the **'urls.py'** file, allow the API to be accesed by the url **"url/api/get_score"** 
    ```python
    path('api/get_score/', get_score, name='get_score'),
    ```
4. In the **'test.py'** file, a unit test is written to check if the API is working. The tests can be carried out using the command `python manage.py test voting_app ` in the terminal, in the **'score_app'** folder. 
    ```python
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
Create a simple admin panel where operations staff can use to manage the database:
- a non engineer should be able to view the SQL tables, and search/make queries
- even better if the staff can edit the entries too

Solution 💡
1. In the **'admin.py'** file, this code is there to structure the admin page. The admin panel displays the `user_id` and `score`, along with a search bar that searches `user_id`.
    ```python
    class ScoreAdmin(admin.ModelAdmin): 
        fieldsets =  [
            (None, {'fields': ['user_id','score']}),
        ]
        list_display=('user_id', 'score')
        search_fields = ['user_id']

    admin.site.register(Score, ScoreAdmin)
    ```
2. There is a Button in the front page that allows users to enter the admin panel, and manipulate the data given that they have the credentials. 



## Task 3  👨‍💻 
If we want to change the schema of the database, say we want to add, edit, or remove
columns:
- demonstrate a process or script, or a demo video of the schema update process
- demonstrate that the endpoints and the services are not affected, and the tests are
  running fine

Solution 💡
1. In the **'models.py'** file, add an additional field to `Score`
    ```python
    class Score(models.Model):
        user_id = models.CharField(max_length=255)
        score = models.FloatField()
        created_at = models.DateTimeField(auto_now_add=True)
    ```
    add `dummy = models.IntegerField(default=None, blank=True, null=True)`
    ```python
    class Score(models.Model):
        user_id = models.CharField(max_length=255)
        score = models.FloatField()
        dummy = models.IntegerField(default=None, blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
    ```
2. In the terminal, run:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
3. Perform the unit test in the terminal: 
    ```
    python manage.py test voting_app
    ```
    The results should look like: 
    ```
    Found 2 test(s).
    System check identified no issues (0 silenced).
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.054s

    OK
    ```
4. Here's a link to the video demonstration: 
    **https://youtu.be/iluPpjBQQTA**



## Bonus Task: Deploy to Cloud ☁️

https://www.youtube.com/watch?v=bE8UllxfFC8



## Bonus Task: Open-ended 🌈
Bonus Task: Open-ended!
If you have specific strengths in certain areas, feel free to demonstrate it. We are a
company that incorporates games, data, and web3. There of opportunities to expand
upon your work!

Solution 💡
1. Beautified the front end to display the scores nicely
2. Added a 'Get Scores (JSON)' button to view the scores in the JSON format using the `get_score` API
3. Added an 'Admin' button to allow easy access to the admin page.

PS[^1]
[^1]: It was initially intended to be a voting app. However, this result's app is simpler to build and answers the requirements in a way that is simple and clear.