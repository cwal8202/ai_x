i = Number('');
console.log('i=', i); // 0
i = parseInt(''); // NaN
console.log('i=', NaN, '- 타입=', typeof(i));
f = 10/3; // 실수인 3.333.... 으로 나옴
console.log('f=', f);
a = 10/0; // => 10/0.0000000000...1 로 나눈 값과 같아서 Infinity가 나옴.
console.log('a=', a, ' - 타입=', typeof(a));

console.log('i가 NaN인지 여부 :', isNaN(i)); // true 
console.log('f가 NaN인지 여부 :', isNaN(f)); // false
console.log('i가 유한수인지 여부 :', isFinite(a)); // false 
console.log('i가 유한수인지 여부 :', isFinite(a)); // true 