from django.shortcuts import render,redirect
from .forms import ProductAddForm

# Create your views here.
def AddProduct(request):
    if request.method=='POST':
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            image = form.cleaned_data['image']
            with open("./media/" + image.name,'wb+') as destination:
                for chunck in image.chunks():
                    destination.write(chunck)
            return redirect('profile')
    form = ProductAddForm()
    return render(request,'add_product.html',{'form':form})
        