#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define MAX_LINE_LEN 200
#define MAX_EVENTS 1000



//swaps values in an array
void swap(int* first, int* second)
{
	int temp = *first;
	*first = *second;
	*second = temp;
}


// Function to perform Selection Sort
void SelectionSort(int arr[],int arr2[],int arr3[], int arr4[], int arr5[], int n)
{
	int i, j, min_idx;

	// One by one move boundary of arr which is month
    
	for (i = 0; i < n - 1; i++) {

		// Find the minimum element in unsorted array
		min_idx = i;
		for (j = i + 1; j < n; j++){
			if (arr[j] < arr[min_idx]){//month
				min_idx = j;
			}else if(arr[j] == arr[min_idx]){
			    if(arr2[j]<arr2[min_idx]){//if months are same then sort by days
			        min_idx = j;
			    }else if(arr2[j]==arr2[min_idx]){//if days are same sort by hours
			        if(arr3[j]<arr3[min_idx]){
			            min_idx = j;
			        }else if(arr3[j] == arr3[min_idx]){//if hours are same sort by minute
                        if(arr4[j]<arr4[min_idx]){
                            min_idx = j;
                        }
                    }
			    }
			}
		}
		// Swap the found minimum element
		// with the first element
		swap(&arr[min_idx], &arr[i]);
		swap(&arr2[min_idx], &arr2[i]);
		swap(&arr3[min_idx], &arr3[i]);
        swap(&arr4[min_idx], &arr4[i]);
        swap(&arr5[min_idx], &arr5[i]);
	}
}
//counts the number of events collected 
int event_counter(int arr[],int n){
    int counter = 0;
    int i = 0;

    while(i < n){
        if(arr[i] != 0){
            counter += 1;
        }else{
            return counter;
        }
        i+=1;
    }
}

//determines whether or not an event is within the given date range
int Is_date_in_range(int start_month, int start_day, int end_month, int end_day, int event_month, int event_day){

    int smonth = start_month;
    int sday = start_day;
    int emonth = end_month;
    int eday = end_day;
    int evemonth = event_month;
    int eveday = event_day;


    //case the start month and end month are the same
    if(smonth == emonth){
        if(sday <= eveday && eveday <= eday){
            return(1);//event day is either the same or bigger than start day and smaller or the same as end day
        }else{
            return(0);// event day is either bigger than end day or smaller than start day
        }
    }else if(smonth <= evemonth && evemonth <= emonth){
        if(smonth == evemonth && sday > eveday){
            return(0);
        }else if(emonth == evemonth && eday < eveday){
            return(0);
        }else{
            return(1);
        }
    }
    return(0);
}

struct event {
    char desc[100];
    char timezone[100];
    char loca[100];
    int day;
    int month;
    int year;
    char dweek[20];
    int startHour;
    int startMin;
    int endHour;
    int endMin;
    bool isStartPM;
    bool isEndPM;
};
//prints a single event, does not handle any of the dashes or the month
void print_function(bool startPM, int Shour, int Smin, bool endPM, int Ehour, int Emin){
    struct event eventData;
    eventData.isStartPM = startPM;
    eventData.startHour = Shour;
    eventData.startMin = Smin;
    eventData.isEndPM = endPM;
    eventData.endHour = Ehour;
    eventData.endMin = Emin;
    


    if(eventData.isStartPM){
            if(eventData.startHour >= 10){
                printf("%d:",eventData.startHour);
            }else{
                printf("0%d:",eventData.startHour);
            }
            if(eventData.startMin < 10){
                printf("0%d ",eventData.startMin);
            }else{
                printf("%d ",eventData.startMin);
            }
            printf("PM to ");
        }else{
            if(eventData.startHour >= 10){
                printf("%d:",eventData.startHour);
            }else{
                printf("0%d:",eventData.startHour);
            }
            if(eventData.startMin < 10){
                printf("0%d ",eventData.startMin);
            }else{
                printf("%d ",eventData.startMin);
            }
            printf("AM to ");
        }
        if(eventData.isEndPM){
            if(eventData.endHour >= 10){
                printf("%d:",eventData.endHour);
            }else{
                printf("0%d:",eventData.endHour);
            }
            if(eventData.endMin < 10){
                printf("0%d ",eventData.endMin);
            }else{
                printf("%d ",eventData.endMin);
            }
            printf("PM: ");
        }else{
            if(eventData.endHour >= 10){
                printf("%d:",eventData.endHour);
            }else{
                printf("0%d:",eventData.endHour);
            }
            if(eventData.endMin < 10){
                printf("0%d ",eventData.endMin);
            }else{
                printf("%d ",eventData.endMin);
            }
            printf("AM: ");
        }
   

}




int main(int argc, char *argv[])
{

FILE *fp;
char *filename;
char buff[MAX_LINE_LEN];


struct tm start;
struct tm end;
char *month_names[]={"January","February","March","April","May","June","July","August","September","October","November","December"};

char *start2;
char *end2; 

//Getting the start + end dates and the filename
start2 = argv[1];
end2 = argv[2];
filename = argv[3];

//skipping the --start= and --end= and --filename=
start2+=8;
end2+=6;
filename +=7;

//getting the start and end dates into a tm variable
sscanf(start2,"%d/%d/%d",&start.tm_year,&start.tm_mon,&start.tm_mday);

start.tm_year = start.tm_year - 1900;

sscanf(end2,"%d/%d/%d",&end.tm_year,&end.tm_mon,&end.tm_mday);

end.tm_year = end.tm_year - 1900;

fp = fopen(filename,"r");




int FileLocations[MAX_EVENTS] = {0}; //keep track of the location in the file of the selected event as well as its month, day, hour of start, minutes of start. The order of the each value are all connected. 
int months[MAX_EVENTS]= {0};
int days[MAX_EVENTS]= {0};
int hours[MAX_EVENTS] = {0};
int minutes[MAX_EVENTS] = {0};
int tracker = 0;





//input line is at calendar
fgets(buff,MAX_LINE_LEN,fp);

//input line is at first event
fgets(buff,MAX_LINE_LEN,fp);

int z = 0;

while(z != 1){



//this saves the location in the file that points to the start of the <event> line such that the next fgets will return <event> not whatever is on the line after <event>
    int save = ftell(fp);
    save = save - strlen(buff);
 
//skips down 4 lines so that buff contains <day>
    int i = 0;
    while(i<4){
        fgets(buff,MAX_LINE_LEN,fp);
        i+=1;
    }

    int temp_day = 0;
    int temp_month = 0;
    int temp_hour = 0;
    int temp_min = 0;

    sscanf(buff," <day>%d</day>\n",&temp_day);

//buff now contains <month>
    fgets(buff,MAX_LINE_LEN,fp);

    sscanf(buff," <month>%d</month>\n",&temp_month);

//buff now contains <start>
    i = 0;
    while(i<3){
        fgets(buff,MAX_LINE_LEN,fp);
        i+=1;
    }

    sscanf(buff," <start>%d:%d</start>\n",&temp_hour,&temp_min);

    if(Is_date_in_range(start.tm_mon,start.tm_mday,end.tm_mon,end.tm_mday,temp_month,temp_day) == 1){
        
        FileLocations[tracker] = save;
        months[tracker] = temp_month;
        days[tracker] = temp_day;
        hours[tracker] = temp_hour;
        minutes[tracker] = temp_min;
        tracker += 1;
        temp_day = 0;
        temp_month = 0;
        temp_hour = 0;
        temp_min = 0;
    }
//skips down to next <event> tag
    i = 0;
    while(i<3){
        fgets(buff,MAX_LINE_LEN,fp);
        i+=1;
    }
//check to see if its <calendar/> by checking is strlen = 11 because it is the only line with that length in the file
    if(strlen(buff) == 11){
        
        z = 1;
    }


}





//At this point I have 5 arrays with required events file location, month ,day ,hour and minutes along with a tracker variable indicating the current position in all 5 arrays. 
//Array values and tracker begins at 0 - MUST KEEP IN SYNC BETWEEN ALL 5

//sorting arrays such that earliest dates -----> later dates

int number_of_events = 0;
number_of_events = event_counter(months,MAX_EVENTS);


SelectionSort(months,days,hours,minutes,FileLocations,number_of_events);




//At this point I now have all the arrays sorted, last step is to print out the necessary data in the required format

//q,w,n,l are just iteration variables
int q = 0;
int w = 0;
int m = 0;
tracker = 0;
int len = 0;
int l = 0;
struct event eventData;

while(q<number_of_events){
    fseek(fp,FileLocations[q],SEEK_SET);
    fgets(buff,MAX_LINE_LEN,fp);
    while(w<11){
        switch(w){
            case 0:
                break;
            case 1:
                sscanf(buff,"  <description>%[^\t\n<]",eventData.desc);
                break;
            case 2:
                sscanf(buff,"  <timezone>%[^\t\n<]",eventData.timezone);
                break;
            case 3:
                sscanf(buff,"  <location>%[^\t\n<]",eventData.loca);
                break;
            case 4:
                sscanf(buff,"  <day>%d</day>",&eventData.day);
                break;
            case 5:
                sscanf(buff,"  <month>%d</month>",&eventData.month);
                break;
            case 6:
                sscanf(buff,"  <year>%d</year>",&eventData.year);
                break;
            case 7:
                sscanf(buff,"  <dweek>%[^\t\n<]",eventData.dweek);
                break;
            case 8:
                sscanf(buff,"  <start>%d:%d</start>",&eventData.startHour,&eventData.startMin);
                if(eventData.startHour > 12){
                    eventData.startHour = eventData.startHour - 12;
                    eventData.isStartPM = true;
                }else if(eventData.startHour == 12){
                    eventData.isStartPM = true;
                }
                break;
            case 9:
                sscanf(buff,"  <end>%d:%d</end>",&eventData.endHour,&eventData.endMin);
                if(eventData.endHour > 12){
                    eventData.endHour = eventData.endHour - 12;
                    eventData.isEndPM = true;
                }else if(eventData.endHour == 12){
                    eventData.isEndPM = true;
                }
                break;
        }

        fgets(buff,MAX_LINE_LEN,fp);
        w+=1;
    }
    
    if(q == 0){
        m = months[q] - 1;
        printf("%s %d, %d (%s)%n\n",month_names[m],eventData.day,eventData.year,eventData.dweek,&len);
        while(l < len){
            printf("-");
            l+=1;
        }
        l=0;
        printf("\n");

        print_function(eventData.isStartPM,eventData.startHour,eventData.startMin,eventData.isEndPM,eventData.endHour,eventData.endMin);
        printf("%s {{%s}} | %s",eventData.desc,eventData.loca,eventData.timezone);  

        if(q+1!=number_of_events){
            printf("\n");
        }
    }else{
        if(months[q]==months[q-1] && days[q] == days[q-1]){

            print_function(eventData.isStartPM,eventData.startHour,eventData.startMin,eventData.isEndPM,eventData.endHour,eventData.endMin);
            printf("%s {{%s}} | %s",eventData.desc,eventData.loca,eventData.timezone);

            if(q+1!=number_of_events){
                printf("\n");
            }
        }else{
            printf("\n");
            m = months[q] - 1;
            printf("%s %d, %d (%s)%n\n",month_names[m],eventData.day,eventData.year,eventData.dweek,&len);
            while(l < len){
                printf("-");
                l+=1;
            }
            l=0;
            printf("\n");

            print_function(eventData.isStartPM,eventData.startHour,eventData.startMin,eventData.isEndPM,eventData.endHour,eventData.endMin);
            printf("%s {{%s}} | %s",eventData.desc,eventData.loca,eventData.timezone);

            if(q+1!=number_of_events){
                printf("\n");
            }
        }


    }


    w=0;
    q+=1;
    eventData.isStartPM = false;
    eventData.isEndPM = false;
}



exit(0);
}