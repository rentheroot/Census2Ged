# Census2Ged

## Purpose
Converts census transcriptions made in [Genscriber](http://www.genscriber.com/genapps/) to gedcom files. You can see some of my posts about Census2Ged [here](https://famgenealogy.blogspot.com/p/my-programs.html)

## Screenshots
![Screenshot of Census2Ged](https://raw.githubusercontent.com/xXReneeXx/Census2Ged/master/screenshot.PNG)

## Default Tags
| Option Name      | Default Tag | Suggested Tag         |
|------------------|-------------|-----------------------|
| Immigration Year | IMMI        | Don't Change          |
| Occupation       | OCCU        | Don't Change          |
| Race             | DSCR        | Race                  |
| Naturalization   | NATU        | Naturalization Status |

## Handling of Custom Tags
The program handles custom tags as recommended in the Gedcom 5.5.1 standard. This will allow them to be compatible with virtually every genealogy program available.

The following is the format the program writes these custom tags in. It uses an 'EVEN' (event) tag, then modifies it with a 'TYPE' tag.

```
1 EVEN description of event
2 TYPE new tag name
```

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
-[ ] Number of dwelling in order of visitation
-[ ] Number of family, in order of visitation
-[X] Name of each person whose place of abode on April 15, 1910, was in this family. Enter surname first, then the given name and middle initial, if any. Include every person living on April 15, 1910. Omit children born since April 15, 1910
-[X] Relationship of this person to the head of the family

