# Manage My Web - ManageMyWeb.org

Bug:

Product Limit - on testing although a product may have a limit of 10, a user could add more by adding one at a time 8 to 9 to 10 to 11 etc. I added a limit in the update cart
which looks at how much of a product is in a users cart, add the new requested quantity and then if this number is higher than product availability, the product quanitity is 
set to the limit, else the quantity is as requested by the user.