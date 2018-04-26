# Census2Ged
Like this project? Send a couple dollars my way and/or visit my blog to see what else I'm up to!
- [Paypal](https://www.paypal.me/ReneeSchmidt)
- [Blog](https://famgenealogy.blogspot.com/)
## Purpose
Converts census transcriptions made in [Genscriber](http://www.genscriber.com/genapps/) to gedcom files. You can see some of my posts about Census2Ged [here](https://famgenealogy.blogspot.com/p/my-programs.html)

## Screenshots
![Screenshot of Census2Ged](https://raw.githubusercontent.com/xXReneeXx/Census2Ged/master/screenshot.PNG)

## Default Tags
Census2Ged picks out gedcom 5.5.1 compliant tags for each piece of information for you, however you may wish to change these (they will still be gedcom 5.5.1 compliant, but they will use EVEN and TYPE tags instead).

| Option Name      | Default Tag | Suggested Tag         |
|------------------|-------------|-----------------------|
| Immigration Year | IMMI        | Don't Change          |
| Occupation       | OCCU        | Don't Change          |
| Race             | DSCR        | Race                  |
| Naturalization   | NATU        | Naturalization Status |
| Literacy         | EDUC        | Literacy              |
| Children Born    | DSCR        | Number of Children    |


## Handling of Custom Tags
The program handles custom tags as recommended in the Gedcom 5.5.1 standard. This will allow them to be compatible with virtually every genealogy program available.

The following is the format the program writes these custom tags in. It uses an 'EVEN' (event) tag, then modifies it with a 'TYPE' tag.

```
1 EVEN description of event
2 TYPE new tag name
```
## Handling of Dates, Years, and Ages
Approximate birth dates are calculated using the year of the census - age of the person at the time if the birth date is not explicitly specified. If the age of a person is a fraction it is changed to 0. Year of the census is attached to all of the applicable facts.

## Supported Relationship Types
Census2Ged currently supports the following relationship types:
- Head
- Wife
- Son
- Daughter
- Child

## Types of Data (Supported and Unsupported) For Each Census
The goal is to eventually present every piece of information in some way for every census. I have copied the names of each of the fields from the [IPUMS enumeration forms](https://usa.ipums.org/usa/voliii/tEnumForm.shtml)
### 1910 Census

**LOCATION:
STREET, AVENUE, ROAD, ETC.
HOUSE NUMBER (IN CITIES AND TOWNS)**

- [ ] Number of dwelling in order of visitation
- [ ] Number of family, in order of visitation
- [X] Name of each person whose place of abode on April 15, 1910, was in this family. Enter surname first, then the given name and middle initial, if any. Include every person living on April 15, 1910. Omit children born since April 15, 1910
- [X] Relationship of this person to the head of the family

**PERSONAL DESCRIPTION:**

- [X] Sex
- [X] Color or Race
- [X] Age at last birthday (partially supported through calculation of aprox. date of birth)
- [ ] Whether single, married, widowed, or divorced
- [X] Number of years of present marriage (partially supported through calculation of aprox. date of marriage)
- [X] Mother of how many children, Number born, Number now living

**NATIVITY:
PLACE OF BIRTH OF EACH PERSON AND PARENTS OF EACH PERSON ENUMERATED. IF BORN IN THE UNITED STATES, GIVE THE STATE OR TERRITORY. IF OF FOREIGN BIRTH, GIVE THE COUNTRY**

- [X] Place of birth of this person
- [ ] Place of birth of father of this person
- [ ] Place of birth of mother of this person

**CITIZENSHIP**

- [X] Year of immigration to the United States
- [X] Whether naturalized or alien
- [X] Whether able to speak English; or, if not, give language spoken

**OCCUPATION:**

- [X] Trade or profession of, or particular kind of work done by this person, as spinner, salesman, laborer, etc.
- [X] General nature of industry, business, or establishment in which this person works, as cotton mill, dry goods store, farm, etc.
- [ ] Whether an employer, employee, or working on own account.

**IF AN EMPLOYEE:**

- [ ] Whether out of work on April 15, 1910
- [ ] Number of weeks out of work during year 1909

**EDUCATION:**

- [X] Whether able to read, Whether able to write
- [ ] Attended school any time since September 1, 1909

**OWNERSHIP OF HOME:**

- [X] Owned or rented
- [X] Owned free or mortgaged
- [X] Farm or house
- [X] Number of farm schedule.
- [X] Whether a survivor of the Union or Confederate Army or Navy
- [X] Whether blind (both eyes).
- [X] Whether deaf and dumb.
