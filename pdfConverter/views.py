from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .forms import InputForm, PdfForm
from .models import InputModel, PdfModel
import os, inspect, sys,glob
from pdfConverter.pdf2img_file import convert
import time
from django.core.paginator import Paginator

base_dir = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
file_path = base_dir + '/media/Pdf_uploads/'

# Create your views here.


def Index(request):
	if request.method == 'POST':
		form = InputForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('detail')
	else:
		form = InputForm()
	return render(request, 'index.html', {'form':form})

def DetailListView(request):
	details = InputModel.objects.all().order_by('-id')
	p = Paginator(details, 5)

	page_number = request.GET.get('page')
	try:
		page_obj = p.get_page(page_number)
	except PageNotAnInteger:
		page_obj = p.page(1)
	except EmptyPage:
		page_obj = p.page(p.num_pages)

	context = {'page_obj': page_obj}

	return render(request, 'details.html', context)

def UpdateListView(request, id):
	context = {}
	obj = get_object_or_404(InputModel, id = id)

	form = InputForm(request.POST or None, instance = obj)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/detail/')

	context["form"] = form

	return render(request, "update.html", context)

def DeleteView(request, id):
	context = {}
	obj = get_object_or_404(InputModel, id = id)
	if request.method =="POST":
		obj.delete()
		return HttpResponseRedirect("http://127.0.0.1:8000/detail/")
	
	return render(request, 'delete.html', context)

def PdfConverter(request):
	if request.method == 'POST':
		form = PdfForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			time.sleep(2)
			list_of_files = glob.glob(file_path+'*') # * means all if need specific format then *.csv
			latest_file = max(list_of_files, key=os.path.getctime, default=0)
			if  os.path.exists(latest_file):
				print('latest_file--------->>', latest_file)
				check_ext= latest_file.split('.')[1]
				if 'pdf'== check_ext.lower():
					zip_download_path, zip_create = convert(latest_file)
					print('********** zip_download_path***********', zip_create)
					# os.remove(latest_file)
					context = {'form':form, 'zip_download_path':zip_download_path, 'zip_create': zip_create}
					return render(request, 'pdf_convert.html', context)
	else:
		form = PdfForm()
	
	return render(request, 'pdf_convert.html', {'form':form})

