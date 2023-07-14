"""views.py"""
import sys
from subprocess import PIPE, run

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def home(request):
    """Home page"""
    return render(request, "home.html")


def filter_selection(request):
    """Filter selection"""
    img = request.FILES["image"]
    _fs = FileSystemStorage()
    _fs.delete("temp.jpeg")
    filename = _fs.save("temp.jpeg", img)
    fileurl = _fs.url(filename)
    return render(request, "filter_selection.html", {"raw_image": fileurl})


def result(request):
    """Result page"""
    _filter = request.POST.get("filter")
    _fs = FileSystemStorage()
    filename = "temp.jpeg"
    fullurl = _fs.open(filename)
    fileurl = _fs.url(filename)
    res = run(
        [sys.executable, "templates//filter.py", str(fullurl), str(filename), _filter],
        shell=False,
        stdout=PIPE,
        check=True,
    )
    resurl = _fs.url(str(res.stdout).split("'")[1])
    return render(
        request, "result.html", {"raw_image": fileurl, "processed_image": resurl}
    )
