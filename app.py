# Импортируем фреймворк Flask
from flask import Flask, render_template
# Импортируем функции из utils.py, которые будем использовать
from utils import *

# Инициализируем приложение
app = Flask(__name__)


@app.route("/")
def page_main():
    """Главная страница"""
    candidates = get_all_candidates()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    """Вывод кандидата по его id"""
    candidate: dict = get_by_id(uid)
    if not candidate:
        return "Нет такого кандидата"
    return render_template("single.html", candidate=candidate)


@app.route("/skill/<skill>")
def page_skills(skill):
    """Вывод кандидатов, в списке навыков у которых содержится определенный skill (навык)"""
    candidates: list[dict] = get_candidates_by_skill(skill)
    candidates_count = len(candidates)
    return render_template("skill.html",
                           candidates=candidates,
                           skill=skill,
                           candidates_count=candidates_count
                           )


@app.route("/search/<candidate_name>")
def page_name(candidate_name):
    """Вывод кандидата, по его имени"""
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template("search.html",
                           candidates=candidates,
                           candidate_name=candidate_name,
                           candidates_count=candidates_count
                           )


if __name__ == '__main__':
    app.run(debug=True)
