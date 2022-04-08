from locust import HttpUser, task

class PerformanceTest(HttpUser):
    @task(6)
    def index(self):
        self.client.get("/", data={"email": "kate@shelifts.co.uk"})

    @task(6)
    def purchase(self):
        self.client.post("/purchasePlaces", data={"club": "Iron Temple", "competition": "Spring Festival", "places": 0})