#include<stdio.h>
#include<malloc.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/**
 * 统计字符串词频
 */
void str2map(char *s, int * sMap){
    int key;
    for (int i = 0; s[i] != '\0'; i++){
        key = s[i] - 'a';
        sMap[key] = sMap[key] ? sMap[key] + 1 : 2;
    }
}

// O(n+m)
int* findAnagrams(char * s, char * p, int* returnSize){
    int i, l, r;
    int sLen,pLen;
    for (sLen = 0; s[sLen] != '\0'; sLen++);
    for (pLen = 0; p[pLen] != '\0'; pLen++);
    int* ret = (int *) malloc(sizeof(int) * sLen);
    * returnSize = 0;
    int pMap[26] = {0};
    int pMapCopy[26];
    str2map(p, pMap); // 生成p字符串的词频字典 =》 查找字典
    for (i = 0; i < 26; i++) pMapCopy[i] = pMap[i];
    l = 0,r = -1;  // [l..r] 区间为p中的 部分-> 全部 字符
    while (s[r + 1] != '\0'){ // 右边滑到最后一位结束循环
        if (pMap[s[r + 1] - 'a'] > 1){ // 如果右边的下一位s[r+1]在查找字典中
            pMap[s[++r] - 'a']--; // 则将其加入区间，并消耗掉此字符
            if (r - l + 1 == pLen){ // 区间长度与p相同 说明区间内为p的异构
                ret[(* returnSize)++] = l; // 将区间左边界地址存入结果集
                pMap[s[l++] - 'a']++;  // 区间收缩,并将左边移除的数据重新加入查找字典
            }
        }else{ // 如果右边下一位不在查找字典中则，分两种情况
            if (pMap[s[r + 1] - 'a'] > 0){ // 右边的下一位依然在p字符串中
                // 则说明区间中此字符超过了p中的量
                pMap[s[l++] - 'a']++; // 缩小区间，直到能将s[r+1]包含进区间
            }else{ // 右边下一位不在字符串p中，则包含此字符的一定不是p的异构符
                for (i = 0; i < 26; i++) pMap[i] = pMapCopy[i];
                r ++; // 直接将区间清零，并重置查找字典
                l = r + 1; // 并将做边界移动到此字符的下一位
            }
        }
    }
    return ret;
}

int main(int argc, char const *argv[]){
    int * retSize = (int *) malloc(sizeof(int));
    char s[] = "cbaebabacd";
    char p[] = "abc";
    /* int pMap[26] = {0};
    int pMapCopy[26];
    str2map(p, pMap);
    for (int i = 0; i < 26; i++)
        printf("%d ",pMap[i]);
    for (int i = 0; i < 26; pMapCopy[i++] = pMap[i-1]);
    printf("\n--------\n");
    for (int i = 0; i < 26; i++)
        printf("%d ", pMapCopy[i]); */
    
    int * ret = findAnagrams(s, p, retSize);
    for (int i = 0; i <  * retSize; i++)
        printf("%d ",ret[i]);
    return 0;
}
