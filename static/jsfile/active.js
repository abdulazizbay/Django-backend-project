function order_by (sort){
    console.log(sort)
    url=`/product_by/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'sort':sort
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            console.log(data.products,data.products.length)
            var products = data.products
            html = ``
            for(let i=0;i<products.length;i++){
                html += `
                    <div style="width: 296px; margin-right: 20px" class="product product-2">
                        <figure class="product-media">
    
                                <span class="product-label label-new">Sale</span>

                            <a href="{% url 'product_info' ${products[i].id} %}">
                                <img src="${products[i].image}" alt="Product image" class="product-image">
                            </a>
    
                            <div class="product-action-vertical">
                                <a href="#" class="btn-product-icon btn-wishlist btn-expandable"><span>Add to wishlist</span></a>
                            </div><!-- End .product-action -->
    
                            <div class="product-action product-action-dark">
                                <a href="#" class="btn-product btn-cart" title="Add to cart"><span>Add to cart</span></a>
                                <a href="popup/quickView.html" class="btn-product btn-quickview" title="Quick view"><span>Quick view</span></a>
                            </div><!-- End .product-action -->
                        </figure><!-- End .product-media -->
    
                        <div class="product-body">
                            <div class="product-cat">
                                <a href="{% url 'product_info' product.id %}">${products[i].category}</a>
                            </div><!-- End .product-cat -->
                            <h3 class="product-title"><a href="{% url 'product_info' product.id %}">${products[i].name}</a></h3><!-- End .product-title -->
                            <div class="product-price">
                                $ <strike style="margin-right: 5px">${products[i].price}</strike>
                                
                                    <p style="color: red; font-weight: bold">${products[i].discount}</p>

                            </div><!-- End .product-price -->
                            <div class="ratings-container">
                                <div class="ratings">
                                    <div class="ratings-val" style="width: 60%;"></div>
                                </div>
                                <span class="ratings-text">( ${products[i].reyting} Reviews )</span>
                            </div>
                        </div>
                    </div>
                    
            `
            document.getElementById('reyting').innerHTML = html
            }
        })
    })
}

// function add_cart (id){
//     url=`/add_to_cart/`
//     fetch(url,{
//         method:'POST',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken,
//         },
//         body:JSON.stringify({
//             'id':id
//         })
//         })
//         .then((response)=>{
//         response.json().then((data) => {
//             console.log("Data keldi",data['count'])
//             var products = data.products
//             html = ``
//             for(let i=0;i<products.length;i++) {
//                     html += `
//                         <div class="product">
//                             <div class="product-cart-details">
//                                 <h4 class="product-title">
//                                     <a href="/product_info/${ products[i].id }">${ products[i].name }</a>
//                                 </h4>
//
//                                 <span class="cart-product-info">
//                                     <span class="cart-product-qty">111</span>
//                                     x $ ${ products[i].price }
//                                     </span>
//                             </div><!-- End .product-cart-details -->
//
//                             <figure class="product-image-container">
//                                 <a href="{% url 'product_info' p.id %}" class="product-image">
//                                     <img src="${ products[i].image }" alt="product">
//                                 /a>
//                             </figure>
//                             <a href="#" class="btn-remove" title="Remove Product"><i class="icon-close"></i></a>
//                         </div>`
//             }
//
//
//             document.getElementById('countid').innerHTML=data['count']
//             document.getElementById('dropdown-products').innerHTML= html
//         })
//
//     })
// }

function add_wishlist(id){
    url=`/add_wishlist/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })

        .then((response)=>{
        response.json().then((data) => {
            console.log('ok')
        })
    })
}

function delete_wishlist (id){
    url=`/delete_wishlist/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
        })
        document.getElementById('product'+id).style.display = 'none'
    })
}