#!/usr/bin/python3
import random #system choose the random number
n=(int(input("press 1 to play"))) #
i=0
j=0
while(n==1):
    t=["rock","paper","scissors"]
    Computer=t[random.randint(0,2)] #computer chooses a random number from 1 and 2 
    print("Enter your Choice:-") #it used to choose our choice
    Player="False"
    Player=input("rock, paper, scissors")
    print("player",Player,"computer",Computer)
    if(Computer==Player): #the choices between player and computer is same 
        print("tie!") #there is a tie between computerand player
    elif(Computer=="rock"): #if computer chose rock
        if(Player=="paper"): #if player chose paper
            print("The computer played: ",Computer) 
            print("The Player played: ",Player)
            print("The paper Wraps the stone!") #output the paper wraps the rock
            print("Player Wins!") #output player wins
            i=i+1
        else:
            print("Computer Wins")
            j=j+1
    elif(Computer=="paper"): #if computer chose paper
        if(Player=="scissors"): #if player chose scissors
            print("The computer played: ",Computer) 
            print("The Player played: ",Player)
            print("The scissors Cuts paper!") #output the scissors cuts the paper
            print("Player Wins!") #output player wins
            i=i+1
        else:
            print("Computer Wins")

            j=j+1
    elif(Computer=="scissors"): #computer chose scissors
        if(Player=="rock"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("rock Breaks the scissors")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")
            j=j+1
    if(i>j):
        print("player leads by ",i-j)
    elif(i==j):
        print("The Scores are tied ")
    else:
        print("computer leads by ",j-i)
