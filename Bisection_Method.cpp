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
	return pow(x, 3) + 4 * pow(x, 2) - 10; // Change this
}

void Bisection (double a, double b) {
	if (Expression(a) * Expression(b) > 0) {
		cout << "a, b khong hop le" << endl;
		return;
	}
	
	double mid = a;
	double count = 0;
	
	cout << "Buoc" << "     a" << "     b" << "     mid" << "     f(mid)" << endl;
	
	while((b - a) >= EP) {
		count++;
		mid = (b + a) / 2;
		
		cout << " " << count << "      " << a << "     " << b << "    " << mid << "   " << Expression(mid) << endl;
		
		if (Expression(mid) == 0) {
			break;
		}
		else if (Expression(mid) < 0) {
			a = mid;
		}
		else {
			b = mid;
		}
	}
	
	cout << "Nghiem gan dung la: " << mid << endl;
	cout << "Sau " << count << " buoc" << endl;
}
 
int main()
{
    Bisection(1, 2);
}
