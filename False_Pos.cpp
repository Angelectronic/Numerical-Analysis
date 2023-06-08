#include <iostream>
#include <iomanip>   
#include <stdlib.h>
#include <stdio.h>  
#include <math.h>
#include <string> 
#include <algorithm>
#include <vector>
#include <fstream>
 
using namespace std;

#define TOL 0.0001
#define N 100

double Expression(double x) {
	return pow(x, 2) - 6; // Change this
}

void False_Pos (double p0, double p1) {
	int i = 2;
	double q0 = Expression(p0);
	double q1 = Expression(p1);
	
	while(i <= N) {
		double p = p1 - q1 * (p1 - p0) / (q1 -q0);
		
		cout << "Buoc: " << i - 1 << " p = " << p << endl;
		
		if (p - p1 < TOL) {
			cout << "Nghiem gan dung la: " << p << endl;
			cout << "Sau " << i - 1 << " buoc" << endl;
			return;
		}
		
		i++;
		double q = Expression(p);
		
		if (q * q1 < 0) {
			p0 = p1;
			q0 = q1;
		}
	
		p1 = p;
		q1 = q; 
	}
	
	cout << "The method failed after " << N <<" iterations";
}
 
int main()
{
    False_Pos(3, 2);
}
