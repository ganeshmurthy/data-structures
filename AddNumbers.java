package com.company;

/**
 * Add two numbers without using the + operator
 */
public class AddNumbers {
    public static void main(String[] args) {
        System.out.println(addNumbers(-13, 0));
    }

    public static int addNumbers(int a, int b) {
        if (b > 0) {
            while (b > 0) {
                a++;
                b--;
            }
        }
        else {
            while (b < 0) {
                a--;
                b++;
            }
        }

        return a;
    }
}
