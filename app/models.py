from sqlalchemy import Column, Integer, String , Float, ForeignKey, Enum, Boolean
from app import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    image=Column(String(255), default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dperson%2Bicon&psig=AOvVaw2Sy_coSUaFSSXd2dWwRtEN&ust=1699974243255000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPDl_tifwYIDFQAAAAAdAAAAABAE')
    def __str__(self):
        return self.name



class Category(db.Model):
    __tablename__= 'catelogy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable= False, unique=True)
    products = relationship('Product', backref='category', lazy=True)
    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default= 0)
    image = Column(String (300))
    category_id= Column(Integer, ForeignKey(Category.id),nullable=False)

if __name__ == "__main__":
    from app import app
    with app.app_context():
        db.create_all()
        import hashlib

        u = User(name='Admin', username='admin',
                 password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),user_role = UserRoleEnum.ADMIN)

        db.session.add(u)
        db.session.commit()

        c1 = Category(name="Mobile")
        c2 = Category(name="Tablet")
        db.session.add(c1)
        db.session.add(c2)
        p1 = Product(name='Iphone 15 Pro max', price=20000, category_id='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:358:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/iphone-15-pro-max_3.png')
        p2 = Product(name='Iphone 13 Pro Max', price=30000, category_id='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/3/_/3_51_1_2_2_1_1_2.jpg')
        p3 = Product(name='Galaxy S23 Ultra', price=25000, category_id='2',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/s/2/s23-ultra-xanh-1.png')
        p4 = Product(name='iPad Pro 2018', price=100000, category_id='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/i/p/ipad-pro-13-select-202210.png')
        p5 = Product(name='Xiaomi Black Shark 4s', price=255000, category_id='1',
                      image='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/x/i/xiaomi-black-shark-5.png')

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
