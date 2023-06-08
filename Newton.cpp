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

#define EP 0.0001

double Expression(double x) {
	return pow(x, 3) - 2 * pow(x, 2) - 5; // Change this
}

double Derivative(double x) {
	return 3 * x * x - 4 * x;
}

void Newton (double p) {
	int count = 0;
	
	double p0 = p;
	double p1 = p0 - Expression(p0) / Derivative(p0);

	while(abs(p1 - p0) > EP) {
		count++;
		
		cout << "Buoc: " << count << " p = " << p1 << endl;
		
		p0 = p1;
		p1 = p0 - Expression(p0) / Derivative(p0);
	}
	
	cout << "Buoc: " << count << " p = " << p1 << endl;
	
	cout << "Nghiem gan dung la: " << p1 << endl;
	cout << "Sau " << count << " buoc" << endl;
}
 
int main()
{
    Newton(3);
}
