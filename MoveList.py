movies = ["Terminator", "Harry Potter: 1", "Kpop Demon Hunters"]
for movie in movies:
    print(movie)

title =input("Please enter a movie title:")

if title in movies:
    print(f"Yes, {title} is one of your favorite movies!")

else:
    print(f"No, {title} is not on the list.")