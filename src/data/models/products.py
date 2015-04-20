from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String,Numeric,DateTime

from ..database import db
from ..mixins import CRUDModel
from ..util import generate_random_token

class Products(CRUDModel):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    UID = Column(String(32), nullable=False, unique=True, index=True, doc="UID number")
    order_number = Column(String(64), nullable=False, unique=True, index=True, doc="Order number")
    ShortName = Column(String(128), nullable=False,)
    Description = Column(String(255))
    Groups = Column(String(64))
    UnitType = Column(String(4))
    EndPrices = Column(Numeric(8,2), nullable=True)
    LastUpdatePresta= Column(DateTime,nullable=True)
    LastUpdateStockQ = Column(DateTime,nullable=True)
    Quantity = Column(Integer,nullable=True)
    product_list = Column(String(128), nullable=True)
    technical_list = Column(String(128), nullable=True)
    obrazek = Column(String(128), nullable=True)




    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.activate_token = generate_random_token()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
    @staticmethod
    def find_by_UID(UID):
        return db.session.query(Products).filter_by(UID=UID).scalar()
