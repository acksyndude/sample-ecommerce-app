// // converting to json
jsonDataProducts = JSON.parse(dataFromProductsInfor)

getIfThereIsAnyProductorNot = jsonDataProducts[Object.keys(jsonDataProducts)[0]]

if_there_any_product = ''

function createProducts() {
    if_there_any_product = jsonDataProducts[Object.keys(jsonDataProducts)[1]]
    console.log(if_there_any_product);

    for (i in if_there_any_product){
   
        let product_series_to_start = if_there_any_product[i]

        productID = product_series_to_start[0];
        productName = product_series_to_start[1];
        productDescritpion = product_series_to_start[2];
        productPrice = product_series_to_start[3];
        productImagePath = product_series_to_start[4];
        creatingElements(productID, productName, productDescritpion, productPrice, productImagePath);
    }
}

function creatingElements(productID, productName, productDescritpion, productPrice, productImagePath) {
    let mainProductDivIs = document.getElementById('mainProductDivRow');
    let secondMainDivElementForProdcuts = document.createElement('div');
    secondMainDivElementForProdcuts.classList.add("col-md-4");
    mainProductDivIs.appendChild(secondMainDivElementForProdcuts);
    
    let thirdMainEle = document.createElement('div');
    thirdMainEle.classList.add('card');
    thirdMainEle.classList.add('mb-4');
    thirdMainEle.classList.add('box-shadow');
    secondMainDivElementForProdcuts.appendChild(thirdMainEle);

    // //image attribute
    let img_child_of_third = document.createElement('img');
    img_child_of_third.classList.add('card-img-top');
    img_child_of_third.setAttribute('data-src', 'holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=E-Commerce Product');
    img_child_of_third.setAttribute('alt', 'E-Commerce Product');
    img_child_of_third.setAttribute('data-holder-rendered', 'true');
    img_child_of_third.setAttribute('style', 'height: 225px; width: 100%; display: block;');
    img_child_of_third.setAttribute('src', productImagePath);
    thirdMainEle.appendChild(img_child_of_third);
    
    let card_body_div_child = document.createElement('div');
    card_body_div_child.classList.add('card-body');
    let paragraph_body_of_card = document.createElement('p')
    paragraph_body_of_card.classList.add('card-header')
    // //Product Name Here Please
    paragraph_body_of_card.innerHTML = productName;
    card_body_div_child.appendChild(paragraph_body_of_card)
    let paragraph_description_of_card = document.createElement('p');
    paragraph_description_of_card.classList.add('card-text')
    // //Product Description Here Please
    // paragraph_description_of_card.innerHTML = "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.";    
    paragraph_description_of_card.innerHTML = productDescritpion;    
    card_body_div_child.appendChild(paragraph_description_of_card)
    thirdMainEle.appendChild(card_body_div_child);

    let btn_div_child_content = document.createElement('div');
    btn_div_child_content.classList.add('d-flex');
    btn_div_child_content.classList.add('justify-content-between');
    btn_div_child_content.classList.add('align-items-center');
    //// creating child of btn-group which is under in this element
    let btn_group_btn_class = document.createElement('div');
    btn_group_btn_class.setAttribute("class", 'btn-group');
    btn_div_child_content.appendChild(btn_group_btn_class);
    ////creating elements of btn_group_btn_class in which there are two buttons
    let btn_button_grp_one = document.createElement('button');
    btn_button_grp_one.setAttribute('type', 'button');
    btn_button_grp_one.classList.add('btn');
    btn_button_grp_one.classList.add('btn-sm');
    btn_button_grp_one.classList.add('btn-outline-success');
    btn_button_grp_one.innerHTML = 'View';
    btn_group_btn_class.appendChild(btn_button_grp_one);
    let btn_button_grp_two = document.createElement('button');
    btn_button_grp_two.setAttribute('type', 'button');
    btn_button_grp_two.setAttribute('class', 'btn btn-sm btn-outline-primary');
    btn_button_grp_two.innerHTML = 'Buy Now';
    btn_group_btn_class.appendChild(btn_button_grp_two);
    let small_element = document.createElement('small');
    small_element.classList.add('text-muted');
    // //product price here
    small_element.innerHTML = '$'+productPrice;
    small_element.style.paddingRight = '5px';
    btn_div_child_content.appendChild(small_element);
    thirdMainEle.appendChild(btn_div_child_content);


}

if (getIfThereIsAnyProductorNot != 0) {
    createProducts();
}else{
    let mainProductDivIs = document.getElementById('mainProductDivRow');
    let secondMainDivElementForProdcuts = document.createElement('p');
    mainProductDivIs.appendChild(secondMainDivElementForProdcuts)
    secondMainDivElementForProdcuts.classList.add("alert");
    secondMainDivElementForProdcuts.classList.add("alert-danger");
    secondMainDivElementForProdcuts.innerHTML = 'No Products were Found';
}

