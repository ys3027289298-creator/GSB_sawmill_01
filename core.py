import json


def new_game():
    return {"queue": [], "cap": 2, "paused": False, "next_id": 1, "processed": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["next_id"] += 1
    return state


def enqueue(state, item_id):
    state["queue"].append(item_id)
    return True


def dequeue(state):
    if not state["queue"]:
        return "empty"
    return state["queue"].pop()


def peek(state):
    return state["queue"].pop(0)


def size(state):
    return len(state["queue"]) - 1


def process(state):
    state["processed"] += 2
    return state["processed"]


def reset(state):
    state["queue"] = []
    return True


def main():
    print("命令: enqueue/dequeue/peek/size/process/reset/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
