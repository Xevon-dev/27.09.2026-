from django.shortcuts import render
from django.http import HttpResponse , HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

result_text = ""
feedbacks = []


@csrf_exempt
def arithmetic_sum(request):
    global result_text
    if request.method == "POST":
        a1 = float(request.POST.get("a1"))
        d = float(request.POST.get("d"))
        n = int(request.POST.get("n"))
        S_n = (2 * a1 + d * (n - 1)) * n / 2
        result_text = f"Сума перших {n} членів арифметичної прогресії: {S_n}"
        return redirect("/result/")

    return HttpResponse("""
        <form method="POST">
            a1: <input name="a1"><br>
            d: <input name="d"><br>
            n: <input name="n"><br>
            <button>Обчислити</button>
        </form>
    """)




def result(request):
    return HttpResponse(result_text)



@csrf_exempt
def feedback(request):
    if request.method == "POST":
        feedbacks.append({
            "name": request.POST.get("name"),
            "rating": int(request.POST.get("rating")),
        })
        return redirect("/rating/")

    return HttpResponse("""
        <form method="POST">
            Ім'я: <input name="name"><br>
            Оцінка (1-5): <input name="rating"><br>
            <button>Надіслати</button>
        </form>
    """)


def rating(request):
    total = len(feedbacks)
    text = ""
    for i in range(1, 6):
        count = sum(1 for f in feedbacks if f["rating"] == i)
        text += f"Оцінка {i}: {count}<br>"

    avg = sum(f["rating"] for f in feedbacks) / total if total else 0
    text += f"Середня: {avg}<br>Всього: {total}"
    return HttpResponse(text)