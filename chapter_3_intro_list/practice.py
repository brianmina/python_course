names = [ "Eric", "pablo", "brian", "daniel", "luis"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"thank you {names[0]}!")
print(f"thank you {names[1]}!")
print(f"thank you {names[2]}!")
print(f"thank you {names[3]}!")
print(f"thank you {names[4]}!")


transportation = ["rollerbalding", "car", "bike"]
print(f"I would like to go to work today by {transportation[0]}!")
print(f"{transportation[1].title()} is the fastest way to get there!")
print(f"{transportation[2].title()} is fun!")


guest_list = [ "eric", "pablo", "brian"]
print(f"Hey {guest_list[0].title()}, I would like to invite you to dinner tonight!")
print(f"Hey {guest_list[1].title()}, I would like to invite you to dinner tonight!")
print(f"Hey {guest_list[2].title()}, I would like to invite you to dinner tonight!")

print(f"{guest_list[0].title()} can't make it!")
guest_list[0] = "Susan"
print(f"Hey {guest_list[0].title()}, I would like to invite you to dinner tonight!")
print(f"Hey {guest_list[1].title()}, still come over?")
print(f"Hey {guest_list[2].title()}, still come over?")

print("Guys!, I found a bigger table!, I'm going to invite more guest.")
guest_list.insert(0,"martha")
guest_list.insert(2,"carlos")
guest_list.append("armand")
print(f"{guest_list[0].title()}, you are invited!")
print(f"{guest_list[1].title()}, you are invited!")
print(f"{guest_list[2].title()}, you are invited!")
print(f"{guest_list[3].title()}, you are invited!")
print(f"{guest_list[4].title()}, you are invited!")
print(f"{guest_list[5].title()}, you are invited!")

print("Ops!, actually I can invite only two people.")

popped_guest1 = guest_list.pop()
print(f"{popped_guest1.title()}, you are not going!")

popped_guest2 = guest_list.pop()
print(f"{popped_guest2.title()}, you are not going!")

popped_guest3 = guest_list.pop()
print(f"{popped_guest3.title()}, you are not going!")

popped_guest4 = guest_list.pop()
print(f"{popped_guest4.title()}"


