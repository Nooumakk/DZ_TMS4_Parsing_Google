from parsing.obj_pars import Books, Films, Games


def main():
    python_courses = Books("https://play.google.com/store/books?hl=ru&gl=US")
    python_courses.get_data()
    python_courses.parse()
    python_courses.save("books.json")

    python_courses = Films("https://play.google.com/store/movies?hl=ru&gl=US")
    python_courses.get_data()
    python_courses.parse()
    python_courses.save("films.json")
    
    python_courses = Games("https://play.google.com/store/games?hl=ru&gl=US")
    python_courses.get_data()
    python_courses.parse()
    python_courses.save("games.json")


if __name__ == "__main__":
    main()