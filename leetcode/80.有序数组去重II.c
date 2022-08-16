#include<stdio.h>

int removeDuplicates(int* nums, int numsSize){
    if(numsSize <= 2) return numsSize;
    int k = 0;
    int times = 1;
    for (int i = 1; i < numsSize; i ++){
        if (nums[k] == nums[i]){
            times ++;
            if (times <= 2){
                k ++;
                nums[k] = nums[i];
            }
        }else{
            k++;
            nums[k] = nums[i];
            times = 1;
        }
    }
    return k+1;
    
}
int main(){
    int nums[] = {1,2,2};
    int res;
    res = removeDuplicates(nums,3);
    for (int i = 0; i < res; i++){
        printf("%d ",nums[i]);
    }
    
    return 0;
}
 
