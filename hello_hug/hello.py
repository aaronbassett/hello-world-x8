import hug


@hug.get("/ncco", versions=1)
def ncco():
    return [{"action": "talk", "text": "Hello World from Hug"}]


@hug.get("/ncco", examples="who=World", versions=range(2, 5))
def ncco(who: hug.types.text):
    return [{"action": "talk", "text": f"Hello {who} from Hug"}]
