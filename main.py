# imports
import pandas as pd
import lxml


# function to clean data##

def cleaner(match):
    def cleaner(match):
        match['team']= match['Unnamed: 0'].str.split(' ').str[1]
        match['name']= match['Unnamed: 0'].str.split(' ').str[0]

        match['atk ACS']= match['ACS'].str.split(' ').str[2].astype(int)
        match['def ACS']= match['ACS'].str.split(' ').str[4].astype(int)
        match['ACS']= match['ACS'].str.split(' ').str[0].astype(int)

        match['atk K']= match['K'].str.split(' ').str[2].astype(int)
        match['def K']= match['K'].str.split(' ').str[4].astype(int)
        match['K']= match['K'].str.split(' ').str[0].astype(int)

        match['atk D']= match['D'].str.split(' ').str[4].astype(int)
        match['def D']= match['D'].str.split(' ').str[6].astype(int)
        match['D']= match['D'].str.split(' ').str[2].astype(int)

        match['atk A']= match['A'].str.split(' ').str[2].astype(int)
        match['def A']= match['A'].str.split(' ').str[4].astype(int)
        match['A']= match['A'].str.split(' ').str[0].astype(int)

        match['atk KAST']= match['KAST'].str.split('%').str[1].astype(int)
        match['def KAST']= match['KAST'].str.split('%').str[2].astype(int)
        match['KAST']= match['KAST'].str.split('%').str[0].astype(int)

        match['atk ADR']= match['ADR'].str.split(' ').str[2].astype(int)
        match['def ADR']= match['ADR'].str.split(' ').str[4].astype(int)
        match['ADR']= match['ADR'].str.split(' ').str[0].astype(int)

        match['atk HS%']= match['HS%'].str.split('%').str[1].astype(int)
        match['def HS%']= match['HS%'].str.split('%').str[2].astype(int)
        match['HS%']= match['HS%'].str.split('%').str[0].astype(int)

        match['atk FK']= match['FK'].str.split(' ').str[2].astype(int)
        match['def FK']= match['FK'].str.split(' ').str[4].astype(int)
        match['FK']= match['FK'].str.split(' ').str[0].astype(int)

        match['atk FD']=match['FD'].str.split(' ').str[2].astype(int)
        match['def FD']=match['FD'].str.split(' ').str[4].astype(int)
        match['FD']=match['FD'].str.split(' ').str[0].astype(int)

        match.drop(['Unnamed: 0','Unnamed: 1','+/–','+/–.1'],axis=1,inplace=True)

# main function
print('please enter link')
matchlink = str(input())
try:
    matches = pd.read_html(matchlink)
except:
    print('given link is invalid')
no_of_maps = len(matches) / 2 - 1


def m1():
    map1 = pd.concat([matches[0], matches[1]])
    cleaner(map1)
    map1.to_csv('map1.csv')


def m2():
    map2 = pd.concat([matches[4], matches[5]])
    cleaner(map2)
    map2.to_csv('map2.csv')


def m3():
    map3 = pd.concat([matches[6], matches[7]])
    cleaner(map3)
    map3.to_csv('map3.csv')


def m4():
    map4 = pd.concat([matches[8], matches[9]])
    cleaner(map4)
    map4.to_csv('map4.csv')


def m5():
    map5 = pd.concat([matches[10], matches[11]])
    cleaner(map5)
    map5.to_csv('map5.csv')


def ovrl():
    overall = pd.concat([matches[2], matches[3]])
    cleaner(overall)
    overall.to_csv('overall.csv')


def vlr_match_CSV(no_of_maps):
    if no_of_maps == 1:
        m1()
    elif no_of_maps == 2:
        m1(), m2(), ovrl()
    elif no_of_maps == 3:
        m1(), m2(), m3(), ovrl()
    elif no_of_maps == 4:
        m1(), m2(), m3(), m4(), ovrl()
    elif no_of_maps():
        m1(), m2(), m3(), m4(), m5(), ovrl()
    else:
        pass


vlr_match_CSV(no_of_maps)
