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
1 EVEN value of tag
2 TYPE new tag name
```

