from django.shortcuts import render, redirect
from models import Picture
from models import picture_people
from models import picture_tag

def index(request):
    pictures = Picture.objects.all()
    toppeople = picture_people.objects.all().select_related("picture").order_by("person")
    toptags = picture_tag.objects.all().select_related("picture").order_by("tag")
    toptags = toptags[:4]
    newTop = []
    names = []
    for item in toppeople:
        print(item.person)
        print(item.person not in newTop)
        if item.person != "" and item.person not in names:
            newTop.append(item)
            names.append(item.person)
    toppeople = newTop[:4]
    print(toppeople)
    print(toptags)
    if request.method == 'POST':
        fileupload = request.FILES.get('fileupload')
        tags = request.POST.get('tags')
        people = request.POST.get('people')
        location = request.POST.get('location')
        newPic = Picture(picture = fileupload, location = location)
        newPic.save()
        print(fileupload)
        indTags = tags.split(", ")
        indPeople = people.split(", ")
        print(indTags)
        print(indPeople)
        print(fileupload)
        for item in indTags:
            print(item)
            pic_tag = picture_tag(picture = newPic, tag=item)
            pic_tag.save()
        for item in indPeople:
            pic_people = picture_people(picture=newPic, person=item)
            pic_people.save()
        return redirect(index)
    return render(request, 'pictures/index.html', {'pictures': pictures, 'toppeople': toppeople, 'toptags': toptags,})