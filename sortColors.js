/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let i = 0;
    let j = nums.length - 1;
    let k=0;
    
    while(k <= j){
        switch(nums[k]){
            case 0:
                if(k > i){
                    [nums[k], nums[i]] = [nums[i], nums[k]]
                }else{
                    k += 1
                }
                i += 1
                break
            case 2:
                if(k<j){
                    [nums[k], nums[j]] = [nums[j], nums[k]]
                }else{
                    k += 1
                }
                j -= 1
                break
            case 1:
                k += 1
                break
        }
    }
};
