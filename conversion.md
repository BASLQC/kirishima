## Record of all changes made

* All JSON is converted from XML to JSON.
* XML Artifacts
  * `"@` is replaced with `"`.
  * "item" is renamed to the current name of the file.
* Any stray integers `\"(\d+)\"` have their quotes removed `\1`, so they aren't imported as strings.

### Files Used

* ConstructTime
* Equipment
* EquipType
* Expedition
* Map
* Quest
* QuestType
* Ship
* ShipType

### Renames

```
Develop - EquipmentRecipes
Construct - SpecialRecipes
```
 
### Period

The period is the period of recurrence of the event. Either daily, weekly, monthly, or no recurrence.

* The QuestType file is eliminated.
* The rest of the values replaced with the following conversions:

```
1 - none
2 - daily
3 - weekly
4 - monthly
```

### Translated Variables

Match without case sensitive.

```
huoLi - firepower
leiZhuang - Torpedo
duiKong - antiair
mingZhong - hitrate
huiBi - evasion
suoDi - lineOfSight
zhuangJia - armor
duiQian - antisub
```

### Ship Info

There are three variables not provided directly by the API:

* 

These may be derived variables. Perhaps the reason why these are in Ship.xml and not anything else is that the variables are only visible to the user by sight, not from the API (and were thus gathered by hand by Chinese strategists).

ShipData is then merged together with the three variables and other info from Ship.xml 

## Kancolle API Dump JSON analysis

Everything is contained in the returned `data` structure:

### `mst_ship`
