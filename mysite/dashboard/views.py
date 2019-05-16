from django.shortcuts import render
from .models import *

from django.http import Http404, JsonResponse
# Create your views here.

def dashboard(request):
    return render(request, 'landing/index.html')

def dash(request):
    return render(request, 'dash/dash.html')

def table(request):
    return render(request, 'table/table.html')

def test(request):
    return render(request, 'test/test.html')

def dashboardgr(request):
    return render(request, 'dashboard/dashboard.html')


def fridge(request):
    return render(request, 'graphs/Fridge.html')

def redshelf(request):
    return render(request, 'graphs/RedShelf.html')

def panorama(request):
    return render(request, 'graphs/Panorama.html')




def display_data(request):
    div_arr = []
    items = ColaFridge.objects.all()


    for item in items:
        if item.label == "cap":
            div_arr.append(float(item.diagonals))
    div_arr = sorted(div_arr, reverse=True)
    context = {
    'div_arr': div_arr,
        'items': items,

    }

    return render(request, 'table/table.html', context)

def add_ajax(request):
    if request.is_ajax():
        items = ColaFridge.objects.all()
        #len_d = []
#diagonals
        div_arr = []
        div_arr_cap_fan = []
        div_arr_cap_spr = []

        div_arr_l = []
        div_arr_l_fan = []
        div_arr_l_spr = []

        div_arr_b = []
        div_arr_b_fan = []
        div_arr_b_spr = []
#sides
        s_arr = []
        s_arr_cap_fan = []
        s_arr_cap_spr = []

        s_arr_l = []
        s_arr_l_fan = []
        s_arr_l_spr = []

        s_arr_b = []
        s_arr_b_fan = []
        s_arr_b_spr = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr.append(float(item.diagonals))
                s_arr.append(float(item.sides))
            if item.label == "label":
                div_arr_l.append(float(item.diagonals))
                s_arr_l.append(float(item.sides))

            if item.label == "cap_fanta":
                div_arr_cap_fan.append(float(item.diagonals))
                s_arr_cap_fan.append(float(item.sides))

            if item.label == "cap_sprite":
                div_arr_cap_spr.append(float(item.diagonals))
                s_arr_cap_spr.append(float(item.sides))

            if item.label == "label_fanta":
                div_arr_l_fan.append(float(item.diagonals))
                s_arr_l_fan.append(float(item.sides))

            if item.label == "label_sprite":
                div_arr_l_spr.append(float(item.diagonals))
                s_arr_l_spr.append(float(item.sides))

            if item.label == "bottle0.5L":
                div_arr_b.append(float(item.diagonals))
                s_arr_b.append(float(item.sides))

            if item.label == "bottle0.5L_fanta":
                div_arr_b_fan.append(float(item.diagonals))
                s_arr_b_fan.append(float(item.sides))

            if item.label == "bottle0.5L_sprite":
                div_arr_b_spr.append(float(item.diagonals))
                s_arr_b_spr.append(float(item.sides))

        div_arr = sorted(div_arr, reverse=True)
        div_arr_l = sorted(div_arr_l, reverse=True)
        div_arr_cap_fan = sorted(div_arr_cap_fan, reverse=True)
        div_arr_cap_spr = sorted(div_arr_cap_spr, reverse=True)
        div_arr_l_fan = sorted(div_arr_l_fan, reverse=True)
        div_arr_l_spr = sorted(div_arr_l_spr, reverse=True)
        div_arr_b = sorted(div_arr_b, reverse=True)
        div_arr_b_fan = sorted(div_arr_b_fan, reverse=True)
        div_arr_b_spr = sorted(div_arr_b_spr, reverse=True)

        s_arr = sorted(s_arr, reverse=True)
        s_arr_l = sorted(s_arr_l, reverse=True)
        s_arr_cap_fan = sorted(s_arr_cap_fan, reverse=True)
        s_arr_cap_spr = sorted(s_arr_cap_spr, reverse=True)
        s_arr_l_fan = sorted(s_arr_l_fan, reverse=True)
        s_arr_l_spr = sorted(s_arr_l_spr, reverse=True)
        s_arr_b = sorted(s_arr_b, reverse=True)
        s_arr_b_fan = sorted(s_arr_b_fan, reverse=True)
        s_arr_b_spr = sorted(s_arr_b_spr, reverse=True)


        len_cap = []
        len_cap_fan = []
        len_cap_spr = []
        len_l  = []
        len_l_fan = []
        len_l_spr = []
        len_b = []
        len_b_fan = []
        len_b_spr = []


        for i in range(1,len(div_arr)):
            len_cap.append(i)
        for i in range(1,len(div_arr_l)):
            len_l.append(i)
        for i in range(1,len(div_arr_cap_fan)):
            len_cap_fan.append(i)
        for i in range(1,len(div_arr_cap_spr)):
            len_cap_spr.append(i)
        for i in range(1,len(div_arr_l_fan)):
            len_l_fan.append(i)
        for i in range(1,len(div_arr_l_spr)):
            len_l_spr.append(i)
        for i in range(1,len(div_arr_b)):
            len_b.append(i)
        for i in range(1,len(div_arr_b_fan)):
            len_b_fan.append(i)
        for i in range(1,len(div_arr_b_spr)):
            len_b_spr.append(i)

        a = len_cap[-1]
        b = len_l[-1]
        c = len_cap_fan[-1]
        d = len_cap_spr[-1]
        e = len_l_fan[-1]
        j = len_l_spr[-1]
        z = len_b[-1]
        u = len_b_fan[-1]
        i = len_b_spr[-1]


        co_data = [a,b,c,d,e,j,z,u,i]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'div_arr': div_arr,
                'len_d': len_cap,
                'div_arr_l': div_arr_l,
                'div_arr_cap_fan': div_arr_cap_fan,
                'div_arr_cap_spr': div_arr_cap_spr,
                'div_arr_l_fan': div_arr_l_fan,
                'div_arr_l_spr': div_arr_l_spr,
                'div_arr_b ': div_arr_b,
                'div_arr_b_fan': div_arr_b_fan,
                'div_arr_b_spr': div_arr_b_spr,

                's_arr': s_arr,
                's_arr_l': s_arr_l,
                's_arr_cap_fan': s_arr_cap_fan,
                's_arr_cap_spr':s_arr_cap_spr,
                's_arr_l_fan':s_arr_l_fan,
                's_arr_l_spr': s_arr_l_spr,
                's_arr_b ': s_arr_b,
                's_arr_b_fan': s_arr_b_fan,
                's_arr_b_spr': s_arr_b_spr,



            }
        return JsonResponse(response)
    else:
        raise Http404



def add_ajaxtwo(request):
    if request.is_ajax():
        items = ColaRedShelf.objects.all()
        #len_d = []
#diagonals
        div_arr_cap = []
        div_arr_l = []
        div_arr_b_one = []
        div_arr_b_pol = []
        div_arr_b_two = []
#sides
        s_arr_cap = []
        s_arr_l = []
        s_arr_b_one = []
        s_arr_b_pol = []
        s_arr_b_two = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr_cap.append(float(item.diagonals))
                s_arr_cap.append(float(item.sides))
            if item.label == "label":
                div_arr_l.append(float(item.diagonals))
                s_arr_l.append(float(item.sides))

            if item.label == "bottle1L":
                div_arr_b_one.append(float(item.diagonals))
                s_arr_b_one.append(float(item.sides))

            if item.label == "bottle1.5L":
                div_arr_b_pol.append(float(item.diagonals))
                s_arr_b_pol.append(float(item.sides))

            if item.label == "bottle2L":
                div_arr_b_two.append(float(item.diagonals))
                s_arr_b_two.append(float(item.sides))


        div_arr_cap = sorted(div_arr_cap, reverse=True)
        div_arr_l = sorted(div_arr_l, reverse=True)
        div_arr_b_one = sorted(div_arr_b_one, reverse=True)
        div_arr_b_pol = sorted(div_arr_b_pol, reverse=True)
        div_arr_b_two = sorted(div_arr_b_two, reverse=True)


        s_arr_cap = sorted(s_arr_cap, reverse=True)
        s_arr_l = sorted(s_arr_l, reverse=True)
        s_arr_b_one = sorted(s_arr_b_one, reverse=True)
        s_arr_b_pol = sorted(s_arr_b_pol, reverse=True)
        s_arr_b_two = sorted(s_arr_b_two, reverse=True)


        len_cap = []
        len_l = []
        len_b_one = []
        len_b_pol  = []
        len_b_two = []



        for i in range(1,len(div_arr_cap)):
            len_cap.append(i)
        for i in range(1,len(div_arr_l)):
            len_l.append(i)
        for i in range(1,len(div_arr_b_one)):
            len_b_one.append(i)
        for i in range(1,len(div_arr_b_pol)):
            len_b_pol.append(i)
        for i in range(1,len(div_arr_b_two)):
            len_b_two.append(i)

        a = len_cap[-1]
        b = len_l[-1]
        c = len_b_one[-1]
        d = len_b_pol[-1]
        e = len_b_two[-1]



        co_data = [a,b,c,d,e]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'len_d': len_cap,

                'div_arr_cap': div_arr_cap,
                'div_arr_l': div_arr_l,
                'div_arr_b_one': div_arr_b_one,
                'div_arr_b_pol': div_arr_b_pol,
                'div_arr_b_two': div_arr_b_two,

                's_arr_cap': s_arr_cap,
                's_arr_l': s_arr_l,
                's_arr_b_one': s_arr_b_one,
                's_arr_b_pol':s_arr_b_pol,
                's_arr_b_two':s_arr_b_two,


            }
        return JsonResponse(response)
    else:
        raise Http404



def add_ajaxthree(request):
    if request.is_ajax():
        items = Panorama.objects.all()
        #len_d = []
#diagonals
        div_arr_cap = []
        div_arr_l = []
        div_arr_b_one = []
        div_arr_b_pol = []
        div_arr_b_two = []
#sides
        s_arr_cap = []
        s_arr_l = []
        s_arr_b_one = []
        s_arr_b_pol = []
        s_arr_b_two = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr_cap.append(float(item.diagonals))
                s_arr_cap.append(float(item.sides))
            if item.label == "label":
                div_arr_l.append(float(item.diagonals))
                s_arr_l.append(float(item.sides))

            if item.label == "bottle1L":
                div_arr_b_one.append(float(item.diagonals))
                s_arr_b_one.append(float(item.sides))

            if item.label == "bottle1.5L":
                div_arr_b_pol.append(float(item.diagonals))
                s_arr_b_pol.append(float(item.sides))

            if item.label == "bottle2L":
                div_arr_b_two.append(float(item.diagonals))
                s_arr_b_two.append(float(item.sides))


        div_arr_cap = sorted(div_arr_cap, reverse=True)
        div_arr_l = sorted(div_arr_l, reverse=True)
        div_arr_b_one = sorted(div_arr_b_one, reverse=True)
        div_arr_b_pol = sorted(div_arr_b_pol, reverse=True)
        div_arr_b_two = sorted(div_arr_b_two, reverse=True)


        s_arr_cap = sorted(s_arr_cap, reverse=True)
        s_arr_l = sorted(s_arr_l, reverse=True)
        s_arr_b_one = sorted(s_arr_b_one, reverse=True)
        s_arr_b_pol = sorted(s_arr_b_pol, reverse=True)
        s_arr_b_two = sorted(s_arr_b_two, reverse=True)


        len_cap = []
        len_l = []
        len_b_one = []
        len_b_pol  = []
        len_b_two = []



        for i in range(1,len(div_arr_cap)):
            len_cap.append(i)
        for i in range(1,len(div_arr_l)):
            len_l.append(i)
        for i in range(1,len(div_arr_b_one)):
            len_b_one.append(i)
        for i in range(1,len(div_arr_b_pol)):
            len_b_pol.append(i)
        for i in range(1,len(div_arr_b_two)):
            len_b_two.append(i)

        a = len_cap[-1]
        b = len_l[-1]
        c = len_b_one[-1]
        d = len_b_pol[-1]
        e = len_b_two[-1]



        co_data = [a,b,c,d,e]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'len_d': len_cap,

                'div_arr_cap': div_arr_cap,
                'div_arr_l': div_arr_l,
                'div_arr_b_one': div_arr_b_one,
                'div_arr_b_pol': div_arr_b_pol,
                'div_arr_b_two': div_arr_b_two,

                's_arr_cap': s_arr_cap,
                's_arr_l': s_arr_l,
                's_arr_b_one': s_arr_b_one,
                's_arr_b_pol':s_arr_b_pol,
                's_arr_b_two':s_arr_b_two,


            }
        return JsonResponse(response)
    else:
        raise Http404
