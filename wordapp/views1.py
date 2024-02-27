from django.shortcuts import render,redirect
import pymysql
from django.http import JsonResponse
from wordapp import shuju
# Create your views here.

def wordlist(request):
    sql='select * from word01'
    conn = pymysql.connect(
        user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
        password="123456",
        host='localhost',
        database='nano',
        port=3306,
    )
    try:
        cursor = conn.cursor()
        result = cursor.execute(sql)
        a=cursor.fetchall()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    if request.method=='GET':
        return render(request, 'wordhome.html', locals())
    else:
        dic={'shoucang':[]}

        for i in a:
            if i[3]=='2':
                dic['shoucang'].append(i[0])
        return JsonResponse(dic)


def detailword(request,id):
    id=int(id)
    sql = f'select * from word01 where id={id}'
    conn = pymysql.connect(
        user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
        password="123456",
        host='localhost',
        database='nano',
        port=3306,
    )
    try:
        cursor = conn.cursor()
        result = cursor.execute(sql)
        a = cursor.fetchall()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    if request.method=='GET':
        xxx=a[0][1].strip()
        id=a[0][0]
        src=f'/static/{xxx}.mp3'
        return render(request,'detailword.html',locals())
    else:
        dic={}
        dic['id']=a[0][0]
        dic['word']=a[0][1]
        dic['fanyi']=a[0][2]
        dic['biaoji']=a[0][3]
        src=f'/static/{a[0][1].strip()}.mp3'
        dic['src']=src
        print(dic)
        return JsonResponse(dic)
def redetailword(request,id):
    return redirect(f'/detailword/{id}/')

def change(request):
    if request.method=="POST":
        if request.POST.get('i'):
            if int(request.POST.get('i'))==1:
                id=request.POST.get('id')
                print('id',id)
                sql = f'update word01 set biaoji=2 where id={id}'
                a=shuju.change(sql)
                print(a)
                print('变成2了')
            else:
                id = request.POST.get('id')
                print(id)
                sql = f'update word01 set biaoji=1 where id={id}'
                shuju.change(sql)
                print('变成1了')
            print('ok了')
            return JsonResponse({})
        else:
            try:
                id=request.POST.get('id')
                print(id)
                if request.POST.get('d'):
                    sql = f'update word01 set biaoji=1 where id={id}'
                else:
                    sql = f'update word01 set biaoji=2 where id={id}'
                conn = pymysql.connect(
                    user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
                    password="123456",
                    host='localhost',
                    database='nano',
                    port=3306,
                )
                try:
                    cursor = conn.cursor()
                    result = cursor.execute(sql)
                    conn.commit()
                    print('修改了')

                except Exception as e:
                    print(e)
                    conn.rollback()
                    return JsonResponse({'msg': 'bad'})
                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()
                return JsonResponse({'msg': 'ok'})
            except:
                return JsonResponse({'msg':'bad'})
