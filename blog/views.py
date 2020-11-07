from django.shortcuts import render
from django.utils import timezone
from .models import LectureList, EnrollList
from .forms import EnrollForm

def schedule_list(request) :
    template_name = 'blog/post_list.html'
    lecture_list = LectureList.objects.all()
    enroll_list  = EnrollList.objects.all()
    if request.method == "POST" :
        search = request.POST['search']
        return  render(request, template_name,  {"search" : search, "lecture_list" :  lecture_list, "enroll_list" : enroll_list, "num" : ["one", "two", "three", "four"], "day" : ["월", "화", "수", "목", "금"]})
    else :
        return  render(request, template_name,  {"search" : "", "lecture_list" :  lecture_list, "enroll_list" : enroll_list, "num" : ["one", "two", "three", "four"], "day" : ["월", "화", "수", "목", "금"]})

def enroll_post(request) :
    op = request.GET['op']
    print(op)

    #enroll
    if op == "insert" :
        lec_id = request.GET['code']
        template_name = 'blog/insert.html'
        lecture_list = LectureList.objects.all()
        enroll_list  = EnrollList.objects.all()
        lec_info = 1
        for l in lecture_list :
            if l.code == lec_id :
                res = l
                break
        for l in enroll_list :
            if int(l.lecture_info.split('-')[1]) >= lec_info :
                lec_info = int(l.lecture_info.split('-')[1]) + 1
        if lec_info < 10 :
            lec_i = "lecture" + "-" + "0" + str(lec_info)
        else :
            lec_i = "lecture" + "-" + str(lec_info)
        ins = EnrollList(code=res.code, lecture=res.lecture, prof=res.prof, location=res.location, start=res.start, end=res.end, day=res.day, lecture_info=lec_i)
        for l in enroll_list :
            if l.code == ins.code :
                return render(request, template_name,  {"message": "Already Enrolled", "lecture" : ins.lecture})

            if int(l.start) <= int(ins.start) and int(l.end) > int(ins.start) and bool(set(ins.day).intersection(set(l.day))):
                return render(request, template_name,  {"message": "Time overlap", "lecture" : ins.lecture})
        ins.save()
        return  render(request, template_name,  {"message": "Successfully Enrolled", "lecture" : ins})
    if op == "delete" :
        lec_id = request.GET['code']
        template_name = 'blog/delete.html'
        lecture_list = LectureList.objects.all()
        enroll_list  = EnrollList.objects.all()
        lec_info = ""
        lec_max = "lecture-00"
        for l in enroll_list :
            lec_max = l
            if l.code == lec_id :
                lec_info = l.lecture_info
        for l in enroll_list :
            if int(lec_max.lecture_info.split('-')[1]) < int(l.lecture_info.split('-')[1]) :
                lec_max = l

        ins = EnrollList(code=lec_max.code, lecture=lec_max.lecture, prof=lec_max.prof, location=lec_max.location, start=lec_max.start, end=lec_max.end, day=lec_max.day, lecture_info=lec_info)
        ins.save()
        EnrollList.objects.filter(code=lec_id).delete()
        EnrollList.objects.filter(lecture_info=lec_max.lecture_info).delete()
        return  render(request, template_name,  {"message": "Successfully Deleted", "lecture" : lec_id})

def enroll_memo(request) :
    template_name = 'blog/memo.html'
    op = request.GET['op']
    lec_code = request.GET['code']
    enroll_list  = EnrollList.objects.all()
    if op == "insert" :
        title = request.POST['title']
        des= request.POST['description']
        for l in enroll_list :
            if l.code == lec_code :
                res = l
                break
        ins = EnrollList(code=res.code, lecture=res.lecture, prof=res.prof, location=res.location, start=res.start, end=res.end, day=res.day, lecture_info=res.lecture_info, memo=title, description=des)
        EnrollList.objects.filter(code=lec_code).delete()
        ins.save()
        return  render(request, template_name,  {"message": "Successfully updated", "lecture" : ins})
    if op == "delete" :
        for l in enroll_list :
            if l.code == lec_code :
                res = l
                break
        ins = EnrollList(code=res.code, lecture=res.lecture, prof=res.prof, location=res.location, start=res.start, end=res.end, day=res.day, lecture_info=res.lecture_info)
        EnrollList.objects.filter(code=lec_code).delete()
        ins.save()
        return  render(request, template_name,  {"message": "Successfully deleted", "lecture" : ins})
