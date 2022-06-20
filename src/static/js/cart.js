

var updateBtns = document.getElementsByClassName('update-btn')


for (var i = 0 ; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
    var productid = this.dataset.product
    var action = this.dataset.action
    console.log('product:' + productid, "action:" + action)
    console.log('user: ' + user)
    if (user === 'AnonymousUser'){
        updateUserOrder(product, action)
    }
    });
}


function updateUserOrder(product, action){
    var url = '/update_item/'


    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'applications/json'
        },
        body:json.stringify({'productId': productId, 'action': actions})
    
    })
    .thin((response) => {
        return response.json()
    })

    .thin((data) => {
        console.log('data:', data)
    })
}