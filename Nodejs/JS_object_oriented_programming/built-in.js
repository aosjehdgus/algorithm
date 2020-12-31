console.log("Math.PI", Math.PI);
console.log("Math.random()", Math.random());

// 객체를 포함해서 함수를 표현할 때는 method 라고 말을 한다.
// 객체에 소속되어 있을 때

console.log("Math.floor(3.9)", Math.floor(3.9));

// 객체 만들어 보기

var MyMath = {
    PI : Math.PI,
    random : function(){
      return Math.random();  
    },
    floor : function(val){
        return Math.floor(val);
    }
}

console.log("MyMath.PI", MyMath.PI);
console.log("MyMath.random()", MyMath.random());
console.log("MyMath.floor(3.9)", MyMath.floor(3.9));

MyMath_PI = Math.PI;
function MyMath_random(){
    return Math.random();
}

function MyMath_floor(val){
    return Math.floor(val);
}