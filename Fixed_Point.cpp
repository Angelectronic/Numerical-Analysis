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

#define EP 0.01

double Expression(double x) {
	return pow(3 * x * x + 3, 0.25); // Change this
}

void Fixed_Point (double p) {
	
	int count = 0;
	
	double p0 = p;
	double p1 = Expression(p0);

	while(abs(p1 - p0) > EP) {
		count++;
		
		cout << "Buoc: " << count << " p = " << p1 << endl;
		
		p0 = p1;
		p1 = Expression(p0);
	}
	
	cout << "Buoc: " << count << " p = " << p1 << endl;
	
	cout << "Nghiem gan dung la: " << p1 << endl;
	cout << "Sau " << count << " buoc" << endl;
}
 
int main()
{
    Fixed_Point(1);
}
