package com.company;

import java.util.Arrays;

public class Main {

    public static int[] mergeSortedArrays(int[] array1, int[] array2) {

        if(array1 == null || array2 == null) {
            throw new IllegalArgumentException("Passed in arrays must be non null");
        }

        int array1Length = array1.length;
        int array2Length = array2.length;

        int[] mergedArray = new int[ array1Length + array2Length ];

        int i=0, j=0, k=0;

        while(i < array1Length && j < array2Length) {

            int array1_val = array1[i];
            int array2_val = array2[j];

            if( array1_val == array2_val) {
                mergedArray[k++] = array1_val;
                mergedArray[k++] = array2_val;
                j++;
                i++;
            }
            else if( array1_val > array2_val) {
                mergedArray[k++] = array2_val;
                j++;
            }
            else {
                mergedArray[k++] = array1_val;
                i++;
            }
        }

        while (i < array1Length) {
            mergedArray[k] = array1[i];
            i++;
        }

        while (j < array2Length) {
            mergedArray[k++] = array2[j];
            j++;
        }



        return mergedArray;
    }

    public static void main(String[] args) {

        int[] array1 = {1, 2, 3, 50};

        int[] array2 = {10, 20, 30, 40};

        System.out.println(Arrays.toString(mergeSortedArrays(array1, array2)));

    }
}

