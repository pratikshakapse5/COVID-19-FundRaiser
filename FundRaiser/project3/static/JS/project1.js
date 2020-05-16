function initBoard() {
  document.getElementById("r1c3").firstChild.focus();
}

function newGame() {
  let table = document.getElementById("t1");
  let inputs = table.getElementsByTagName("input");
  for (let i=0; i < inputs.length; i++) {
    if (!inputs[i].disabled) {
      inputs[i].value = "";
    }
  }
  initBoard();
}

function checkCellValid(cell) {
  let value = parseInt(cell.value);
  let isValid = (Number.isInteger(value) && value >= 1 && value <=9);
  if (isValid) {
    cell.style.color = "green";
    cell.blur();
  }
  else
  cell.value = "";
}
function a(){
var b= document.getElementById("ccnum").value;
if (check(b)){
   document.getElementById("ccnum").style.border = "1px solid black";
   document.getElementById("ccnum").setCustomValidity("");
    return true;
}
else {
    document.getElementById("ccnum").style.border = "2px dashed red";
    document.getElementById("ccnum").setCustomValidity("Please enter a valid credit card number.");
    return false;
}
}
function check(ccnum) {

    var sum     = 0,
        alt     = false,
        i       = ccnum.length-1,
        num;
    if (ccnum.length < 13 || ccnum.length > 19){
        return false;
    }
    while (i >= 0){
        num = parseInt(ccnum.charAt(i), 10);
        if (isNaN(num)){
            return false;
        }
        if (alt) {
            num *= 2;
            if (num > 9){
                num = (num % 10) + 1;
            }
        } 
        alt = !alt;
        sum += num;
        i--;
    }
    return (sum % 10 == 0);

