from billApp import db



class Customer(db.Model):
    cid = db.Column(db.String(), nullable = False,primary_key=True)
    cname = db.Column(db.String(length=30), nullable = False, unique=True)
    number = db.Column(db.Integer(), nullable = False)
    


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable = False, unique=True)
    price1 = db.Column(db.Float(), nullable=False)
    price2 = db.Column(db.Float(), nullable=False)
    price3 = db.Column(db.Float(), nullable=False)
    pcode = db.Column(db.String(length=4), nullable=False, unique=True)
    
    def __repr__(self):
        return f'Item {self.name}'
    
    def __str__(self):
        return f'{self.name}'
    
    
    

