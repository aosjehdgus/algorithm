// var memberArray = ['dongle', 'dongri', 'donghyun'];
// console.group('array loop');
// var i  = 0;
// while(i < memberArray.length){
//     console.log(i, memberArray[i]);    
//     i = i + 1;
// }
// console.groupEnd('array loop');

console.group('object loop');

var memberObject = {
    developer :'dongle',
    manager : 'dongri',
    designer : 'donghyun'
}

for(role in memberObject){
    console.log(role, memberObject[role]);

}

console.groupEnd('object loop');

// 객체가 반복적으로 실행될 때마다 그 순번에 해당되는 원소의 이름이 주입될 변수가 온다.
// 포인문이라고 한다. 이 객체가 갖고 있는 원소의 값만큼 {}(중괄호)안의 코드가 실행 된다.



// 객체에서 값에 접근 할 때는 . 을 사용한다.


// delete memberObject.manager
// console.log("memberObject.manager", memberObject.manager);

// console.log("memberObject.designer", memberObject.designer);

// // 객체에서도 []를 통해서 값에 접근 할 수 있다.

// console.log("memberObject['designer']", memberObject['designer']);


// //수정할 때 memberObject.designer = 'kdh';



