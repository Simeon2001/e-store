#   ECOMMERCE
 an ecommerce API

 ## TUTORIALS

* TO CREATE AN ACCOUNT USE https://store-wa.herokuapp.com/api/register then with a post request containing the json data:
--------------------

    {"username":"hartech","password":"Linktree2021","email":"hartech@gmail.com"}
-------------------------------------

after registering it automatically create an authtoken.

* TO LOGIN TO ACCOUNT USE https://store-wa.herokuapp.com/api/token then with a post request containing the json data:
--------------------

    {"username":"jesse","password":"Apple29999"}
-------------------------------------

* which generate this result:

--------------------

    {"status":true,"token":"121fe8dbc25140d8fa896a6367221acf55616891"}
-------------------------------------

* TO GET ALL PRODUCT IN STORE USE https://store-wa.herokuapp.com/api/product then with a get request and result is json data:
--------------------

    [{"id":1,"category":"shoe","name":"nike air","price":"5000","available":true,"image":"https://img.net"},{"id":2,"category":"pant","name":"blue jean","price":"7000","available":true,"image":"https://img.net"}]
-------------------------------------

* TO GET product in cart for EACH USER USE https://store-wa.herokuapp.com/api/cart then with a GET request and user TOKEN with a result of this:
which contain 

--------------------

   
    {
        "id": 1,
        "mea": "nike air",
        "order": 1,
        "quantity": 1,
        "get_total": 5000
    },
    {
        "id": 2,
        "mea": "blue jean",
        "order": 1,
        "quantity": 1,
        "get_total": 7000
    }

-------------------------------------




* TO add a product to cart or increase it quantity for a certain user USE https://store-wa.herokuapp.com/api/update then with a POST request, then with the product id e.g 1,2,3 and "Y" to increase the quantity and "N" to reduce:
--------------------
    {"id":"2","bool":"N"}
-------------------------------------

this will add product with id 1 to the cart and increase it quantity from 0 to 1.
if this post request is resend with id 1 and y it will increase the quantity from 1-2.

will return 

-----------------------
{
    "message": "add"
}

'if it to reduce the quantity':

{
    "message": "minus"
}

------------------------------------------