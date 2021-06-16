# Queue party
class TheDongALongEmptier:
    import queue
    entries = queue.Queue()

    entries.put("ding")
    entries.put("dong")
    entries.put("wong")
    entries.put("schlong")
    entries.put("dabong")

    while not entries.empty():
        el = entries.get()
        print(el)
    print("Done")


TheDongALongEmptier()
