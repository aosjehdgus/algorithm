var dongle = {
    name : 'dongle',
    first : 10,
    second : 20,
    sum : function(f,s){
        return f + s;
    }
}

console.log(dongle.sum(dongle.first, dongle.second));

var dongle = {
    name : 'dongle',
    first : 10,
    second : 20,
    sum : function(){
        return dongle.first + dongle.second;
    }
}

console.log(dongle.sum());

var dongle = {
    name : 'dongle',
    first : 10,
    second : 20,
    sum : function(){
        return this.first + this.second;
    }
}

console.log(dongle.sum());


// var kim = {
//     name : 'kim',
//     first : 10,
//     second : 20,
//     sum : function(){
//         return this.first + this.second;
//     }
// }
// console.log(kim.sum());

