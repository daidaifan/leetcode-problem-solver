/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

*/

#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

int max(int a, int b) {
    if(a < b) {
        return b;
    }
    return a;
}

int maxProfit(int k, int* prices, int pricesSize) {
    printf("k=%d, pricesSize=%d\n", k, pricesSize);
    if(pricesSize <= 1) {
        return 0;
    }
    int* holds = (int*) malloc(sizeof(int) * pricesSize);
    int* release = (int*) malloc(sizeof(int) * pricesSize);
    for(int i=0;i<pricesSize;i++) {
        holds[i] = INT_MIN;
        release[i] = 0;
    }
    /* complexity: n * k */
    for(int i=0;i<pricesSize;i++) {
        for(int _k=k-1;_k>=0;_k--) {
            int last_release = 0;
            if(_k != 0) {
                last_release = release[_k-1];
            }
            release[_k] = max(release[_k], holds[_k] + prices[i]);
            holds[_k] = max(holds[_k], last_release - prices[i]);
        }
    }
    int max_release = INT_MIN;
    for(int i=0;i<pricesSize;i++) {
        if(release[i] > max_release) {
            max_release = release[i];
        }
    }
    return max_release;
}

int main() {
    int pricesSize = 6;
    int prices[6] = {7, 1, 5, 3, 6, 4};
    int k = 2;

    int profit = maxProfit(k, prices, pricesSize);
    printf("profit = %d\n", profit);
    return profit;
}


