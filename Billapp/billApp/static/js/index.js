var item_prices = [];
var amount = 0;
function bill(item){
  var ids = [];
  var values = [];
  var counts = [];
  var quan = 0;
  var val_id = item.id.slice(0,item.id.length-2);
  item.onclick = () =>{
    quan ++;
    //console.log(`Quan is ${quan}`);
    let val_id = item.id.slice(0,item.id.length-2);
    let price = document.getElementById(val_id).innerText
    // //console.log(document.getElementById(val_id).innerText);
      amount += parseInt(price);
      //amount.toFixed(2);
     document.getElementById("a"+val_id.slice(val_id.length-1)).innerHTML = price * quan;
     
     //console.log(document.getElementById("customer").innerHTML);
     
    if ((amount > 10000) && (document.getElementById("customer").innerHTML !== "")){
       console.log("Registered Customer Checking Out!");
       let cash = amount * (0.012);
       amount = amount - cash
       document.getElementById("amount").innerHTML = Math.floor(amount) + " with cash benefits worth " + Math.floor(cash);

     }
     try{
      if ((amount > 10000) && document.getElementById("customer").innerHTML ===""){
       console.log("Unregistered")
      amount = amount - ((0.01)*amount);
      document.getElementById("amount").innerHTML = Math.floor(amount) + " with 1% discount";
    }
    if (amount < 10000){
      document.getElementById("amount").innerHTML = Math.floor(amount);
     }
  }
    catch(error){
      console.log("Unregistered")
      amount = amount - ((0.01)*amount);
      document.getElementById("amount").innerHTML = Math.floor(amount) + " with 1% discount";
    }
  }
}