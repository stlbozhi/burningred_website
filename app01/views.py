from django.shortcuts import render,redirect
import time

from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.conf import settings
import os
# Create your views here.

def homepage(request):
    try:
        with open('./save_img_file.txt','r') as f:
            content=f.read()
    except:
        content=''
    if content=='':
        content_list=''
    else:

        content_list=content.split('\n')
        content_list=list(filter(None,content_list))
    path = settings.IMG_UPLOAD
    return render(request,"home.html",locals())

def add_img(request):
    img=request.FILES.get('img')
    img_name=img.name
    mobile=os.path.splitext(img_name)[0]
    ext=os.path.splitext(img_name)[1]
    img_name=mobile+str(time.time())+ext
    img_path=os.path.join(settings.IMG_UPLOAD,img_name)
    with open('./save_img_file.txt','a+') as f:
        f.write(img_name+'\n')
        f.seek(0)
        content=f.read()
        print(content)

    content_list=content.split('\n')
    content_list=list(filter(None,content_list))
    with open(img_path,'ab') as fp:
        for chunk in img.chunks():
            fp.write(chunk)
    path=settings.IMG_UPLOAD
    return redirect("/home/",locals())

def delete_img(request):
    name=request.POST.get('name')
    file_name=os.path.join(settings.IMG_UPLOAD,name)
    print(file_name)
    os.remove(file_name)
    with open('./save_img_file.txt', 'r') as f:
        content=f.read()

    content_list=content.split('\n')
    for i in content_list:
        if name==i:
            content_list.remove(i)

        with open('./save_img_file.txt',"w") as f:
            for i in content_list:
                f.write(i+'\n')

    return JsonResponse({'msg': 'ok'})




def home1(request):
    return render(request,"home1.html",locals())

def word(request):
    return render(request,"word.html",locals())

def download_find(request):
    a='f:/'
    lis=os.listdir(a)
    return render(request,"download_find.html",locals())

def download_find1(request):
    try:

        a=request.POST.get('name')

        lis=os.listdir(a)
        le=str(len(lis))
        dic={}
        j=0
        for i in lis:
            dic[j]=i
            j+=1

        return JsonResponse({'msg':dic,'le':le})
    except:
        return JsonResponse({'msg': 'bad'})


def download_resume_appendix(request,src):
    """
    下载文件
    """
    file_path=src
    print(file_path)
    # file_path=request.POST.get('src')
    f=open(file_path,'rb')
    try:

        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise Http404