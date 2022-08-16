# include<stdio.h>

int minL (int a,int b){
    return a > b? b : a;
}
int maxL (int a, int b){
    return a > b? a: b;
}

int maxArea(int* height, int heightSize){
    int i = 0;
    int j = heightSize - 1;
    int area = -1;
    while (i < j){
        area = maxL(area, minL(height[i], height[j]) * (j - i));
        if (height[i] < height[j])
            i++;
        else
            j--;
    }
    return area;
}



int main(int argc, char const *argv[]){
    int heights[] = {1,8,6,2,5,4,8,3,7};
    int res = maxArea(heights,9);
    printf("%d",res);
    return 0;
}
