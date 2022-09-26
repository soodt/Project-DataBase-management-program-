import pandas as pd
import matplotlib.pyplot as plt
import sys 
def main_menu():
        print(" _________________________________ ")
        print("|                                 |")
        print("|          ~ MAIN MENU~           |")
        print("|_________________________________|")
        print("|                                 |")
        print("|1. DATA COLLECTION               |")
        print("|2. DATA MANIPULATION             |")
        print("|3. DATA ANALYSIS                 |")
        print("|4. DATA VISUALISATION            |")
        print("|5. EXIT                          |")
        print("|_________________________________|")
def collection():
        print(" _______________________________ ")
        print("|                               |")
        print("|     ~DATA COLLECTION MENU~    |")
        print("|_______________________________|")
        print("|                               |")
        print("|1. IMPORT DATA FROM CSV        |")
        print("|2. IMPORT DATA FROM TEXT       |")
        print("|3. RETURN TO MAIN MENU         |")
        print("|_______________________________|")
def manipulation():
        print(" _________________________________ ")
        print("|                                 |")
        print("|   ~DATA MANIPULATION MENU~      |")
        print("|_________________________________|")
        print("|                                 |")
        print("|1. INSERT ROW                    |")
        print("|2. DELETE ROW                    |")
        print("|3. UPDATE INFORMATION            |")
        print("|4. SORT DATA                     |")
        print("|5. ADD ANOTHER DATAFRAME FILE    |")
        print("|6. RETURN TO MAIN MENU           |")
        print("|_________________________________|")
def insert_row():
            print(" _________________________________________ ")
            print("|                                         |")
            print("|       ~INSERT ROW MENU~                 |")
            print("|_________________________________________|")
            print("|                                         |")
            print("|1. INSERT ROW AT THE END                 |")
            print("|2. INSERT ROW AT SPECIFIC POSITION       |")
            print("|3. RETURN TO MANIPULATION MENU           |")
            print("|_________________________________________|")
def update():
            print(" ________________________________ ")
            print("|                                |") 
            print("|         ~UPDATE MENU~          |")
            print("|________________________________|")
            print("|                                |")
            print("|1. UPDATE TOTAL POPULATION      |")
            print("|2. UPDATE TOTAL LITERATES       |")
            print("|3. UPDATE SEX RATIO             |")
            print("|4. UPDATE LITERACY RATE         |")
            print("|5. UPDATE TOTAL GRADUAGETS      |")
            print("|6. UPDATE STATE CODE            |")
            print("|7. RETURN TO MANIPULATION MENU  |")
            print("|________________________________|")
def sort():
            print(" ________________________________ ")
            print("|                                |")
            print("|        ~SORTING MENU~          |")
            print("|________________________________|")
            print("|                                |")
            print("|1. SORT ASCENDING               |")
            print("|2. SORT DESCENDING              |")
            print("|3. RETURN TO MANIPULATION MENU  |")
            print("|________________________________|")
def sort_asc():
                print(" _______________________________________ ")
                print("|                                       |")
                print("|        ~SORTING MENU(ASCENDING)~      |")
                print("|_______________________________________|")
                print("|                                       |")
                print("|1. SORT BY TOTAL POPULATION            |")
                print("|2. SORT BY LITERACY RATE               |")
                print("|3. SORT BY SEX RATIO                   |")
                print("|4. SORT BY GRADUATES                   |")
                print("|5. SORT BY STATES                      |")
                print("|6. SORT BY MALE GRADUATES              |")
                print("|7. RETURN TO SORTING MENU              |")
                print("|_______________________________________|")
def sort_des():
                print(" ______________________________________ ")
                print("|                                      |")
                print("|        ~SORTING MENU(DESCENDING)~    |")
                print("|______________________________________|")
                print("|                                      |")
                print("|1. SORT BY TOTAL POPULATION           |")
                print("|2. SORT BY LITERACY RATE              |")
                print("|3. SORT BY SEX RATIO                  |")
                print("|4. SORT BY GRADUATES                  |")
                print("|5. SORT BY STATES                     |")
                print("|6. SORT BY MALE GRADUATES             |")
                print("|7. RETURN TO SORTING MENU             |")
                print("|______________________________________|")
def another_df():
            print(" _________________________________________ ")
            print("|                                         |")
            print("|     ~ADDING ANOTHER DATAFRAME~          |")
            print("|_________________________________________|")
            print("|                                         |")
            print("|1. ADD ANOTHER CSV FILE DATAFRAME        |")
            print("|2. ADD ANOTHER TEXT FILE DATAFRAME       |")
            print("|3. RETURN TO MANIPULATION MENU           |")
            print("|_________________________________________|")
def analysis():
        print(" ___________________________________ ")
        print("|                                   |")
        print("|      ~DATA ANALYSIS MENU~         |")
        print("|___________________________________|")
        print("|                                   |")
        print("|1. DISPLAY TOP RECORDS             |")
        print("|2. DISPLAY BOTTOM RECORDS          |")
        print("|3. DISPLAY PARTICULAR COLUMN(S)    |")
        print("|4. DISPLAY PARTICULAR ROW(S)       |")
        print("|5. RETURN TO MAIN MENU             |")
        print("|___________________________________|")
def column():
            print(" ___________________________________________________________________________ ")
            print("|                                                                           |")
            print("|                  ~DISPLAY COLUMN(S) MENU~                                 |")
            print("|___________________________________________________________________________|")
            print("|                                                                           |")
            print("|1. CITY NAME WITH STATE NAME & CODE                                        |")
            print("|2. CITY NAME WITH TOTAL POPULATION, MALE & FEMALE POPULATION               |")
            print("|3. CITY NAME WITH TOTAL LITERATES,MALE & FEMALE LITERATES                  |")
            print("|4. CITY NAME WITH SEX RATIO & CHILD SEX RATIO                              |")
            print("|5. CITY NAME WITH TOTAL LITERACY RATE,MALE & FEMALE LITERACY RATE          |")
            print("|6. CITY NAME WITH TOTAL GRADUATES,MALE & FEMALE GRADUATES                  |")
            print("|7. RETURN TO ANALYSIS MENU                                                 |")
            print("|___________________________________________________________________________|")
def row():
            print(" ___________________________________________________________________________ ")
            print("|                                                                           |")
            print("|                            ~DISPLAY ROW(S) MENU~                          |")
            print("|___________________________________________________________________________|")
            print("|                                                                           |")
            print("|1. COMPLETE DETAILS OF ALL CITIES BASED ON STATE                           |")
            print("|2. COMPLETE DETAILS OF ALL CITIES WITH FEMALE POPULATION>MALE POPULATION   |")
            print("|3. COMPLETE DETAILS OF ALL CITIES WITH FEMALE LITERATES>MALE LITERATES     |")
            print("|4. COMPLETE DETAILS OF ALL CITIES WITH FEMALE GRADUATES>MALE GRADUATES     |")
            print("|5. COMPLETE DETAILS OF CITY WITH MAX POPULATION                            |")
            print("|6. COMPLETE DETAILS OF CITY WITH MIN POPULATION                            |")
            print("|7. COMPLETE DETAILS OF CITY WITH HIGHEST CHILD SEX RATIO                   |")
            print("|8. RETURN TO ANALYSIS MENU                                                 |")
            print("|___________________________________________________________________________|")
def visualisation():
            print(" _________________________________________ ")
            print("|                                         |")
            print("|      ~DATA VISUALISATION MENU~          |")
            print("|_________________________________________|")
            print("|                                         |")
            print("|1. LINE GRAPH                            |")
            print("|2. BAR GRAPH                             |")
            print("|3. MULTIBAR GRAPH                        |")
            print("|4. RETURN TO MAIN MENU                   |")
            print("|_________________________________________|")
def line_graph():
                        print(" _________________________________________ ")
                        print("|                                         |")
                        print("|           ~LINE GRAPH MENU~             |")
                        print("|_________________________________________|")
                        print("|                                         |")
                        print("|1. CITY vs TOTAL POPULATION              |")
                        print("|2. CITY vs TOTAL LITERATES               |")
                        print("|3. CITY VS CHILD SEX RATIO               |")
                        print("|4. CITY vs TOTAL LITERATCY RATE          |")
                        print("|5. CITY vs TOTAL GRADUATES               |")
                        print("|6. CITY vs TOTAL MALE GRADUATES          |")
                        print("|7. CITY vs TOTAL FEMALE GRADUATES        |")
                        print("|8. RETURN TO VISUALISATION MENU          |")
                        print("|_________________________________________|")
def bar_graph():
                        print(" _________________________________________ ")
                        print("|                                         |")
                        print("|            ~BAR GRAPH MENU~             |")
                        print("|_________________________________________|")
                        print("|                                         |")
                        print("|1. CITY vs TOTAL MALE POPULATION         |")
                        print("|2. CITY vs TOTAL FEMALE POPULATION       |")
                        print("|3. CITY vs TOTAL MALE LITERATES          |")
                        print("|4. CITY vs TOTAL FEMALE LITERATE         |")
                        print("|5. CITY VS SEX RATIO                     |")
                        print("|6. CITY vs TOTAL MALE LITERATCY RATE     |")
                        print("|7. CITY vs TOTAL FEMALE LITERATCY RATE   |")
                        print("|8. RETURN TO VISUALISATION MENU          |")                        
                        print("|_________________________________________|")
def multibar_graph():
                        print(" ___________________________________________________________________ ")
                        print("|                                                                   |")
                        print("|                     ~MULTIBAR GRAPH MENU~                         |")
                        print("|___________________________________________________________________|")
                        print("|                                                                   |")
                        print("|1. COMPARE TOTAL MALE-FEMALE POPULATION OF DIFFERENT CITIES        |")
                        print("|2. COMPARE TOTAL MALE-FEMALE LITERATES OF DIFFERENT CITIES         |")
                        print("|3. COMPARE TOTAL MALE-FEMALE LITRACY RATE OF DIFFERENT CITIES      |")
                        print("|4. COMPARE TOTAL MALE-FEMALE GRADUAGETS OF DIFFERENT CITIES        |")
                        print("|5. RETURN TO VISUALISATION MENU                                    |")
                        print("|___________________________________________________________________|")
def exit_message():
                       print("THANK YOU")
                       print("SUBMITTED BY:-")
                       print(" ____________________________________________________ ")
                       print("|          |                      |                  |")
                       print("| ROLL NO. |         NAME         |        CLASS     |")
                       print("|__________|______________________|__________________|")
                       print("|          |                      |                  |")
                       print("|  12025   |  PRATHAM AGARWALLA   |        XII-A     |")
                       print("|  12085   |  RAGHAV SONI         |        XII-B     |")
                       print("|  12090   |  TANUJ SOOD          |        XII-B     |")
                       print("|__________|______________________|__________________|")                        
                        

ch='Y'
while ch=='y' or ch=='Y':
    main_menu()
    chm=int(input("ENTER YOUR CHOICE: "))
    if chm==1:
        collection()
        print("ENTER YOUR CHOICE: ")
        ch1=int(input())
        if ch1==1:
            print("ENTER THE CSV FILENAME ")
            x=input()
            print("THE CONTENT OF THE CSV FILE IS: ")
            df=pd.read_csv(x)
            print(df)
        elif ch1==2:
            print("ENTER THE TEXT FILENAME ")
            x=input()
            print("ENTER THE DELIMITER IN THE TEXT FILE ")
            y=input()
            print("THE CONTENT OF THE TEXT FILE IS: ")
            df=pd.read_csv(x,delimiter=y)
            print(df)
        elif ch1==3:
            main_menu()
            print("ENTER YOUR CHOICE: ")
            chm=int(input())
        else:
            print("INVALID NUMBER")
            print("RETURN TO MAIN MENU [Y/N] ")
            ch=input()
    elif chm==2:
        manipulation()
        print("ENTER YOUR CHOICE: ")
        ch2=int(input())
        if ch2==1:
            insert_row()
            print("ENTER YOUR CHOICE: ")
            ch6=int(input())
            df=pd.read_csv("cities.csv")
            if ch6==1:
                    print("ENTER CITY NAME: ")
                    cn=input()
                    print("ENTER STATE CODE: ")
                    sc=int(input())
                    print("ENTER STATE NAME: ")
                    sn=input()
                    print("ENTER TOTAL POPULATION: ")
                    tp=int(input())
                    print("ENTER MALE POPULATION: ")
                    mp=int(input())
                    print("ENTER FEMALE POPULATION: ")
                    fp=int(input())
                    print("ENTER LITERATES: ")
                    l=int(input())
                    print("ENTER MALE LITERATES: ")
                    ml=int(input())
                    print("ENTER FEMALE LITERATES: ")
                    fl=int(input())
                    print("ENTER SEX RATIO: ")
                    sr=int(input())
                    print("ENTER CHILD SEX RATIO: ")
                    csr=int(input())
                    print("ENTER LITERACY RATE: ")
                    lr=int(input())
                    print("ENTER MALE LITERACY RATE: ")
                    mlr=int(input())
                    print("ENTER FEMALE LITERACY RATE: ")
                    flr=int(input())
                    print("ENTER GRADUATES: ")
                    g=int(input())
                    print("ENTER MALE GRADUATES: ")
                    mg=int(input())
                    print("ENTER FEMALE GRADUATES: ")
                    fg=int(input())
                    data=[cn,sc,sn,tp,mp,fp,l,ml,fl,sr,csr,lr,mlr,flr,g,mg,fg]
                    la=len(df.index)
                    df.loc[la]=data
                    print(df)
            elif ch6==2:
                print(df)
                pos=int(input("ENTER THE POSITION: "))
                print("ENTER CITY NAME: ")
                cn=input()
                print("ENTER STATE CODE: ")
                sc=int(input())
                print("ENTER STATE NAME: ")
                sn=input()
                print("ENTER TOTAL POPULATION: ")
                tp=int(input())
                print("ENTER MALE POPULATION: ")
                mp=int(input())
                print("ENTER FEMALE POPULATION: ")
                fp=int(input())
                print("ENTER LITERATES: ")
                l=int(input())
                print("ENTER MALE LITERATES: ")
                ml=int(input())
                print("ENTER FEMALE LITERATES: ")
                fl=int(input())
                print("ENTER SEX RATIO: ")
                sr=int(input())
                print("ENTER CHILD SEX RATIO: ")
                csr=int(input())
                print("ENTER LITERACY RATE: ")
                lr=int(input())
                print("ENTER MALE LITERACY RATE: ")
                mlr=int(input())
                print("ENTER FEMALE LITERACY RATE: ")
                flr=int(input())
                print("ENTER GRADUATES: ")
                g=int(input())
                print("ENTER MALE GRADUATES: ")
                mg=int(input())
                print("ENTER FEMALE GRADUATES: ")
                fg=int(input())
                data=[cn,sc,sn,tp,mp,fp,l,ml,fl,sr,csr,lr,mlr,flr,g,mg,fg]
                df.loc[pos-1]=data
                print(df)
            elif ch6==3:
                manipulation()
                print("ENTER YOUR CHOICE: ")
                ch2=int(input())
            else:
                print("INVALID NUMBER")
        elif ch2==2:
            df=pd.read_csv("cities.csv")
            df2=df[['State Code','State']]
            df2=df2.drop_duplicates()
            print(df2)
            x=int(input("ENTER THE STATE CODE OF THE STATE WHOSE CITY'S RECORD YOU WISH TO DELETE: "))
            p=df.loc[df['State Code']==x]
            print(p)
            o=int(input("ENTER THE INDEX NUMBER OF THE CITY NAME TO BE DELETED: "))
            df.drop(o,inplace=True)
            print(df)
        elif ch2==3:
            update()
            print("ENTER YOUR CHOICE: ")
            ch7=int(input())
            df=pd.read_csv("cities.csv")
            df2=df[['State Code','State']]
            df2=df2.drop_duplicates()
            print(df2)
            x=int(input("ENTER THE STATE CODE OF THE STATE WHOSE CITY'S RECORD YOU WISH TO UPDATE: "))
            p=df.loc[df['State Code']==x]
            print(p)
            if ch7==1:
                print("ENTER THE INDEX NUMBER OF CITYNAME TO BE UPDATED: ")
                a=int(input())
                print("ENTER NEW TOTAL POPULATION: ")
                b=int(input())
                idx= next(iter(df[df["City Name"].index==a].index),'no match')
                df.loc[idx,"Total Population"]=b
                print(df)
            elif ch7==2:
                print("ENTER THE INDEX NUMBER OF CITYNAME TO BE UPDATED: ")
                a=int(input())
                print("ENTER NEW TOTAL LITERATES: ")
                b=int(input())
                idx= next(iter(df[df["City Name"].index==a].index),'no match')
                df.loc[idx,"Literates"]=b
                print(df)
            elif ch7==3:
                print("ENTER THE INDEX NUMBER OF CITYNAME TO BE UPDATED: ")
                a=int(input())
                print("ENTER NEW SEX RATIO: ")
                b=int(input())
                idx= next(iter(df[df["City Name"].index==a].index),'no match')
                df.loc[idx,"Sex Ratio"]=b
                print(df)
            elif ch7==4:
                print("ENTER THE INDEX NUMBER OF CITYNAME TO BE UPDATED: ")
                a=int(input())
                print("ENTER NEW LITERACY RATE: ")
                b=int(input())
                idx= next(iter(df[df["City Name"].index==a].index),'no match')
                df.loc[idx,"Literacy Rate"]=b
                print(df)
            elif ch7==5:
                print("ENTER THE INDEX NUMBER OF CITYNAME TO BE UPDATED: ")
                a=int(input())
                print("ENTER TOTAL GRADUATES: ")
                b=int(input())
                idx= next(iter(df[df["City Name"].index==a].index),'no match')
                df.loc[idx,"Graduates"]=b
                print(df)
            elif ch7==6:
                print("ENTER THE INDEX NUMBER OF CITYNAME TO BE UPDATED: ")
                a=int(input())
                print("ENTER NEW STATE CODE: ")
                b=int(input())
                idx= next(iter(df[df["City Name"].index==a].index),'no match')
                df.loc[idx,"State Code"]=b
                print(df)
            elif ch7==7:
                manipulation()
                print("ENTER YOUR CHOICE: ")
                ch2=int(input())
            else:
                print("INVALID NUMBER")
                print("RETURN TO MAIN MENU [Y/N] ")
                ch=input()
        elif ch2==4:
            df=pd.read_csv("cities.csv")
            sort()
            s=int(input())
            if s==1:
                sort_asc()
                print("ENTER YOUR CHOICE: ")
                ch8=int(input())
                if ch8==1:
                    df.sort_values("Total Population",inplace=True)
                    print(df)
                elif ch8==2:
                    df.sort_values("Literacy Rate",inplace=True)
                    print(df)
                elif ch8==3:
                    df.sort_values("Sex Ratio",inplace=True)
                    print(df)
                elif ch8==4:
                    df.sort_values("Graduates",inplace=True)
                    print(df)
                elif ch8==5:
                    df.sort_values("State",inplace=True)
                    print(df)
                elif ch8==6:
                    df.sort_values("Male Graduates",inplace=True)
                    print(df)
                elif ch8==7:
                    sort()
                else:
                    print("INVALID NUMBER")
            elif s==2:
                sort_des()
                print("ENTER YOUR CHOICE: ")
                ch8=int(input())
                if ch8==1:
                    df.sort_values("Total Population",inplace=True,ascending=False)
                    print(df)
                elif ch8==2:
                    df.sort_values("Literacy Rate",inplace=True,ascending=False)
                    print(df)
                elif ch8==3:
                    df.sort_values("Sex Ratio",inplace=True,ascending=False)
                    print(df)
                elif ch8==4:
                    df.sort_values("Graduates",inplace=True,ascending=False)
                    print(df)
                elif ch8==5:
                    df.sort_values("State",inplace=True,ascending=False)
                    print(df)
                elif ch8==6:
                    df.sort_values("Male Graduates",inplace=True,ascending=False)
                    print(df)
                elif ch8==7:
                    sort()
                else:
                    print("INVALID NUMBER")
                    print("RETURN TO MAIN MENU [Y/N] ")
                    ch=input()
        elif ch2==5:
            another_df()
            print("ENTER YOUR CHOICE: ")
            df=pd.read_csv("cities.csv")
            adf=int(input())
            if adf==1:
                 print("ENTER CSV FILENAME: ")
                 x=input()
                 print("THE CONTENT OF THE APPENDED DATAFRAME IS: ")
                 df1=pd.read_csv(x)
                 a=df.append(df1,ignore_index=True)
                 print(a)
            elif adf==2:
                 print("ENTER THE TEXT FILENAME")
                 x=input()
                 print("ENTER THE DELIMITER IN TEXT FILE")
                 y=input()
                 print("THE CONTENT OF APPENDED DATAFRAME IS:")
                 df1=pd.read_csv(x,delimiter=y)
                 a=df.append(df1,ignore_index=True)
                 print(a)
            elif adf==3:
                manipulation()
                print("ENTER YOUR CHOICE: ")
                ch2=int(input())
            else:
                print("INVALID NUMBER")
                print("RETURN TO MAIN MENU [Y/N] ")
                ch=input()
        elif ch2==6:
            main_menu()
            print("ENTER YOUR CHOICE: ")
            chm=int(input())
        else:
            print("INVALID NUMBER")
            print("RETURN TO MAIN MENU [Y/N] ")
            ch=input()
    elif chm==3:
        analysis()
        print("ENTER YOUR CHOICE: ")
        cha=int(input())
        if cha==1:
            df=pd.read_csv("cities.csv")
            n=int(input("ENTER THE NUMBER OF ROWS TO BE DISPLAYED "))
            print("THE FIRST",n,"RECORDS ARE: ")
            print(df.head(n))
        elif cha==2:
            df=pd.read_csv("cities.csv")
            n=int(input("ENTER THE NUMBER OF ROWS TO BE DISPLAYED "))
            print("THE LAST",n,"RECORDS ARE: ")
            print(df.tail(n))
        elif cha==3:
            df=pd.read_csv("cities.csv")
            column()
            print("ENTER YOUR CHOICE: ")
            chc=int(input())
            if chc==1:
                print("DISPLAYING PARTICULAR COLUMN(S) FROM THE DATAFRAME: ")
                df=pd.read_csv("cities.csv",usecols=['City Name','State','State Code'],index_col=0)
                print(df)
            elif chc==2:
                print("DISPLAYING PARTICULAR COLUMN(S) FROM THE DATAFRAME: ")
                df=pd.read_csv("cities.csv",usecols=['City Name','Total Population','Male Population','Female Population'],index_col=0)
                print(df)
            elif chc==3:
                print("DISPLAYING PARTICULAR COLUMN(S) FROM THE DATAFRAME: ")
                df=pd.read_csv("cities.csv",usecols=['City Name','Literates','Male Literates','Female Literates'],index_col=0)
                print(df)
            elif chc==4:
                print("DISPLAYING PARTICULAR COLUMN(S) FROM THE DATAFRAME: ")
                df=pd.read_csv("cities.csv",usecols=['City Name','Sex Ratio','Child Sex Ratio'],index_col=0)
                print(df)
            elif chc==5:
                print("DISPLAYING PARTICULAR COLUMN(S) FROM THE DATAFRAME: ")
                df=pd.read_csv("cities.csv",usecols=['City Name','Literacy Rate','Male Literacy Rate','Female Literacy Rate'],index_col=0)
                print(df)
            elif chc==6:
                print("DISPLAYING PARTICULAR COLUMN(S) FROM THE DATAFRAME: ")
                df=pd.read_csv("cities.csv",usecols=['City Name','Graduates','Male Graduates','Female Graduates'],index_col=0)
                print(df)
            elif chc==7:
                analysis()
                print("ENTER YOUR CHOICE: ")
                cha=int(input()) 
            else:
                print("INVALID NUMBER")
                print("RETURN TO MAIN MENU [Y/N] ")
                ch=input()
        elif cha==4:
            df=pd.read_csv("cities.csv")
            row()
            print("ENTER YOUR CHOICE: ")
            chr=int(input())
            if chr==1:
                df=pd.read_csv("cities.csv")
                x=input("ENTER THE STATE NAME IN BLOCK LETTERS")
                p=df.loc[df['State']==x]
                print(p)
            elif chr==2:
                df=pd.read_csv("cities.csv")
                c=df.loc[df['Female Population']>df['Male Population']]
                print(c)
            elif chr==3:
                df=pd.read_csv("cities.csv")
                c=df.loc[df['Female Literates']>df['Male Literates']]
                print(c)
            elif chr==4:
                df=pd.read_csv("cities.csv")
                c=df.loc[df['Female Graduates']>df['Male Graduates']]
                print(c)
            elif chr==5:
                df=pd.read_csv("cities.csv")
                c=df.loc[df['Total Population']==max(df['Total Population'])]
                print(c)
            elif chr==6:
                df=pd.read_csv("cities.csv")
                c=df.loc[df['Total Population']==min(df['Total Population'])]
                print(c)
            elif chr==7:
                df=pd.read_csv("cities.csv")
                c=df.loc[df['Child Sex Ratio']==max(df['Child Sex Ratio'])]
                print(c)
            elif chr==8:
                analysis()
                print("ENTER YOUR CHOICE: ")
                cha=int(input()) 
            else:
                print("INVALID NUMBER")
                print("RETURN TO MAIN MENU [Y/N] ")
                ch=input()
        elif cha==5:
            main_menu()
            print("ENTER YOUR CHOICE: ")
            chm=int(input())
        else:
                print("INVALID NUMBER")
                print("RETURN TO MAIN MENU [Y/N] ")
                ch=input()
    elif chm==4:
            visualisation()
            print("ENTER YOUR CHOICE: ")
            chv=int(input())
            df=pd.read_csv("cities.csv")
            city=df['City Name']
            sc=df['State Code']
            st=df['State']
            pop=df['Total Population']
            mpop=df['Male Population']
            fpop=df['Female Population']
            lit=df['Literates']
            mlit=df['Male Literates']
            flit=df['Female Literates']
            sr=df['Sex Ratio']
            csr=df['Child Sex Ratio']
            lr=df['Literacy Rate']
            mlr=df['Male Literacy Rate']
            flr=df['Female Literacy Rate']
            gr=df['Graduates']
            mgr=df['Male Graduates']
            fgr=df['Female Graduates']
            if chv==1:
                        plt.xlabel("CITY NAME",color='r',fontsize=14)
                        plt.xticks(rotation='vertical')
                        fig=plt.gcf()
                        fig.set_size_inches(50,10,forward=True)
                        line_graph()
                        gl=int(input("ENTER YOUR CHOICE: "))
                        if gl==1:
                            plt.ylabel("TOTAL POPULATION",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL POPULATION",color='r',fontsize=20)
                            plt.plot(city,pop)
                            plt.legend(loc="upper left")
                            plt.show()
                        elif gl==2:
                            plt.ylabel("TOTAL LITERATES",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL LITERATES",color='r',fontsize=20)
                            plt.plot(city,lit)
                            plt.legend(loc="upper left")
                            plt.show()
                        elif gl==3:
                            plt.ylabel("CHILD SEX RATIO",color='r',fontsize=14)
                            plt.title("CITY vs CHILD SEX RATIO",color='r',fontsize=20)
                            plt.plot(city,csr)
                            plt.legend(loc="upper left")
                            plt.show()
                        elif gl==4:
                            plt.ylabel("TOTAL LITERACY RATE",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL LITERACY RATE",color='r',fontsize=20)
                            plt.plot(city,lr)
                            plt.show()   
                        elif gl==5:
                            plt.ylabel("TOTAL GRADUATES",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL GRADUATES",color='r',fontsize=20)
                            plt.plot(city,gr)
                            plt.legend(loc="upper left")
                            plt.show()
                        elif gl==6:
                            plt.ylabel("TOTAL MALE GRADUATES",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL MALE GRADUATES",color='r',fontsize=20)
                            plt.plot(city,mgr)
                            plt.legend(loc="upper left")
                            plt.show()
                        elif gl==7:
                            plt.ylabel("TOTAL FEMALE GRADUATES",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL FEMALE GRADUATES",color='r',fontsize=20)
                            plt.plot(city,fgr)
                            plt.legend(loc="upper left")
                            plt.show()
                        elif gl==8:
                            visualisation()
                            print("ENTER YOUR CHOICE: ")
                            chv=int(input())
                        else:
                            print("INVALID NUMBER")
                            print("RETURN TO MAIN MENU [Y/N] ")
                            ch=input()
            elif chv==2:
                        plt.xlabel("CITY NAME",color='r',fontsize=14)
                        plt.xticks(rotation='vertical')
                        fig=plt.gcf()
                        fig.set_size_inches(50,10,forward=True)
                        bar_graph()
                        chb=int(input("ENTER YOUR CHOICE: "))
                        if chb==1:
                            plt.ylabel("TOTAL MALE POPULATION",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL MALE POPULATION",color='r',fontsize=20)
                            plt.bar(city,mpop)
                            plt.show()    
                        elif chb==2:
                            plt.ylabel("TOTAL FEMALE POPULATION",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL FEMALE POPULATION",color='r',fontsize=20)
                            plt.bar(city,fpop)
                            plt.show()
                        elif chb==3:
                            plt.ylabel("TOTAL MALE LITERATES",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL MALE LITERATES",color='r',fontsize=20)
                            plt.bar(city,mlit)
                            plt.show()
                        elif chb==4:
                            plt.ylabel("TOTAL FEMALE LITERATES",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL FEMALE LITERATES",color='r',fontsize=20)
                            plt.bar(city,flit)
                            plt.show()
                        elif chb==5:
                            plt.ylabel("CHILD SEX RATIO",color='r',fontsize=14)
                            plt.title("CITY vs CHILD SEX RATIO",color='r',fontsize=20)
                            plt.bar(city,csr)
                            plt.show()
                        elif chb==6:
                            plt.ylabel("TOTAL MALE LITERACY RATE",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL MALE LITERACY RATE",color='r',fontsize=20)
                            plt.bar(city,mlr)
                            plt.show()   
                        elif chb==7:
                            plt.ylabel("TOTAL FEMALE LITERACY RATE",color='r',fontsize=14)
                            plt.title("CITY vs TOTAL FEMALE LITERACY RATE",color='r',fontsize=20)
                            plt.bar(city,flr)
                            plt.show() 
                        elif chb==8:
                            visualisation()
                            print("ENTER YOUR CHOICE: ")
                            chv=int(input())
                        else:
                            print("INVALID NUMBER")
                            print("RETURN TO MAIN MENU [Y/N] ")
                            ch=input()
            elif chv==3:
                        plt.xlabel("CITY NAME",color='r',fontsize=14)
                        plt.xticks(rotation='vertical')
                        fig=plt.gcf()
                        fig.set_size_inches(50,10,forward=True)
                        multibar_graph()
                        chmb=int(input("ENTER YOUR CHOICE: "))
                        if chmb==1:
                            plt.ylabel("POPULATION",color='r',fontsize=14)
                            plt.title("TOTAL MALE-FEMALE POPULATION OF DIFFERENT CITIES ",color='r',fontsize=20)
                            plt.bar(city,mpop,label="TOTAL MALE POPULATION",color='b')
                            plt.bar(city,fpop,label="TOTAL FEMALE POPULATION",color='red')
                            plt.legend(loc="upper left")
                            plt.show()  
                        elif chmb==2:
                            plt.ylabel("POPULATION",color='r',fontsize=14)
                            plt.title("TOTAL MALE-FEMALE LITERATES OF DIFFERENT CITIES",color='r',fontsize=20)
                            plt.bar(city,mlit,label="TOTAL MALE LITERATES",color='b')
                            plt.bar(city,flit,label="TOTAL FEMALE LITERATES",color='red')
                            plt.legend(loc="upper left")
                            plt.show()
                        elif chmb==3:
                            plt.ylabel("POPULATION",color='r',fontsize=14)
                            plt.title("TOTAL MALE-FEMALE LITRACY RATE OF DIFFERENT CITIES ",color='r',fontsize=20)
                            plt.bar(city,mlr,label="TOTAL MALE LITRACY RATE",color='b')
                            plt.bar(city,flr,label="TOTAL FEMALE LITRACY RATE",color='red')
                            plt.legend(loc="upper left")
                            plt.show()
                        elif chmb==4:
                            plt.ylabel("POPULATION",color='r',fontsize=14)
                            plt.title("TOTAL MALE-FEMALE GRADUAGETS OF DIFFERENT CITIES ",color='r',fontsize=20)
                            plt.bar(city,mgr,label="TOTAL MALE GRADUATES",color='b')
                            plt.bar(city,fgr,label="TOTAL FEMALE GRADUATES",color='red')
                            plt.legend(loc="upper left")
                            plt.show()
                        elif chmb==5:
                            visualisation()
                            print("ENTER YOUR CHOICE: ")
                            chv=int(input())
                        else:
                            print("INVALID NUMBER")
                            print("RETURN TO MAIN MENU [Y/N] ")
                            ch=input()
            elif chv==4:
                main_menu()
                print("ENTER YOUR CHOICE: ")
                chm=int(input())
            else:
                print("INVALID NUMBER")
                print("RETURN TO MAIN MENU [Y/N] ")
                ch=input()
    elif chm==5:
            exit_message()
            sys.exit(0)
    else:
        print("INVALID NUMBER")
        print("RETURN TO MAIN MENU [Y/N] ")
        ch=input()

        while ch=='n' or ch=='N':
            exit_message()
            break