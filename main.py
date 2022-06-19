import books, students, time, datetime

while True:
    date = datetime.datetime.now() + datetime.timedelta(days=14)
    date = date.strftime('%Y-%m-%d')
    try:
        time.sleep(2)
        is_valid_student = is_valid_book = False
        choice = input("\033[1;37;1m\n=====================================\nEnter 1 to borrow book\nEnter 2 to return book\nEnter 3 to check availability of book\nEnter 4 to check student's record\n=====================================\n")
        if choice == "eeeeeeee":
            print("\033[1;31;1mTerminating Program...")
            time.sleep(1)
            break
        else:
            choice = int(choice)
        if choice == 1 or choice == 2:
            if choice == 1:
                card = input("\033[1;36;1mTap your student card: ")
                Students = students.students
                for x in range(len(Students)):
                    if card == Students[x]["no"]:
                        position = x
                        is_valid_student = True
                        print("\033[1;33;1mWelcome to the library,", Students[x]["name"])
                        break
                if not is_valid_student:
                    print("\033[1;31;1mInvalid student. Please contact our committee members if you need help.")
                    continue

            while True:
                time.sleep(1)
                barcode = input("\033[1;35;1mScan the barcode of the book (press ENTER to return to main menu): \033[1;37;1m")
            
                if barcode == "":
                    print("\033[1;37;1mThank you for using our service. Have a great day ahead!")
                    break

                Books = books.books
                for book in Books:
                    if barcode == book["no"]:
                        is_valid_book = True
                        if choice == 1:
                            if book["available"]:
                                book["available"] = False
                                book["borrowedBy"] = card
                                book["returnDate"] = date
                                print("\033[1;32;1mYou successfully borrowed", book["name"], "(Return Date:", date, ")")
                            else:
                                print(f"\033[1;31;1m{book['name']} is currently being borrowed. Please return it first.")
                        elif choice == 2:
                            if not book["available"]:
                                book["available"] = True
                                book["borrowedBy"] = None
                                returnDate = book["returnDate"]
                                # x = datetime.datetime.strptime(returnDate, '%Y-%m-%d')
                                # y = datetime.datetime.strptime(date, '%Y-%m-%d')
                                book["returnDate"] = None
                                # if x > y: # Student returns book early (Originally return date is later than today's date)
                                print("\033[1;32;1mYou successfully returned", book["name"])
                                # else:
                                # print("\033[1;32;1mYou successfully returned", book["name"], "(Late for", (str(y-x)).split(",")[0], ")")
                            else:
                                print(f"\033[1;31;1m{book['name']} is already returned.")
                        file = open("books.py", "w")
                        file.write(f"books = {Books}")
                        file.close()
                if not is_valid_book:
                    print("\033[1;31;1mInvalid book. Please try again. Contact our committee members if you need help.")
                    
                is_valid_book = False

        elif choice == 3:
            barcode = input("\033[1;35;1mScan the barcode of the book: ")
            Books = books.books
            for book in Books:
                if barcode == book["no"]:
                    is_valid_book = True
                    if book["available"]:
                        print(f"\033[1;32;1m{book['name']} is currently available for borrowing")
                    else:
                        card = book["borrowedBy"]
                        returnDate = book["returnDate"]
                        for x in range(len(students.students)):
                            if card == students.students[x]["no"]:
                                position = x
                                break
                        print(f"\033[1;31;1m{book['name']} is currently being borrowed by", students.students[position]["name"], "and is scheduled to be returned on", returnDate)
                        
            if not is_valid_book:
                print("\033[1;31;1mInvalid book")

        elif choice == 4:
            card = input("\033[1;36;1mTap your student card: ")
            Students = students.students
            for x in range(len(Students)):
                if card == Students[x]["no"]:
                    position = x
                    is_valid_student = True
                    break
            if not is_valid_student:
                print("\033[1;31;1mInvalid student. Please contact our committee members if you need help.")
                continue
            listOfBooks = []
            Books = books.books
            for book in Books:
                if book["borrowedBy"] == card:
                    listOfBooks.append(book)
            if len(listOfBooks) != 0:
                print("\033[1;32;1m----------------------------------------------")
                print("➤ Borrow record of", students.students[position]["name"], f"[{len(listOfBooks)}]")
                for book in listOfBooks:
                    print("\033[1;32;1m----------------------------------------------")
                    print("\033[94mName:", book["name"])
                    print("Author:", book["author"])
                    print("Publisher:", book["publisher"])
                    print("ISBN:", book["isbn"])
                    print("Return Date:", book["returnDate"])
                print("\033[1;32;1m----------------------------------------------")
            else:
                print(f"\033[94m{students.students[position]['name']} does not have any existing record.")
        else:
            print("\033[1;31;1mInvalid action. Please try again.")
    except Exception:
        print("\033[1;31;1mInvalid action. Please try again.")