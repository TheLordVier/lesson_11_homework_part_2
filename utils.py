# Импортируем стандартный модуль json
import json


def load_candidates_from_json() -> list[dict]:
    """
    Создаём функцию чтения json файла
    """
    with open("candidates.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all_candidates() -> list[dict]:
    """
    Создаём функцию, которая покажет всех кандидатов
    """
    return load_candidates_from_json()


def get_by_id(uid: int) -> dict | None:
    """
     Создаём функцию получения кандидата по его id
     """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if uid == candidate["id"]:
            return candidate
    return None


def get_candidates_by_name(name: str) -> list[dict]:
    """
     Создаём функцию, которая вернёт кандидата по имени
     """
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill: str) -> list[dict]:
    """
     Создаём функцию, которая вернёт кандидатов по навыку
     """
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
