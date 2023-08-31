#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import  *

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    '''

    # session.query(Customer).delete()
    # # make user you correctly name the attr you are initializing the object with 
    # hubert = Customer(name ='kiniop')
    # zack = Customer(name='zack')
    # charlez = Customer(name='charlez')
    # hether = Customer(name='hether')
    
    # session.add_all([hubert, zack,charlez,hether])
    # session.commit()
    # res = (session.query(Customer).all())
    # #print the orders that belongs to a customer
    # print(charlez.orders)
    # # if a customer has more than on order, python gives an array of the oder objet
    # # we can access then using the index
    # print('for zack:-> ',zack.orders[0].title)
    # print('for zack:-> ',zack.orders[1].title)

    # # for i in res:
    # #     print(f"{i.id} {i.name}")



# ----------- populate the order table
    session.query(Order).delete()
    # make user you correctly name the attr you are initializing the object with 
    order1 = Order(title='shwarma', customer=zack)
    order2 = Order(title='milk shake', customer=charlez)
    order3 = Order(title='oil', customer=hether)
    order4 = Order(title='nyamachoma', customer=zack)

    session.add_all([order1,order2,order3,order4])
    session.commit()
    # ----------- get the rcords from the order table
    orders = session.query(Order).filter(Order.id == 2)
    # we can reverse access the customer, from the order, making use of the 
    #backref variable provided = customer
    print(order1.customer.id,order1.customer.name)
   
    # for order in orders:
    #     print(order.id, order.customer.name)'''


    session.query(Game).delete()

    fake = Faker()

    genres = ['action', 'adventure', 'strategy',
        'puzzle', 'first-person shooter', 'racing']
    platforms = ['nintendo 64', 'gamecube', 'wii', 'wii u', 'switch',
        'playstation', 'playstation 2', 'playstation 3', 'playstation 4',
        'playstation 5', 'xbox', 'xbox 360', 'xbox one', 'pc']
  

    games = []
    for i in range(50):
        game = Game(
            title=fake.unique.name(),
            genre=random.choice(genres),
            platform=random.choice(platforms),
            price=random.randint(5, 60)
        )

        # add and commit individually to get IDs back
        session.add(game)
        session.commit()

        games.append(game)
        # session.add_all(games)
        # session.commit()
        # print(game)

    session.query(Review).delete()
    reviews_list = []
    for game in games:
        for i in range(random.randint(1,5)):
            review = Review(
                score=random.randint(0, 10),
                comment=fake.sentence(),
                game_id=game.id
            )

            reviews_list.append(review)
    
    session.bulk_save_objects(reviews_list)
    session.commit()
    session.close()

    '''----------------if we manually wanna delete the reviews data
      all_review = session.query(Review)
    for rev in all_review:
        session.delete(rev)
    session.commit()

    '''
 
    # reviews = session.query(Review).filter(Review.score <1).first()
    # for rev in reviews:
    #     print(rev.game.title)
    
    # print(reviews.game) # should give you the game this rev belongs to 

    # ------------------------------------
# #     #lets access the game and the one to many relshp it has with reviews
    g = session.query(Game).first()
    print(g)
    print('-----------------')

    game1_reviews = ([  rev for rev in session.query(Review).filter_by(game_id = g.id)])
    print((game1_reviews))
    print('-----------------')
 # lets see how many    reviews this game has
    # print(g.reviews)

    # lets access the game with ID 2 and delete it 
    # and then we see if all the review associated with it are gone as well
    # game_with_id_2 = session.query(Game).filter(Game.id == 2)
    # id =0
    
    # for i in game_with_id_2:
    #     id = i.id
    #     game = i
    # print(id)
    # session.delete(game)
    # # lets get all the reviews for the game_with_id_2
    # game_with_id_2_reviews= session.query(Review).filter_by(game_id = id).all()
    # print(game_with_id_2_reviews)
 


   