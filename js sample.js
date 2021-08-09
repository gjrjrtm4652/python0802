
//출력하기
/*
 어디로 무엇을 콘솔탭 문자열
*/
console.log('first output');
//화면에 문자열을
document.write('secoond output')

//입력받기
var value = prompt('첫번째 입력','placeholder');
console.log(typeof(value));

var result = Number(value) + 10;
console.log(result);

//scope
var v1;
{
v2 = 2;
let v3;
const v4 = 4;
console.log(v1,v2,v3,v4);
v3 = v1+v2;
console.log(v3);
}
console.log(v2);
arr.pop();
console.log(arr.length);

//여러 개의 데이터들
var csv =',,,,,,';
var qry ='name=value&parm=11&loc=kr';
var json ='{name:value, parm:11,loc:[kr,en]}';
var obj ={
    name : 'jang',
    method : function(){},
};
obj.name;
obj.method();