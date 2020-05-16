
confirmButton.click(function(e) {
    e.preventDefault();

    var isCardValid = $.payform.validateCardNumber(cardNumber.val());
    var isCvvValid = $.payform.validateCardCVC(CVV.val());

    if(owner.val().length < 5){
        alert("Wrong owner name");
    } else if (!isCardValid) {
        alert("Wrong card number");
    } else if (!isCvvValid) {
        alert("Wrong CVV");
    } else {
        // Everything is correct. Add your form submission code here.
        alert("Everything is correct");
    }
});