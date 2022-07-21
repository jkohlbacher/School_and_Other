#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <fstream>
#include <cassert>

#include "scrabble.hpp"

int Score(const std::string word)
{
    int sum{0};
    
 
std::string s1{"aeilnorstu"};
std::string s2{"dg"};
std::string s3{"bcmp"};
std::string s4{"fhvwy"};
std::string s5{"k"};
std::string s8{"jx"};
std::string s10{"qz"};

int sum{0};

for(auto g:word){

	for(auto one:s1){
		if(one == g){
			sum+=1;
		}
	}
	for(auto two:s2){
		if(two == g){
			sum+=2;
		}
	}
	for(auto three:s3){
		if(three == g){
			sum+=3;
		}
	}
	for(auto four:s4){
		if(four == g){
			sum+=4;
		}
	}
	for(auto five:s5){
		if(five == g){
			sum+=5;
		}
	}
	for(auto eight:s8){
		if(eight == g){
			sum+=8;
		}
	}
	for(auto ten:s10){
		if(ten == g){
			sum+=10;
		}
	}

}

return sum;
}


dict_type Read_Dictionary(const std::string filename)
{
    // your code goes here
}

words_set_type Find_Best_Words(const dict_type &dict, std::string tiles)
{
    // your code goes here
}

