import random as rnd
name = "Deniz"
surname = "Yazıcıoğlu"

#Entrance
for lives in range(3):

    user_name = input("enter your name: ")
    user_surname = input("enter your surname: ")

    if name == user_name and surname == user_surname:
        print("Welcome!")
        break

    elif name != user_name and surname == user_surname:
        print("your name is wrong")
        lives -= 1

    elif name == user_name and surname != user_surname:
        print("your surname is wrong.")

    else:
        print("your name and surname are wrong.")
print("please try again later.")


def course():

    print("you should take course min. 3 or max. 5")

    while True:

        x = int(input("Please enter your how many course minimum you want: "))
        y = int(input("Please enter your how many course maximum you want: "))
        if 3 <= x <= 5 and 3 <= y <= 5:
            print("congrats")
        else:
            print("You failed in class.")
            break



        course1 = input("Enter your course name: ")
        course2 = input("Enter your course name: ")
        course3 = input("Enter your course name: ")
        course4 = input("Enter your course name: ")
        course5 = input("Enter your course name: ")

        MyList = [course1, course2, course3, course4, course5]
        print("your chose courses", MyList)
        print("The system choose one of these courses for your exam instead of you.")
        z = rnd.choice(MyList)
        print(z)

        mt = int(input("enter your midterm grade: "))
        f = int(input("enter your final grade: "))
        pr = int(input("enter your project grade: "))
        dict1 = {"midterm": mt, "final": f, "project": pr}
        print(dict1)

        mt_note = mt * 0.3
        f_note = f * 0.5
        pr_note = pr * 0.2
        grade = mt_note + f_note + pr_note
        print("your grade is,", grade)

        if grade >= 90:
            print("you took AA")
            break
        elif 70 <= grade < 90:
            print("you took BB")
            break
        elif 50 <= grade < 70:
            print("you took CC")
            break
        elif 30 <= grade < 50:
            print("you took DD")
            break
        else:
            print("You took FF, so you FAİLED in class")

course()