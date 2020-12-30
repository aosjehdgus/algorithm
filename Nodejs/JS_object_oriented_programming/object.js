// 배열에서는 값에 접근 할 때 []를 사용했다.

var memberArray = ['dongle', 'dongri', 'donghyun'];
console.log("memberArray[1]", memberArray[1]);

// 객체에서 값에 접근 할 때는 . 을 사용한다.

var memberObject = {
    developer :'dongle',
    manager : 'dongri',
    designer : 'donghyun'
}
delete memberObject.manager
console.log("memberObject.manager", memberObject.manager);

console.log("memberObject.designer", memberObject.designer);

// 객체에서도 []를 통해서 값에 접근 할 수 있다.

console.log("memberObject['designer']", memberObject['designer']);


//수정할 때 memberObject.designer = 'kdh';



