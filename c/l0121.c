/*
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
*/

#include<stdio.h>
#include<stdlib.h>

int maxProfit(int* prices, int pricesSize) {
    int min_index = 0;
    int max_profit = 0;
    for(int i=1;i<pricesSize;i++) {
        if(prices[i] - prices[min_index] > max_profit) {
            max_profit = prices[i] - prices[min_index];
        }
        else if(prices[i] < prices[min_index]) {
            min_index = i;
        }
    }
    return max_profit;
}

int main() {
    int pricesSize = 6;
    int prices[6] = {7, 1, 5, 3, 6, 4};

    int profit = maxProfit(prices, pricesSize);
    printf("profit = %d\n", profit);
    return profit;
}


