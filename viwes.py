from flask import Blueprint, jsonify
from utils import *
# Создаем блупринт
movie_blueprint = Blueprint('movie_blueprint', __name__)


# Создаем вьюшку для маршрута /movie/<title> , которая бы выводила данные про фильм
@movie_blueprint.route('/movie/<title>')
def movie_by_title(title):
    return title_info(title)

# Создаем вьюшку для маршрута /movie/year/to/year, которая бы выводила список словарей.
@movie_blueprint.route('/movie/<year1>/to/<year2>')
def range_by_year(year1, year2):
    return jsonify(year_to_year(year1, year2))


# Создаем вьюшку для маршрута /rating/children,family, adult, которая бы выводила список словарей.
@movie_blueprint.route('/rating/<rating>')
def get_by_rating(rating):
    return jsonify(movie_by_rating(rating))


# Создаем вьюшку  /genre/<genre> которая возвращала бы список
@movie_blueprint.route('/genre/<genre>')
def get_by_genre(genre):
    return jsonify(movie_by_genre(genre))