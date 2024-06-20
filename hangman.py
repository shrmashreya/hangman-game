
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image , ImageTk

run = True

while(run == True):
        # Main Menu Interface
        root = tk.Tk()
        root.title("Main Menu")

        
        # show the game interface
        def switch_interface():
            root.withdraw()  # Hide the first interface
            score_board.withdraw() # hide the score interface
            game_interface.deiconify()  # Show the game interface

        # show the first interface
        def back_to_menu():
            game_interface.withdraw()  # Hide the game interface
            score_board.withdraw() # hide the score interface
            root.deiconify()  # Show the first interface


        # show the first interface
        def back_to_menu2():
            score_board.withdraw()
            game_interface.withdraw()
            root.deiconify()

          
        
        # show the game interface
        def back_to_game():
            global win_count
            score_board.withdraw()
            root.withdraw()
            game_interface.deiconify()
            run = True
            new_game()
            win_count = 0
            score_label.config(text=f"Score = {win_count} ") 

        # show the score interface
        def switch_interface2():
            global win_count
            game_interface.withdraw()
            root.withdraw()
            score_board.deiconify() 
            score2_label.config(text=win_count)      

        #background main menu
        jpg_image = Image.open("bb.jpeg")
        jpg_image = jpg_image.resize((1600, 900), Image.LANCZOS)  # Resize to fit the window
        background_image = ImageTk.PhotoImage(jpg_image)
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window
        root.attributes('-fullscreen', True)
        
        #button main menu
        start_button = tk.Button(root, text="Start Game",  bg="yellow", fg="black" ,command=switch_interface , width=25,height=2 )
        start_button.place(x=675 , y=400)

        exit_button = tk.Button(root, text="Exit",  bg="yellow", fg="black", command=root.quit , width=25,height=2)
        exit_button.place(x=675 , y=500)


        #list of words and question
        Trivia = [
            {"word":"python","question":"A popular programming language"},
            {"word":"computer","question": "An electronic device that performs various operations using data"},
            {"word":"keyboard","question":"An input device used for typing"},
            {"word":"guitar","question": "A musical instrument with strings"},
            {"word":"pizza","question":"A dish consisting of a flat round base of dough topped with ingredients"},
            {"word":"elephant","question":"A large mammal with a long trunk and big ears"},
            {"word":"sunflower","question":"A plant with large yellow flowers that follow the sun"},
            {"word":"beach","question": "A sandy or pebbly shore by the ocean"},
            {"word":"rainbow","question":"A meteorological phenomenon with a spectrum of light appearing in the sky"},
            {"word":"galaxy","question":"A massive system of stars, gas, and dust held together by gravity"},
            {"word":"nebula","question":"A cloud of gas and dust in space"},
            {"word":"constellation","question":"A group of stars that forms a recognizable pattern"},
            {"word":"apple","question": "it keeps doctors away"},
            {"word":"banana","question": "fruit which rich is in calcium"},
            {"word":"computer","question": "An electronic device"},
            {"word":"java","question": "A programming language"},
            {"word":"hangman","question": "A word guessing game"},
            {"word":"ocean","question": "A large body of water"},
            {"word":"mountain","question": "A tall natural land formation"},
            {"word":"giraffe","question": "A long-necked animal"},
            {"word":"umbrella","question": "Used to stay dry in the rain"},
            {"word":"moon","question": "Earth's natural satellite"},
            {"word":"butterfly","question": "An insect with colorful wings"},
            {"word":"chocolate","question": "A sweet treat made from cocoa"},
            {"word":"universe","question": "All of space, including stars and galaxies"},
            {"word":"mountain","question": "A tall natural land formation"},
            {"word":"kangaroo","question": "A marsupial known for its hopping"},
            {"word":"strawberry","question": "A red fruit often used in desserts"},
            {"word":"telescope","question": "An optical instrument for viewing distant objects"},
            {"word":"rainbow","question": "A colorful arc in the sky after rain"},
            {"word":"fireworks","question": "Explosive displays of light and color"},
            {"word":"chemistry","question": "The study of matter and its properties"},
            {"word":"biology","question": "The science of living organisms"},
            {"word":"astronomy","question": "The study of celestial objects like stars and planets"},
            {"word":"physics","question": "The study of matter, energy, and the fundamental forces of the universe"},
            {"word":"geology","question": "The science of the Earth's structure and history"},
            {"word":"ecosystem","question": "A community of living organisms and their environment"},
            {"word":"photosynthesis","question": "The process by which plants convert sunlight into energy"},
            {"word":"genetics","question": "The study of heredity and DNA"},
            {"word":"microscope","question": "An instrument used to magnify small objects"},
            {"word":"paleontology","question": "The study of ancient life through fossils"},
            {"word":"supernova","question": "A powerful explosion at the end of a star's life cycle"},
            {"word":"blackhole","question": "A region in space with intense gravitational pull that nothing can escape from"},
            {"word":"asteroid","question": "A small rocky body that orbits the Sun"},
            {"word":"comet","question": "A celestial object made of ice, gas, and dust that develops a tail as it approaches the Sun"},
            {"word":"satellite","question": "An object that orbits a planet or other celestial body"},
            {"word":"astronaut","question": "A person trained to travel and work in space"},
            {"word":"telescope","question": "An instrument used to observe distant objects in space"},
            {"word":"biology","question": "The study of living organisms and their interactions"},
            {"word":"chemistry","question": "The branch of science that deals with the composition, structure, and properties of matter"},
            {"word":"astronomy","question": "The study of celestial objects and phenomena beyond Earth's atmosphere"},
            {"word":"physics","question": "The study of matter, energy, and the fundamental forces of nature"},
            {"word":"evolution","question": "The process by which species change over time through natural selection"},
            {"word":"photosynthesis","question": "The process by which plants convert light energy into chemical energy"},
            {"word":"dinosaur","question": "Extinct reptiles that lived millions of years ago"},
            {"word":"hypothesis","question": "A testable explanation for a phenomenon"},
            {"word":"ecosystem","question": "A community of organisms and their physical environment"},
            {"word":"gravity","question": "The force that attracts two masses toward each other"},
            {"word":"blackhole","question": "A region of space where gravity is so strong that not even light can escape"},
            {"word":"oxygen","question": "Essential for respiration, this element is the most abundant in the Earth's atmosphere"}
        ]

        hangman_img = []
        for i in range(8):
            image = PhotoImage(file=f"Images/han{i}.png")
            hangman_img.append(image)

        def choose_word():
            word_info = random.choice(Trivia)
            word_arr = []
            word_arr.append(word_info["word"])
            word_arr.append(word_info["question"])
            return word_arr

        def update_hangman(mistakes):
            hangman_label.config(image = hangman_img[mistakes])

        #New game
        def new_game():
            global choosen,question,word,word_with_blanks,repeat,mistakes
            choosen = choose_word()
            question = choosen[1]
            word = choosen[0]
            word_with_blanks = "_"*len(word)
            repeat=[]
            mistakes = 0
            word_display.config(text=word_with_blanks)
            question_label.config(text=question)
            update_hangman(mistakes)


        # define a function to check if the letter is in word
        def check_guess(guess):
            global word_with_blanks
            global repeat
            global win_count
            global run
            global mistakes
            if guess in repeat:
                messagebox.showerror("Warning", "You can't repeat the entries")
                return

            repeat.append(guess)

            if guess in word:    
                word_with_blanks = ''.join([guess if word[i] == guess else word_with_blanks[i] for i in range(len(word))])
                word_display.config(text=word_with_blanks)

                if word_with_blanks == word:
                    win_count += 1
                    run = True
                    score_label.config(text=f"Score = {win_count}")
                    new_game()
            else:
                mistakes += 1
                if mistakes == 8:
                    messagebox.showerror("It's over", "Game Over\n" + "The Word was: '" + word + "'")
                    switch_interface2()
                else:
                    update_hangman(mistakes)

                

                    
        #game interface
        game_interface = tk.Toplevel()
        game_interface.title("The Hang Man")
        jpg1_image = Image.open("bb.jpeg")
        jpg1_image = jpg1_image.resize((1600, 900), Image.LANCZOS)  # Resize to fit the window
        background1_image = ImageTk.PhotoImage(jpg1_image)
        background1_label = tk.Label(game_interface, image=background1_image)
        background1_label.place(relwidth=1, relheight=1)  # Cover the entire window
        game_interface.attributes('-fullscreen', True)
        back_button = tk.Button(game_interface, text="Back to Menu", bg="yellow", fg="black", command=back_to_menu , width=25,height=2)
        back_button.place(x=500,y=700)
        exit_button = tk.Button(game_interface, text="Exit",  bg="yellow", fg="black", command=root.quit , width=25,height=2)
        exit_button.place(x=700 , y=700) 
        end_button = tk.Button(game_interface, text="End Game",  bg="yellow", fg="black", command=switch_interface2 , width=25,height=2)
        end_button.place(x=700 , y=800) 
        win_count = 0

        hangman_label = tk.Label(game_interface, bg="#79e3fd")
        hangman_label.place(x=200 , y=100)

        choosen = choose_word()
        question = choosen[1]
        word = choosen[0]
        word_with_blanks = "_"*len(word)
        #create dashes
        dash_frame = tk.Frame(game_interface)
        dash_frame.place(x=550 , y=500)  
        word_display = tk.Label(dash_frame,bg="#bae3e5", text=word_with_blanks, font=("Helvetica", 20) , padx=20)
        word_display.pack()
        #display questions on screen
        question_label = tk.Label(game_interface , text=question , font=("Helvetica", 18) , bg="#79e3fd")
        question_label.place(x=600 , y=200)

        repeat = []

        def get_entry_input():
            input_text = guess_entry.get()
            check_guess(input_text)
            guess_entry.delete(0, tk.END)

        def validate_entry_text(P):
            return len(P) <= 1
        validation = game_interface.register(validate_entry_text)

         

        #create guess entry and button
        guess_entry = tk.Entry(game_interface,validate="key", validatecommand=(validation, "%P"), width=6 , font=("Helvetica", 20),bg="#93d4d8")
        guess_entry.place(x=500 , y=600)
        guess_button = tk.Button(game_interface, text="Guess" , command=get_entry_input ,  width=25,height=2 , bg="yellow")
        guess_button.place(x=700 ,y=600)
        

        # Bind the Enter key to the guess entry action
        guess_entry.bind('<Return>', lambda event: get_entry_input())

        # Ensure the entry widget is focused when the application starts
        guess_entry.focus_set()

        mistakes = 0
        update_hangman(mistakes)

        #display score and attempts on screen
        score_label = tk.Label(game_interface,text=f"Score = {win_count} ", font=("Helvetica", 18) ,bg="#81d39a",width=15,height=1)
        score_label.place(x=1100 , y= 50)
        #Skip Button
        skip = tk.Button(game_interface,text="SKIP" , command=new_game ,  width=25,height=2,bg="yellow")
        skip.place(x=900,y=700)

        game_interface.withdraw()

        #ScoreBoard Interface
        score_board = tk.Toplevel()
        score_board.title("SCORE BOARD")
        #background of scoreboard
        jpg2_image = Image.open("back.jpg")
        jpg2_image = jpg2_image.resize((1600,900),Image.LANCZOS)
        background2_image = ImageTk.PhotoImage(jpg2_image)
        background2_label = tk.Label(score_board,image=background2_image)
        background2_label.place(relwidth=1,relheight=1)
        score_board.attributes('-fullscreen',True)
        
        widgets = tk.Frame(score_board,bg='#B1A2CA')
        widgets.place(x=650 , y=150)
        
        
        #texts of scoreboard
        game_over = tk.Label(widgets,text="GAME OVER" , font=("Helvetica", 40) , fg='red',bg='#B1A2CA')
        game_over.pack(pady=20)

        score_text = tk.Label(widgets,text="Your Total Score is :" , font=("Helvetica", 20) , fg='white',bg='#B1A2CA')
        score_text.pack()

        score2_label = tk.Label(widgets,text=win_count , font=("Helvetica", 50) , fg='yellow',bg='#B1A2CA',width=5,height=2)
        score2_label.pack(pady=10)

        play_again = tk.Label(widgets,text="Do You Want to Play Again ?" , font=("Helvetica", 20) , fg='white',bg='#B1A2CA')
        play_again.pack()

        #buttons of scoreboard
        play_button = tk.Button(widgets,text="Yes",bg="yellow", fg="black",command=back_to_game, width=12,height=2)
        play_button.pack(pady=10)
        back_menu = tk.Button(widgets,text="No",bg="yellow", fg="black",command=back_to_menu2, width=12,height=2)
        back_menu.pack(pady=10)
        exit_button = tk.Button(widgets, text="Exit",  bg="yellow", fg="black", command=root.quit , width=20,height=2)
        exit_button.pack(pady=10)

        score_board.withdraw()
        
        root.mainloop()
        