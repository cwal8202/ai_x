/*class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + self.age
    def eat(self, food):
        print(self.name + '이' + food + '를 먹는다');
    person = Person('홍길동', 20)
    print(person)
    print(person.name, person.age);
*/
const person = {'name':'홍길동', 'age':20};
console.log(person['name'], person['age']);
console.log('person :', person.name, person.age);
const arr = ['홍길동', 20]; // {0:'홍길동', 1:20};
console.log(arr[0], arr[1]);