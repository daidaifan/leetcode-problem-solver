/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
*/

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int max(int a, int b) {
    if(a > b) {
        return a;
    }
    return b;
}

int maxProfit(int* prices, int pricesSize) {
    int hold1 = INT_MIN, hold2 = INT_MIN;
    int release1 = 0, release2 = 0;
    for (int i=0;i<pricesSize;i++) {
        int price = prices[i];
        release2 = max(release2, hold2 + price);
        hold2 = max(hold2, release1 - price);
        release1 = max(release1, hold1 + price);
        hold1 = max(hold1, -price);
        printf("price = %d, release2=%d, hold2=%d, release1=%d, hold1=%d\n", price, release2, hold2, release1, hold1);
    }
    return release2;
}

int main() {
    int pricesSize = 6;
    int prices[6] = {7, 1, 5, 3, 6, 4};

    int profit = maxProfit(prices, pricesSize);
    printf("profit = %d\n", profit);
    return profit;
}

/*
price = 7, release2=0, hold2=-7, release1=0, hold1=-7
price = 1, release2=0, hold2=-1, release1=0, hold1=-1
price = 5, release2=4, hold2=-1, release1=4, hold1=-1
price = 3, release2=4, hold2=1, release1=4, hold1=-1
price = 6, release2=7, hold2=1, release1=5, hold1=-1
price = 4, release2=7, hold2=1, release1=5, hold1=-1
profit = 7
*/

/*
The thinking is simple and is inspired by the best solution from Single Number II (I read through the discussion after I use DP).
Assume we only have 0 money at first;
4 Variables to maintain some interested 'ceilings' so far:
The maximum of if we've just buy 1st stock, if we've just sold 1nd stock, if we've just buy 2nd stock, if we've just sold 2nd stock.
Very simple code too and work well. I have to say the logic is simple than those in Single Number II.

public class Solution {
    public int maxProfit(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
        int release1 = 0, release2 = 0;
        for(int i:prices){                              // Assume we only have 0 money at first
            release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
            hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
            release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
            hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far. 
        }
        return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}
*/



