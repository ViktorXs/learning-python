# Queue party
class IsThisAnanas:
    import queue
    entries = queue.Queue()

    entries.put("Was")
    entries.put("ist")
    entries.put("das")
    entries.put("für")
    entries.put("eine")
    entries.put("Ananas?")

    while not entries.empty():
        el = entries.get()
        print(el)
    print("Eine Gute!")


IsThisAnanas()
