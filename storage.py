# Responsável por salvar e organizar os outputs gerados em arquivos JSON com timestamp.

import json
import os
from datetime import datetime

def save_execution(student_profile: dict,
                   topic: str,
                   content_type: str,
                   output: str) -> None:

    timestamp = datetime.now().isoformat()

    data = {
        "timestamp": timestamp,
        "student": {
            "id": student_profile["id"],
            "name": student_profile["name"]
        },
        "topic": topic,
        "content_type": content_type,
        "output": output
    }

    # Garante que a pasta outputs existe
    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/{timestamp.replace(':', '-')}.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"\nExecução salva em: {filename}")


CACHE_FILE = "outputs/cache.json"

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_cache(cache_data):
    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache_data, file, ensure_ascii=False, indent=4)


def generate_cache_key(student_name, topic, content_type):
    return f"{student_name}_{topic}_{content_type}".lower()


def get_cached_response(student_name, topic, content_type):
    cache = load_cache()
    key = generate_cache_key(student_name, topic, content_type)
    return cache.get(key)


def store_response_in_cache(student_name, topic, content_type, response):
    cache = load_cache()
    key = generate_cache_key(student_name, topic, content_type)
    cache[key] = response
    save_cache(cache)


HISTORY_FILE = "outputs/history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_history(history_data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history_data, file, ensure_ascii=False, indent=4)


def add_to_history(student_name, topic, content_type, source, output):
    history = load_history()

    record = {
        "timestamp": datetime.now().isoformat(),
        "student": student_name,
        "topic": topic,
        "content_type": content_type,
        "source": source,  # "api" ou "cache"
        "output": output
    }

    history.append(record)
    save_history(history)


def get_full_history():
    return load_history()


def get_history_by_student(student_name: str):
    history = load_history()
    return [
        record for record in history
        if record["student"].lower() == student_name.lower()
    ]


def get_history_by_topic(topic: str):
    history = load_history()
    return [
        record for record in history
        if record["topic"].lower() == topic.lower()
    ]