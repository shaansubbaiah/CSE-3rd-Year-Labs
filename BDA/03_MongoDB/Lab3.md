## BDA LAB-3

### MongoDB

1. Create a new collection
 ```
 use Student
 ```

2. Insert a value
```json
db.Student.insert({
    "Name" : "XYZ",
    "RollNo:" : 1,
    "Age" : 21,
    "ContactNo" : "1234567890",
    "EmailId": "user1@lab.com"
})
 ```

3. Insert multiple values at once
```json
var MyStudents = [
    {
        "Name" : "ABC",
        "RollNo:" : 3,
        "Age" : 22,
        "ContactNo" : "2234567890",
        "EmailId": "user2@lab.com"
    },
    {
        "Name" : "DEF",
        "RollNo:" : 5,
        "Age" : 21,
        "ContactNo" : "3234567890",
        "EmailId" : "user3@lab.com"
    },
    {
        "Name" : "GHI",
        "RollNo:" : 7,
        "Age" : 20,
        "ContactNo" : "4234567890",
        "EmailId" : "user4@lab.com"
    },
    {
        "Name" : "JKL",
        "RollNo:" : 10,
        "Age" : 18,
        "ContactNo" : "5234567890",
        "EmailId" : "user5@lab.com"
    },
]

db.Student.insert(MyStudents);
 ```

4. Print all current values
```json
db.getCollection('Student').find({}).forEach(printjson)
```
```json
{
	"_id" : ObjectId("606ad5a6e581cc0b904470a5"),
	"Name" : "XYZ",
	"RollNo:" : 1,
	"Age" : 21,
	"ContactNo" : "1234567890",
	"EmailId" : "user1@lab.com"
}
{
	"_id" : ObjectId("606ad60fe581cc0b904470a6"),
	"Name" : "ABC",
	"RollNo:" : 3,
	"Age" : 22,
	"ContactNo" : "2234567890",
	"EmailId" : "user2@lab.com"
}
{
	"_id" : ObjectId("606ad60fe581cc0b904470a7"),
	"Name" : "DEF",
	"RollNo:" : 5,
	"Age" : 21,
	"ContactNo" : "3234567890",
	"EmailId" : "user3@lab.com"
}
{
	"_id" : ObjectId("606ad60fe581cc0b904470a8"),
	"Name" : "GHI",
	"RollNo:" : 7,
	"Age" : 20,
	"ContactNo" : "4234567890",
	"EmailId" : "user4@lab.com"
}
{
	"_id" : ObjectId("606ad60fe581cc0b904470a9"),
	"Name" : "JKL",
	"RollNo:" : 10,
	"Age" : 18,
	"ContactNo" : "5234567890",
	"EmailId" : "user5@lab.com"
}
```
5.  Update RollNo of a student
```json
db.Student.update(
{"RollNo:" : 10},
{$set: { "EmailId" : "modified@lab.com"}});
```
```json
db.getCollection('Student').find({"RollNo:":10}).forEach(printjson)
```
```json
{
	"_id" : ObjectId("606ad60fe581cc0b904470a9"),
	"Name" : "JKL",
	"RollNo:" : 10,
	"Age" : 18,
	"ContactNo" : "5234567890",
	"EmailId" : "modified@lab.com"
}
```
6.  Update Name of a student
```json
db.Student.update(
{"Name" : "XYZ"},
{$set: { "Name" : "EcksWhyZee"}});
```
```json
db.getCollection('Student').find({"Name" : "EcksWhyZee"}).forEach(printjson)
```
```json
{
	"_id" : ObjectId("606ad5a6e581cc0b904470a5"),
	"Name" : "EcksWhyZee",
	"RollNo:" : 1,
	"Age" : 21,
	"ContactNo" : "1234567890",
	"EmailId" : "user1@lab.com"
}
```
7.  Export to json
```
mongoexport --db testdb --collection Student --out C:\Users\shaan\Desktop\Exported\Student.json
```
```json
{"_id":{"$oid":"606ad5a6e581cc0b904470a5"},"Name":"EcksWhyZee","RollNo:":1.0,"Age":21.0,"ContactNo":"1234567890","EmailId":"user1@lab.com"}

{"_id":{"$oid":"606ad60fe581cc0b904470a6"},"Name":"ABC","RollNo:":3.0,"Age":22.0,"ContactNo":"2234567890","EmailId":"user2@lab.com"}

{"_id":{"$oid":"606ad60fe581cc0b904470a7"},"Name":"DEF","RollNo:":5.0,"Age":21.0,"ContactNo":"3234567890","EmailId":"user3@lab.com"}

{"_id":{"$oid":"606ad60fe581cc0b904470a8"},"Name":"GHI","RollNo:":7.0,"Age":20.0,"ContactNo":"4234567890","EmailId":"user4@lab.com"}

{"_id":{"$oid":"606ad60fe581cc0b904470a9"},"Name":"JKL","RollNo:":10.0,"Age":18.0,"ContactNo":"5234567890","EmailId":"modified@lab.com"}
```
8.  Drop Student
```json
db.getCollection('Student').drop()
```
9.  Import from exported file
```
mongoimport --db testdb --collection Student C:\Users\shaan\Desktop\Exported\Student.json
``` 
---
