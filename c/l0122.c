/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
*/

#include<stdio.h>
#include<stdlib.h>

int maxProfit(int* prices, int pricesSize) {
    int current_index = 0;
    int acc_profit = 0;
    for(int i=1;i<pricesSize;i++) {
        if(prices[i] - prices[current_index] > 0) {
            acc_profit += prices[i] - prices[current_index];
        }
        current_index = i;
    }
    return acc_profit;
}

int main() {
    int pricesSize = 6;
    int prices[6] = {7, 1, 5, 3, 6, 4};

    int profit = maxProfit(prices, pricesSize);
    printf("profit = %d\n", profit);
    return profit;
}


