# functions.py => fn1() 부터 fn9() 까지
from customer import Customer
# fn1 사용자 입력
def fn1_insert_customer_info() :
    '''
        사용자로부터 name, phone, email, age, grade, etc를 입력받아 customer형 객체 반환
    '''
    import re
    insert_name = input("이름 : ")
    insert_name_pattern = r'([가-힣]{2,})|([a-zA-Z]{3,})'
    while not re.search(insert_name_pattern, insert_name):
        print('이름을 제대로 입력하세요(한글 2글자 이상, 영어 3글자 이상)')
        insert_name = input('이름 : ')
    insert_phone = input("전화번호 : ")
    insert_email = input("이메일 : ")
    while(True) :
        try : 
            insert_age = int(input("나이 : "))
            if not(0<= insert_age <= 130) :
                raise Exception("유효한 나이를 입력하세요(1~130)")
            break
        except Exception as e:
            print(e)
    try : 
        insert_grade = int(input("고객등급(1~5) : "))
        if insert_grade < 1:
            insert_grade = 1
        if insert_grade > 5:
            insert_grade = 5
    except :
            print("유효하지 않은 등급 입력시 1등급으로 초기화")
            insert_grade = 1
    insert_etc = input("기타 정보 : ")
    return Customer(insert_name, insert_phone, insert_email, insert_age, insert_grade, insert_etc)
# fn2 사용자 정보 출력
def fn2_print_customers(customer_list):
    'customer_list를 출력(pdf 40page 스타일)'
    print('=' * 70)
    print('{:^70}'.format('고객 정보'))
    print('-' * 70)
    print('{:>5} {:3} {:13} {:13} {:3} {}'.format('GRADE', '이름', '전화', '메일', '나이', '기타'))
    print('=' * 70)
    for customer in customer_list : 
        print(customer)
    print("=" * 70)

# fn3 삭제 - 동명이인 있을때 선택해서 삭제
def fn3_delete_customer(customer_list):
    del_name = input("삭제할 고객의 이름을 입력하세요")
    del_idx = []
    for idx, customer in enumerate(customer_list) :
        if customer.name == del_name :
            del_idx.append(idx)
    if del_idx :
        for idx in del_idx[::-1] : # 마지막 순번부터 지워야 index 감소해도 삭제가 가능함
            print(customer_list[idx], '지우겠습니까?', end='')
            answer = input('(Y/N)')
            if answer.upper() == 'Y' :
                print("요청하신 {}({})님 삭제하였습니다.".format(del_name, 
                                                             customer_list[idx].phone) )
                del customer_list[idx]
    else :
        print('{}님 데이터는 존재하지 않습니다.'.format(del_name))

# fn4 고객 이름 검색
def fn4_search_customer(customer_list):
    '''
    찾을 이름을 input으로 받아, customer_list에서 검색하여
    같은 이름은 search_list에 append한 후 search_list를 출력
    같은 이름이 없으면 없다고 출력
    '''
    search_name = input("검색할 고객의 이름을 입력하세요")
    search_list = []
    for customer in customer_list :
        if customer.name == search_name :
            search_list.append(customer)
    if search_list :
        fn2_print_customers(search_list)
    else : print("검색한 고객은 존재하지 않습니다.")

# fn5 csv 파일로 내보내기
import csv
def fn5_save_customer_csv(customer_list):
    '매개변수로 받은 customer_list를 딕셔너리리스트로 변환해서 csv 출력'
    if customer_list : 
        customer_dic_list = []
        for customer in customer_list :
            customer_dic_list.append(customer.as_dic())
        fieldnames = list(customer_dic_list[0].keys())
        filename = input('저장할 csv 파일명은?')
        with open('data/{}.csv'.format(filename), 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader() # 헤더
            dict_writer.writerows(customer_dic_list)
            print(f'data/{filename}.csv 내보내기 완료')
    else :
        print("입력된 회원 데이터가 없어 csv 내보내기 취소합니다.")

# fn9 ch09_customers.txt파일 저장 후 프로그램 종료
def fn9_save_customer_txt(customer_list):
    '''
        customer_list를 to_list_style()를 이용해서 ['홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해']
        ch09_customers.txt로 백업
    '''
    customer_txt_list = []
    for customer in customer_list :
        customer_txt_list.append(customer.to_list_style()+'\n')

    with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f :
        f.writelines(customer_txt_list)