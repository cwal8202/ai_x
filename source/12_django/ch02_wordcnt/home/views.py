from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request) :
    context = {
        'msg':'wordCount welcome Page',
        'greeting':'Hello, Django(장고)',
    }
    return render(request=request,
                  template_name='home/index.html',
                  context=context)

def test(request) :
    return HttpResponse('''<h1>테스트 페이지</h1>
        <button onclick="location='/'">처음으로</button>
''')

def showIntId(request:HttpRequest, id:int):
    msg = "숫자 ID는 " + str(id)
    msg = f"숫자 ID는 {id}"
    id_type = "int입니다."
    return render(request, 
                  "home/showId.html", 
                  {'msg':msg, 'type':id_type})

def showStrId(request:HttpRequest, id:str):
    msg = "문자 ID는 " + id
    msg = f"문자 ID는 {id}"
    id_type = "str입니다."
    return render(request, 
                  "home/showId.html", 
                  {'msg':msg, 'type':id_type})

def web(request) :
    context = {
        'age_list': ['20', '30', '40', '50', '60이상'],
        'gender_list': ['남', '여'],
        'family_list': ['1인 가구', '부모동거', '부부', '자녀1명', '자녀2명 이상', '기타'],
        'preference_list': ['통조림/즉석/선물', '생수/음료/커피', '과자/비엔/베이커리', '냉장/냉동/건조식', '유제품', '건강식품'],
        'value_list': ['VIP', '우수고객', '정확우수고객', '신고객', '잠재이탈고객', '이탈/휴면고객'],
        'lifestyle_list': ['트렌드추종', '가격민감', '브랜드선호', '건강지향'],
    }
    return render(request, "home/test.html", context)
