func runningSum(nums []int) []int {
    var lastSum = 0
    var result = make([]int,0) 
    for _, CurNum := range nums {
        result = append(result, CurNum+lastSum)
        lastSum = CurNum+lastSum
    }
    return result
}
