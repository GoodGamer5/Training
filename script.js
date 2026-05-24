
// const persons = new Object({
//   name: "John",
//   age: 30,
//   city: "New York",
//   sayHello: function(job) {
//     console.group("Person Details:");
//     console.log("Hello, my name is " + this.name);
//     console.log("I am " + this.age + " years old.");
//     console.log(`My job is ${job}.`);
//    console.groupEnd();
//   }
// });
// const person = new Object({
//   name: "Alice",
//   age: 25,
//   city: "Los Angeles"
// });
// // Object.prototype.sayHello = function() {
// //   console.log("Hello, my name is " + this.name);
// // }; 

//  persons.sayHello.bind(person, "developer")();
//  persons.sayHello.call(person, "developer");
//  persons.sayHello.apply(person, ["developer"]);


//  const names = ["anna", "bob", "carl"];
// const upperCaseNames = names.map(names => names.toUpperCase());

// const ages = [12, 25, 17, 30, 15, 22];
// const adults = ages.filter(ages => ages >= 18);

// const prices = [100, 200, 350, 80];
// const salesPrices = prices.map(price => price - price * 0.1);
// console.log(salesPrices);

// const users = [
//   { name: "Алекс", active: true },
//   { name: "Мария", active: false },
//   { name: "Иван", active: true },
// ];
// const activeUsers = users.filter(user => user.active);
// const activeUserNames = activeUsers.map(user => user.name);
// console.log(activeUsers);
// console.log(activeUserNames);

// const cart = [
//   { item: "меч", price: 150 },
//   { item: "щит", price: 200 },
//   { item: "зелье", price: 50 },
// ];
// const totalPrice = cart.reduce((total, element) => total + element.price, 0);
// console.log(totalPrice);

// const colors = ["red", "green", "blue"];
// const [firstColor, secondColor] = colors;
// console.log(firstColor, secondColor);

// const user = { name: "Иван", age: 25, city: "Москва" };
// const {name, city} = user;
// console.log(name, city);

// const product = { title: "Меч", price: 150, inStock: true };

// // Перепиши функцию используя деструктуризацию в параметре
// function getInfo() {
//   const { title, price } = product;
//   return `${title} стоит ${price}`;
// }
// console.log(getInfo()); 
// const hero = {
//   name: "Артас",
//   stats: {
//     hp: 500,
//     damage: 80
//   }
// };
// const {name, stats:{hp}} = hero;
// console.log(hp, name);
// const config = { w: 1920, h: 1080 };
// const {w: width, h: height} = config;
// console.log(width, height);
// const fruits = ["яблоко", "банан"];
// const moreFruits = ["манго", "киви"];
// // Объедини оба массива в один
// // Результат: ["яблоко", "банан", "манго", "киви"]
// const allFruits = [...fruits, ...moreFruits];
// console.log(allFruits);
// const base = { hp: 100, damage: 20 };
// const bonus = { armor: 15, speed: 10 };
// const stats = { ...base, ...bonus };
// console.log(stats);
// const original = [1, 2, 3];
// const copy = [...original, 4];
// console.log(copy);
// console.log(original);
// const user = { name: "Иван", age: 25, city: "Москва" };
// const updatedUser = { ...user, age: 26 };
// console.log(updatedUser);
// const numbers = [3, 1, 4, 1, 5, 9, 2];
// const maxNumber = Math.max(...numbers);
// console.log(maxNumber);