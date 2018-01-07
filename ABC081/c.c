#include <stdio.h>
#include <stdlib.h>

int N,K,cnt,ans;

int asc(const void *a, const void *b) {
  return *(int *)a - *(int *)b;
}

int main ()
{
scanf ("%d %d\n" ,&N ,&K);

int A[N];
int B[N];  // 各要素の数

for ( int i =0; i < N ; i ++){
	scanf ("%d", &A[i]);
}

for ( int i =0; i < N ; i ++){
	B[i] = 0;
}

for (int i=0;i<N;i++){
	for(int j=0;j<N;j++){
		if(i == A[j]){
			//printf("add:%d-%d\n", i,A[i]);
			B[i]++;
		}
	}
	if(B[i]>0){
		cnt++;
	}
}

//printf("cnt:%d\n", cnt);

qsort(B, sizeof(B) / sizeof(int), sizeof(int), asc);
int change = cnt - K;

if (cnt > K){
	for(int i=0; i < N; i++){
		if(B[i] != 0){
			ans += B[i];
			change--;
		}
		if(change == 0){
			break;
		}
	}
}

printf("%d\n", ans);

}
