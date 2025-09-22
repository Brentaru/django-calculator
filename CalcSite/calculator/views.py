from django.shortcuts import render

# Create your views here.

def index(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    op = request.GET.get("op", "add")

    result = None
    error = ""

    if a is not None and b is not None:
        try:
            x = float(a); y = float(b)
            if   op == "add": result = x + y
            elif op == "sub": result = x - y
            elif op == "mul": result = x * y
            elif op == "div":
                if y == 0: error = "Cannot divide by zero."
                else: result = x / y
            else: error = "Unknown operation."
        except ValueError:
            error = "Please enter valid numbers."

    return render(request, "calculator/index.html",
                  {"a": a, "b": b, "op": op, "result": result, "error": error})