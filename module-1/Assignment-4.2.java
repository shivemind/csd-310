/*
Author: Daniel Shively
Date: Sat Jun 10
Assignment: Assignment 4
*/

/*
Purpose: This program prompts a user to enter two strings and then checks if either 
of the first string is a substring of the second string or vice versa.
*/

import java.util.Scanner; 

public class SubstringChecker {

    public static void main(String[] args) {
        // Create a new Scanner object for user input
        Scanner scanner = new Scanner(System.in); 

        // Prompt the user to enter the first string
        System.out.println("Please enter the first string:");
        String string1 = scanner.nextLine();

        // Prompt the user to enter the second string
        System.out.println("Please enter the second string:");
        String string2 = scanner.nextLine();

        // Call the checkSubstring function to check if either string is a substring of the other
        checkSubstring(string1, string2);
        
        // Close the scanner object to prevent memory leaks
        scanner.close();
    }

    // Function to check if either string is a substring of the other
    public static void checkSubstring(String string1, String string2) {
        if(string1.contains(string2)) {
            System.out.println("The second string is a substring of the first string.");
        } else if(string2.contains(string1)) {
            System.out.println("The first string is a substring of the second string.");
        } else {
            System.out.println("Neither string is a substring of the other.");
        }
    }
}