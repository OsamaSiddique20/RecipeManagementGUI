from extensions import db
from http import HTTPStatus
class Recipe(db.Model):
    __tablename__ = 'recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(1000))  
    instructions = db.Column(db.String(1000))
    category = db.Column(db.String(1000))
    rating = db.Column(db.String(1000))

    @property
    def data(self):
        return {
            'recipe_id': self.recipe_id,
            'name': self.name,
            'ingredients': self.ingredients, 
            'instructions': self.instructions,
            'category': self.category,
            'rating': self.rating
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        result = cls.query.all()
        return [recipe.data for recipe in result]
    
    @classmethod
    def get_by_id(cls,id):
        result = cls.query.filter(cls.recipe_id == id).first()
        return result.data if result else None