from django.conf import settings

from produtos.models import Produto


class Carrinho(object):
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)   #CART_SESSION_ID

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}  #empty dictionary

        self.cart = cart

    #acess the PRODUCT from the database.
    def __iter__(self):
        for prod in self.cart.keys():
            self.cart[str(prod)['produto']] = Produto.objects.get(pk=prod)

    #check the length of tip of the cart (how many items we have in the card).
    def __len__(self):
        return sum(item['quantidade'] for item in self.cart.values())

    #every time we do a modification to the card we want to notify the browser or the server that something happened with the session.
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified =True #session has been updated for the user

    # add a product in the cart
    def add (self, produto_id, quantidade=1, update_quantidade=True): #update_quantidade -> TRUE because i can add the same product whatever i want.
        produto_id = str(produto_id)

        #not in the cart yet
        if produto_id not in self.cart:
            self.cart[produto_id] = {'quantidade':0, 'id': produto_id}

        #we want increment or decrement the number of quantities in the cart
        if update_quantidade:
            self.cart[produto_id]['quantidade'] += int(quantidade)

            #check if the quantity is zero that we want to remove from the cart
            if self.cart[produto_id]['quantidade'] == 0:
                self.remove(produto_id)

        #update the session
        self.save()

    def remove(self, produto_id):
        if produto_id in self.cart:
            del self.cart[produto_id]
            self.save()


