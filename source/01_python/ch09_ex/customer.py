# customer.py = Customer클래스, to_customer(), load_customer()
class Customer:
    '고객 데이터와 as_dic(), to_list_style(txt백업시), __str__()'
    def __init__(self, name, phone, email, age, grade, etc):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.grade = grade
        self.etc = etc
    def as_dic(self): # 객체를 딕셔너리데이터로 반환 (csv 파일 저장시)
        return self.__dict__
    def to_list_style(self): # 객체를 list return("홍길동, 010-8999-9999, e@e.com, 20, 3, 까칠해")
        return f"{self.name},{self.phone},{self.email},{self.age},{self.grade},{self.etc}"
#         temp = [self.name, self.phone, self.email, str(self.age), str(self.grade), self.etc]
#         return ', '.join(temp)
    def __str__(self): # *** 홍길동 010-8999-9999 e@e.com 20 까칠해
        return "{:>5} {:3} {:13} {:15} {:3} {}".format(self.grade*"*",
                                               self.name,
                                               self.phone,
                                               self.email,
                                               self.age,
                                               self.etc)
    
def to_customer(row): # txt 파일 내용 한줄 홍길동 , 010 8999 9999, e@e.com, 20, 3, 까칠해
    '''
    row = "홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해"(txt파일 내용)을 매개변수로 받아
    Customer 객체로 return
    '''
    result = row.split(',')                  # 을 Customer 객체로 반환
    return Customer(result[0].strip(),
                    result[1].strip(),
                    result[2].strip(),
                    int(result[3].strip()),
                    int(result[4].strip()),
                    result[5].strip())

def load_customers() :
    customer_list = []
    try:
        with open('data/ch09_customers.txt', 'r', encoding='utf-8') as f:
            # txt 데이터 한줄씩 customer 객체로 받아 customer_list.append
            lines = f.readlines()
            for line in lines:
                # line = '홍길동, 010-9999-9999, a@a.com, 30, 3, 까칠해'
                customer = to_customer(line)
                customer_list.append(customer)
    except:
        with open('data/ch09_customers.txt', 'w', encoding='utf-8') as f:
            print('초기화 파일을 생성하였습니다.')
    return customer_list