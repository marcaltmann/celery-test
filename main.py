from celery import Celery

app = Celery('test')

@app.task
def add(x, y): return x + y


def main():
    print("Hello from celery-tests!")


if __name__ == "__main__":
    main()
