from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# example

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    orders = relationship('Order', backref='customer')
  

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    customer_id = Column(Integer(), ForeignKey('customers.id'))



#----------------------------------------------------------------------
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    reviews = relationship('Review', backref=backref('game'), cascade='all, delete-orphan')
    
    
    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'
 

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))


    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'