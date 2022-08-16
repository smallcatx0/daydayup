#include<stdio.h>
#include<malloc.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target,int* resSize) {
    int i,j;
    int* res = (int *)malloc(sizeof(int)*2);
    * resSize = 2;
    for(i=0;i<numsSize-1; ++i){
        for(j=i+1; j<numsSize; ++j){
            if(nums[i] + nums[j] == target){
                res[0] = i;
                res[1] = j;
               break;
            }
        }
    }
     return res;
}

int main(){
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int * resSize = (int * )malloc(sizeof(int));
    int * res = twoSum(nums, 4, target, resSize);
    printf("%d %d", res[0], res[1]);
    return 0;
}
