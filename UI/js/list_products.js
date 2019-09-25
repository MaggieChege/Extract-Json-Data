function setToken(result){
   return localStorage.setItem('access_token', result.body.access_token)
}





window.onload = function Products(){
 let products_url = 'http://127.0.0.1:5000/api/';


  fetch(products_url,{
    method:"GET",
    Headers: {
     'Accept':'application/json',
     'Content-type':'application/json',
    },
    })

  .then(respose => respose.json())
  .then((data) =>{
   console.log(data.data);
   let products = data.data;
   console.log(products)
   let product_table  = document.getElementById('customers');
   header = `
   <tr class="header">
   <th>id</th>
    <th>calltype</th>
        <th>clientname</th>
        <th>contacttype</th>
        <th>datecreated</th>
        <th>disposition_id</th>
        <th>mobileno</th>
        <th>questionsubtype</th>
        <th>questiontype</th>
        <th>sourcename</th>
        <th>store_id</th>

      </tr>`
    product_table.innerHTML=header

    products.forEach(function(product){
      let item=JSON.stringify(product)
      item="  "+ item +"  "
    

      product_table.innerHTML += '<tr>'+
      '<td>'+product.id +'</td>'+
      '<td>'+product.calltype +'</td>'+
      '<td>'+product.clientname+'</td>'+
      '<td>'+product.contacttype+ '</td>'+
      '<td>'+product.datecreated + '</td>'+
      '<td>'+product.disposition_id+ '</td>'+
      '<td>'+product.mobileno + '</td>'+
      '<td>'+product.questionsubtype+ '</td>'+
      '<td>'+product.questiontype + '</td>'+
      '<td>'+product.sourcename+ '</td>'+
      '<td>'+product.store_id + '</td>'+

      '</tr>';

    });
  })
}

