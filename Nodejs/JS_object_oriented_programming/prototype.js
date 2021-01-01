function Person(name, first, second, third){

    this.name = name;
    this.first = first;
    this.second = second;
    this.third = third;
  

}

Person.prototype.sum = function(){
    return this.first + this.second + this.third;
} 

var dongle = new Person('dongle', 10, 20, 30);
dongle.sum = function(){
    return 'this : ' +  (this.first + this.second + this.third);
}
var dongri = new Person('dongri', 10, 10, 10);

console.log(dongle.sum());
console.log(dongri.sum());

