int maxProfit(int* prices, int pricesSize){
    int curMin, curProfit;
    curMin = prices[0];
    curProfit = 0;
    
    // Loop through every num in the array
    for (int i=1; i < pricesSize; i++) {
        // If the num < current minimum, store the new minimum
        if (prices[i] < curMin) {
            curMin = prices[i];
        }
        // Otherwise, see if (num - minimum) gives the most profit
        else if (prices[i] - curMin > curProfit) 
            curProfit = prices[i] - curMin;
    };
    
    return curProfit;
}