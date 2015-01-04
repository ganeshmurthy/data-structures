package com.company;

public class BubbleSort {

    public static void swap(int[] unSortedArray, int x, int y) {
        int temp = unSortedArray[x];
        unSortedArray[x] = unSortedArray[y];
        unSortedArray[y] = temp;
    }

    /**
     * Simple sorting algorithm that repeatedly steps through the list to be sorted, compares each
     * pair of adjacent items and swaps them if they are in the wrong order
     * Time complexity is O(N*N).
     * Space complexity is O(1) since the array is sorted in place.
     * @param unSortedArray
     */
    public static void bubbleSort(int[] unSortedArray) {

        if (unSortedArray == null || unSortedArray.length == 0) {
            throw new IllegalArgumentException("unSortedArray must not be null or empty");
        }

        boolean anySwap = true;

        while(anySwap) {

            anySwap = false;

            for (int i = 0; i < unSortedArray.length - 1; i++) {
                if (unSortedArray[i] > unSortedArray[i+1]) {
                    swap(unSortedArray, i, i+1);
                    anySwap = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arrayToSort = {3, 2, 1, 6};
        bubbleSort(arrayToSort);
    }
}
