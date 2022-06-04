

var updateBtns = document.getElementsByClassName('update-btn')


for (var i = 0 ; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
    var productid = this.dataset.product
    var action = this.dataset.action
    console.log('product:' + productid, "action:" + action)
    });
}