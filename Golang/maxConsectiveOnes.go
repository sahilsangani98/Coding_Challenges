func findMaxConsecutiveOnes(nums []int) int {
    var lastMaxConsecNum = 0 // Remembers last Maximum Consecutive number
    var currMaxConsecNum = 0 // Remembers current Maximum Consecutive number
    
    for idx := 0; idx < len(nums); idx++ {
        if nums[idx] == 1{
            currMaxConsecNum+=1
            
            // Check if Current Consecutive number is greater Last Consecutive number
            if currMaxConsecNum > lastMaxConsecNum{
                lastMaxConsecNum = currMaxConsecNum
            }
        } else{
            // Reset Current Consecutive number
            currMaxConsecNum = 0
        }
	}
    return lastMaxConsecNum
}